"""
Extract missing base.* localization keys by comparing git HEAD version
of BaseLocation.cs with current version. For each Loc.Get("base.xxx") call
in the current file, find the corresponding hardcoded English string from
the original file by matching surrounding context lines.
"""
import subprocess
import re
import json

# Get the diff
result = subprocess.run(
    ['git', 'diff', '-U3', 'Scripts/Locations/BaseLocation.cs'],
    capture_output=True, text=True, encoding='utf-8'
)
diff = result.stdout

# Load existing keys
with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

# Parse diff hunks to find old line -> new line pairs
# We look for removed lines (starting with -) that have English strings
# paired with added lines (starting with +) that have Loc.Get("base.xxx")
missing_keys = {}

lines = diff.split('\n')
i = 0
while i < len(lines):
    line = lines[i]

    # Look for removed lines with English strings
    if line.startswith('-') and not line.startswith('---'):
        # Collect consecutive removed lines
        removed = []
        while i < len(lines) and lines[i].startswith('-') and not lines[i].startswith('---'):
            removed.append(lines[i][1:])  # strip the -
            i += 1

        # Collect consecutive added lines
        added = []
        while i < len(lines) and lines[i].startswith('+') and not lines[i].startswith('+++'):
            added.append(lines[i][1:])  # strip the +
            i += 1

        # Match removed/added lines that are similar
        for r_line in removed:
            for a_line in added:
                # Find Loc.Get("base.xxx") in added line
                loc_matches = re.findall(r'Loc\.Get\("(base\.[a-z_0-9]+)"(?:,\s*(.+?))?\)', a_line)
                if not loc_matches:
                    continue

                for key, args in loc_matches:
                    if key in en:
                        continue  # already defined
                    if key in missing_keys:
                        continue  # already found

                    # Try to extract the original English string from the removed line
                    # Look for quoted strings in the removed line
                    str_matches = re.findall(r'"([^"]+)"', r_line)
                    if str_matches:
                        # Pick the longest string as the most likely original
                        original = max(str_matches, key=len)
                        if len(original) > 2:  # skip single chars
                            # If the key has format args, convert $"...{var}..." to "...{0}..."
                            if args:
                                # The original likely has interpolated variables
                                # Replace {var} patterns with {0}, {1}, etc
                                counter = [0]
                                def replace_interp(m):
                                    result = '{' + str(counter[0]) + '}'
                                    counter[0] += 1
                                    return result
                                original = re.sub(r'\{[^}]+\}', replace_interp, original)
                            missing_keys[key] = original
    else:
        i += 1

# Print results
print(f"Found {len(missing_keys)} missing keys from diff analysis")
print()

# Write them out
for k, v in sorted(missing_keys.items()):
    print(f'  "{k}": "{v}",')
