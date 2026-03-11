"""
Extract all missing localization keys using pre-computed missing key list
and git diffs.
"""
import subprocess
import re
import json
import os
import glob

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

# Read pre-computed missing keys list
with open('tools/all_missing_keys.txt', 'r') as f:
    missing = set(line.strip() for line in f if line.strip())

print(f"Missing keys to find: {len(missing)}")

# Group by prefix
by_prefix = {}
for k in missing:
    prefix = k.split('.')[0]
    by_prefix.setdefault(prefix, []).append(k)
for prefix, keys in sorted(by_prefix.items(), key=lambda x: -len(x[1])):
    print(f"  {prefix}: {len(keys)}")

# Find which files contain missing keys by searching all .cs files
key_to_file = {}
for cs_file in glob.glob('Scripts/**/*.cs', recursive=True):
    try:
        with open(cs_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        continue
    for m in re.finditer(r'Loc\.Get\("([a-z][a-z_0-9]*\.[a-z_0-9]+)"', content):
        key = m.group(1)
        if key in missing and key not in key_to_file:
            key_to_file[key] = cs_file.replace('\\', '/')

files_needed = set(key_to_file.values())
print(f"\nFiles to process: {len(files_needed)}")
for f in sorted(files_needed):
    keys_in_file = [k for k, v in key_to_file.items() if v == f]
    print(f"  {f}: {len(keys_in_file)} missing keys")

colors = {'red', 'green', 'blue', 'yellow', 'cyan', 'white', 'gray', 'bright_red',
          'bright_green', 'bright_yellow', 'bright_cyan', 'bright_white', 'dark_gray',
          'dark_magenta', 'dark_red', 'bright_blue', 'dark_cyan', 'dark_green',
          'ConsoleColor.Yellow', 'ConsoleColor.White', 'ConsoleColor.Red', 'ConsoleColor.Cyan',
          'ConsoleColor.Green', 'ConsoleColor.Gray', 'ConsoleColor.Magenta', 'bright_magenta',
          'dark_yellow'}

all_extracted = {}

for filepath in sorted(files_needed):
    result = subprocess.run(
        ['git', 'diff', '-U0', filepath],
        capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    diff_lines = result.stdout.split('\n')

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
                loc_matches = re.findall(r'Loc\.Get\("([a-z][a-z_0-9]*\.[a-z_0-9]+)"', a_line)
                for key in loc_matches:
                    if key not in missing or key in all_extracted:
                        continue

                    best_original = None
                    # Try same index
                    if a_idx < len(removed):
                        r_line = removed[a_idx]
                        strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                        meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                      and not re.match(r'^[a-z]+\.[a-z_]', s) and s not in ('false', 'true')]
                        if meaningful:
                            best_original = max(meaningful, key=len)

                    # Search all removed
                    if not best_original:
                        for r_line in removed:
                            has_terminal = any(p in a_line for p in ['terminal.Write', 'terminal.SetColor', 'GetInput', 'WriteBoxHeader'])
                            has_r_terminal = any(p in r_line for p in ['terminal.Write', 'terminal.SetColor', 'GetInput', 'WriteBoxHeader'])
                            if has_terminal and has_r_terminal:
                                strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                                meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                              and not re.match(r'^[a-z]+\.[a-z_]', s) and s not in ('false', 'true')]
                                if meaningful:
                                    best_original = max(meaningful, key=len)
                                    break

                    if best_original:
                        counter = [0]
                        def replace_interp(m):
                            r = '{' + str(counter[0]) + '}'
                            counter[0] += 1
                            return r
                        cleaned = re.sub(r'\{[a-zA-Z_][a-zA-Z_0-9.()]*(?:\?[^}]*)?\}', replace_interp, best_original)
                        all_extracted[key] = cleaned
        else:
            i += 1

found = sum(1 for v in all_extracted.values())
still_missing = missing - set(all_extracted.keys())

print(f"\nExtracted from diffs: {found}")
print(f"Not found in diffs: {len(still_missing)}")

# Add all extracted to JSON
for key, value in all_extracted.items():
    en[key] = value
    if key not in es:
        es[key] = value

# For keys not found in diffs, use the key name as placeholder
for key in still_missing:
    en[key] = key
    if key not in es:
        es[key] = key

with open('Localization/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, ensure_ascii=False, indent=2)

print(f"\nAdded {found + len(still_missing)} keys total")
print(f"Final: en={len(en)}, es={len(es)}")

if still_missing:
    print(f"\n{len(still_missing)} keys used raw key as value (not in diff):")
    for k in sorted(still_missing)[:30]:
        print(f"  {k}")
    if len(still_missing) > 30:
        print(f"  ... and {len(still_missing)-30} more")
