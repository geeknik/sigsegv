"""
Remove orphaned keys from es.json that have no matching key in en.json.
These are Spanish translations that were added without an English counterpart.
"""
import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es_data = json.load(f)

# Find orphaned keys (in es but not en), excluding comment keys
orphaned = []
for key in es_data:
    if key.startswith('_') or key.startswith('//'):
        continue
    if key not in en_data:
        orphaned.append(key)

print(f"Found {len(orphaned)} orphaned keys in es.json:")
for key in sorted(orphaned):
    print(f"  {key}: {es_data[key][:60]}...")

# Remove them
for key in orphaned:
    del es_data[key]

with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es_data, f, ensure_ascii=False, indent=2)

print(f"\nRemoved {len(orphaned)} orphaned keys from es.json")
