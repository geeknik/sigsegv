"""
Extract ALL missing localization keys across all modified .cs files
by comparing git HEAD with current version.
"""
import subprocess
import re
import json
import os

# Load existing keys
with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

# Get list of all used keys
result = subprocess.run(
    ['grep', '-roE', r'Loc\.Get\("[a-z]+\.[a-z_0-9]+"', 'Scripts/'],
    capture_output=True, text=True, encoding='utf-8'
)
used_keys = set()
for line in result.stdout.strip().split('\n'):
    m = re.search(r'Loc\.Get\("([a-z]+\.[a-z_0-9]+)"', line)
    if m:
        used_keys.add(m.group(1))

missing_keys = {k for k in used_keys if k not in en}
print(f"Total missing keys: {len(missing_keys)}")

# Group by file - find which files contain these missing keys
key_to_files = {}
for line in result.stdout.strip().split('\n'):
    m = re.match(r'(.+?):.*Loc\.Get\("([a-z]+\.[a-z_0-9]+)"', line)
    if m and m.group(2) in missing_keys:
        key_to_files.setdefault(m.group(2), set()).add(m.group(1))

# Get unique files that need processing
files_to_process = set()
for key, files in key_to_files.items():
    for f in files:
        files_to_process.add(f)

print(f"Files with missing keys: {len(files_to_process)}")
for f in sorted(files_to_process):
    count = sum(1 for k, fs in key_to_files.items() if f in fs)
    print(f"  {f}: {count} missing keys")

# Extract from each file's diff
all_extracted = {}

for filepath in sorted(files_to_process):
    # Get diff for this file
    result = subprocess.run(
        ['git', 'diff', '-U0', filepath],
        capture_output=True, text=True, encoding='utf-8'
    )
    diff_lines = result.stdout.split('\n')

    colors = {'red', 'green', 'blue', 'yellow', 'cyan', 'white', 'gray', 'bright_red',
              'bright_green', 'bright_yellow', 'bright_cyan', 'bright_white', 'dark_gray',
              'dark_magenta', 'dark_red', 'bright_blue', 'dark_cyan', 'dark_green',
              'ConsoleColor.Yellow', 'ConsoleColor.White', 'ConsoleColor.Red', 'ConsoleColor.Cyan',
              'ConsoleColor.Green', 'ConsoleColor.Gray', 'ConsoleColor.Magenta'}

    i = 0
    while i < len(diff_lines):
        line = diff_lines[i]
        hunk_match = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
        if hunk_match:
            i += 1
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

            for a_idx, a_line in enumerate(added):
                loc_matches = re.findall(r'Loc\.Get\("([a-z]+\.[a-z_0-9]+)"', a_line)
                for key in loc_matches:
                    if key in en or key in all_extracted:
                        continue
                    if key not in missing_keys:
                        continue

                    best_original = None
                    # Try same index
                    if a_idx < len(removed):
                        r_line = removed[a_idx]
                        strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                        meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                      and not re.match(r'^[a-z]+\.[a-z_]', s) and s != 'false' and s != 'true']
                        if meaningful:
                            best_original = max(meaningful, key=len)

                    # Try all removed lines
                    if not best_original:
                        a_stripped = a_line.strip()
                        for r_line in removed:
                            r_stripped = r_line.strip()
                            if ('terminal.Write' in a_stripped and 'terminal.Write' in r_stripped) or \
                               ('WriteBoxHeader' in a_stripped and 'WriteBoxHeader' in r_stripped) or \
                               ('terminal.GetInput' in a_stripped and 'terminal.GetInput' in r_stripped):
                                strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                                meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                              and not re.match(r'^[a-z]+\.[a-z_]', s) and s != 'false' and s != 'true']
                                if meaningful:
                                    best_original = max(meaningful, key=len)
                                    break

                    if best_original:
                        # Clean up interpolation
                        counter = [0]
                        def replace_interp(m):
                            r = '{' + str(counter[0]) + '}'
                            counter[0] += 1
                            return r
                        cleaned = re.sub(r'\{[a-zA-Z_][a-zA-Z_0-9.()]*(?:\?[^}]*)?\}', replace_interp, best_original)
                        all_extracted[key] = cleaned
                    else:
                        all_extracted[key] = f"TODO: {key}"
        else:
            i += 1

# Report
found = sum(1 for v in all_extracted.values() if not v.startswith('TODO:'))
todo = sum(1 for v in all_extracted.values() if v.startswith('TODO:'))
still_missing = missing_keys - set(all_extracted.keys())

print(f"\nExtracted: {found} with values, {todo} need manual review")
print(f"Still missing (not found in diff): {len(still_missing)}")

# Save extracted
with open('tools/all_missing_keys.json', 'w', encoding='utf-8') as f:
    json.dump(all_extracted, f, ensure_ascii=False, indent=2)

# Show TODOs and still missing
if todo > 0:
    print("\nKeys needing manual review:")
    for k, v in sorted(all_extracted.items()):
        if v.startswith('TODO:'):
            print(f"  {k}")

if still_missing:
    print(f"\nKeys not found in any diff ({len(still_missing)}):")
    for k in sorted(still_missing)[:20]:
        print(f"  {k}")
    if len(still_missing) > 20:
        print(f"  ... and {len(still_missing) - 20} more")

# Add to en.json and es.json
added = 0
for key, value in all_extracted.items():
    if key not in en and not value.startswith('TODO:'):
        en[key] = value
        added += 1
    if key not in es and not value.startswith('TODO:'):
        es[key] = value  # Use English as fallback for now

with open('Localization/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, ensure_ascii=False, indent=2)

print(f"\nAdded {added} keys to en.json and es.json")
print(f"Final totals: en={len(en)}, es={len(es)}")
