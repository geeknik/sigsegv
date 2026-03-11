"""
Extract ALL missing localization keys from git diffs for all modified CS files.
"""
import subprocess
import re
import json
import sys

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

# Find all Loc.Get keys used in code
result = subprocess.run(
    ['grep', '-roE', r'Loc\.Get\("[a-z]+\.[a-z_0-9]+"', 'Scripts/'],
    capture_output=True, text=True, encoding='utf-8', errors='replace'
)

used_keys = set()
for line in result.stdout.strip().split('\n'):
    if not line:
        continue
    m = re.search(r'Loc\.Get\("([a-z][a-z_0-9]*\.[a-z_0-9]+)"', line)
    if m:
        used_keys.add(m.group(1))

en_keys = set(en.keys())
missing = used_keys - en_keys
print(f"Used keys: {len(used_keys)}, Defined: {len(en_keys)}, Missing: {len(missing)}")

if not missing:
    print("No missing keys!")
    sys.exit(0)

# Group missing keys by prefix
by_prefix = {}
for k in missing:
    prefix = k.split('.')[0]
    by_prefix.setdefault(prefix, []).append(k)
for prefix, keys in sorted(by_prefix.items(), key=lambda x: -len(x[1])):
    print(f"  {prefix}: {len(keys)} missing")

# Find which files have these missing keys
key_to_file = {}
for line in result.stdout.strip().split('\n'):
    if not line:
        continue
    m = re.match(r'(.+?):.*Loc\.Get\("([a-z][a-z_0-9]*\.[a-z_0-9]+)"', line)
    if m and m.group(2) in missing:
        key_to_file.setdefault(m.group(2), m.group(1))

files_needed = set(key_to_file.values())
print(f"\nFiles to process: {len(files_needed)}")

colors = {'red', 'green', 'blue', 'yellow', 'cyan', 'white', 'gray', 'bright_red',
          'bright_green', 'bright_yellow', 'bright_cyan', 'bright_white', 'dark_gray',
          'dark_magenta', 'dark_red', 'bright_blue', 'dark_cyan', 'dark_green',
          'ConsoleColor.Yellow', 'ConsoleColor.White', 'ConsoleColor.Red', 'ConsoleColor.Cyan',
          'ConsoleColor.Green', 'ConsoleColor.Gray', 'ConsoleColor.Magenta', 'bright_magenta'}

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
                    # Try same index in removed
                    if a_idx < len(removed):
                        r_line = removed[a_idx]
                        strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                        meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                      and not re.match(r'^[a-z]+\.[a-z_]', s) and s != 'false' and s != 'true']
                        if meaningful:
                            best_original = max(meaningful, key=len)

                    # Try searching all removed lines
                    if not best_original:
                        for r_line in removed:
                            if 'terminal.Write' in a_line and 'terminal.Write' in r_line:
                                strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                                meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                              and not re.match(r'^[a-z]+\.[a-z_]', s) and s != 'false' and s != 'true']
                                if meaningful:
                                    best_original = max(meaningful, key=len)
                                    break
                        # Also try GetInput, WriteBoxHeader patterns
                        if not best_original:
                            for r_line in removed:
                                if ('GetInput' in a_line and 'GetInput' in r_line) or \
                                   ('WriteBoxHeader' in a_line and 'WriteBoxHeader' in r_line) or \
                                   ('Loc.Get' in a_line and 'terminal' in r_line):
                                    strings = re.findall(r'"([^"]*(?:\\.[^"]*)*)"', r_line)
                                    meaningful = [s for s in strings if s and len(s) > 1 and s not in colors
                                                  and not re.match(r'^[a-z]+\.[a-z_]', s) and s != 'false' and s != 'true']
                                    if meaningful:
                                        best_original = max(meaningful, key=len)
                                        break

                    if best_original:
                        # Clean interpolation
                        counter = [0]
                        def replace_interp(m):
                            r = '{' + str(counter[0]) + '}'
                            counter[0] += 1
                            return r
                        cleaned = re.sub(r'\{[a-zA-Z_][a-zA-Z_0-9.()]*(?:\?[^}]*)?\}', replace_interp, best_original)
                        all_extracted[key] = cleaned
                    else:
                        all_extracted[key] = f"TODO:{key}"
        else:
            i += 1

found = sum(1 for v in all_extracted.values() if not v.startswith('TODO:'))
todo = sum(1 for v in all_extracted.values() if v.startswith('TODO:'))
still_missing = missing - set(all_extracted.keys())

print(f"\nExtracted: {found} with values, {todo} need TODO")
print(f"Not in any diff: {len(still_missing)}")

# Add to JSON files
added = 0
for key, value in sorted(all_extracted.items()):
    if not value.startswith('TODO:'):
        en[key] = value
        if key not in es:
            es[key] = value  # English fallback
        added += 1

# For still_missing keys, add placeholder
for key in still_missing:
    en[key] = key  # Use key as value (will show raw key)
    if key not in es:
        es[key] = key
    added += 1

with open('Localization/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, ensure_ascii=False, indent=2)

print(f"\nAdded {added} keys total")
print(f"Final: en={len(en)}, es={len(es)}")

# Show TODO keys
if todo > 0:
    print(f"\n{todo} keys need manual review (using key as value):")
    for k, v in sorted(all_extracted.items()):
        if v.startswith('TODO:'):
            print(f"  {k}")

if still_missing:
    print(f"\n{len(still_missing)} keys not found in diffs (using key as placeholder):")
    for k in sorted(still_missing)[:20]:
        print(f"  {k}")
    if len(still_missing) > 20:
        print(f"  ... and {len(still_missing)-20} more")
