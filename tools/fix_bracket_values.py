"""
Fix localization values that start with ']' — these are menu items where the code
already renders the closing bracket, but the extraction captured it as part of the value.
"""
import json

for lang in ['en', 'es']:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    for key, value in list(data.items()):
        if isinstance(value, str) and value.startswith(']'):
            data[key] = value[1:]
            fixed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: stripped leading ] from {fixed} values")
