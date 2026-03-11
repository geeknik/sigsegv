"""
Compare original and modified BaseLocation.cs line by line using unified diff.
For each Loc.Get("base.xxx") in the new file, find the corresponding original
English string by looking at what was replaced in that exact diff hunk position.
"""
import subprocess
import re
import json

# Load existing keys
with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

# Get unified diff with more context
result = subprocess.run(
    ['git', 'diff', '-U0', 'Scripts/Locations/BaseLocation.cs'],
    capture_output=True, text=True, encoding='utf-8'
)
diff_lines = result.stdout.split('\n')

missing_keys = {}

i = 0
while i < len(diff_lines):
    line = diff_lines[i]

    # Parse hunk header: @@ -old_start,old_count +new_start,new_count @@
    hunk_match = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
    if hunk_match:
        i += 1
        # Collect removed and added lines for this hunk
        removed = []
        added = []
        while i < len(diff_lines):
            if diff_lines[i].startswith('-') and not diff_lines[i].startswith('---'):
                removed.append(diff_lines[i][1:])
                i += 1
            elif diff_lines[i].startswith('+') and not diff_lines[i].startswith('+++'):
                added.append(diff_lines[i][1:])
                i += 1
            elif diff_lines[i].startswith(' '):
                i += 1
            else:
                break

        # For each added line with Loc.Get("base.xxx"), find the matching removed line
        for a_idx, a_line in enumerate(added):
            loc_matches = re.findall(r'Loc\.Get\("(base\.[a-z_0-9]+)"', a_line)
            for key in loc_matches:
                if key in en or key in missing_keys:
                    continue

                # Try to find corresponding removed line
                # Strategy: look at removed line at same index, or search for similar structure
                best_original = None

                # First try: same index position
                if a_idx < len(removed):
                    r_line = removed[a_idx]
                    # Extract quoted strings
                    strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                    # Filter to meaningful strings (not colors, not empty)
                    colors = {'red', 'green', 'blue', 'yellow', 'cyan', 'white', 'gray', 'bright_red',
                              'bright_green', 'bright_yellow', 'bright_cyan', 'bright_white', 'dark_gray',
                              'dark_magenta', 'dark_red', 'bright_blue', 'dark_cyan', 'dark_green'}
                    meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                  and not s.startswith('base.') and s != 'false']
                    if meaningful:
                        best_original = max(meaningful, key=len)

                # Second try: search all removed lines for similar indentation/structure
                if not best_original:
                    a_stripped = a_line.strip()
                    for r_line in removed:
                        r_stripped = r_line.strip()
                        # Check if they have similar structure (same method call pattern)
                        if ('terminal.Write' in a_stripped and 'terminal.Write' in r_stripped) or \
                           ('terminal.SetColor' in a_stripped and 'terminal.SetColor' in r_stripped):
                            strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                            meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                          and not s.startswith('base.') and s != 'false']
                            if meaningful:
                                best_original = max(meaningful, key=len)
                                break

                if best_original:
                    # Clean up interpolation: replace {variable} with {0}, {1}, ...
                    counter = [0]
                    def replace_interp(m):
                        r = '{' + str(counter[0]) + '}'
                        counter[0] += 1
                        return r
                    cleaned = re.sub(r'\{[a-zA-Z_][a-zA-Z_0-9.()]*\}', replace_interp, best_original)
                    missing_keys[key] = cleaned
                else:
                    missing_keys[key] = f"MISSING: {key}"
    else:
        i += 1

# Output as JSON for review
found = sum(1 for v in missing_keys.values() if not v.startswith('MISSING:'))
missing = sum(1 for v in missing_keys.values() if v.startswith('MISSING:'))
print(f"Found {found} keys with values, {missing} keys without values")
print(f"Total: {len(missing_keys)} missing keys")
print()

# Write to a JSON file for review
with open('tools/base_keys_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(missing_keys, f, ensure_ascii=False, indent=2)

print("Written to tools/base_keys_extracted.json")
print()
# Show first 30 for review
for i, (k, v) in enumerate(sorted(missing_keys.items())):
    if i >= 40:
        print(f"  ... and {len(missing_keys) - 40} more")
        break
    marker = " *** " if v.startswith("MISSING:") else ""
    print(f'  "{k}": "{v}"{marker}')
