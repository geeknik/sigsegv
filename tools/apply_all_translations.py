"""
Apply all Spanish translations from the 5 batch translation files.
Imports each batch's translations dict and applies to es.json.
"""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'translate_batches'))

from dungeon_es import translations as dungeon_tr
from base_es import translations as base_tr
from castle_inn_inv_es import translations as castle_inn_inv_tr
from narrative_es import translations as narrative_tr
from small_es import translations as small_tr

# Combine all translations
all_translations = {}
for name, tr in [('dungeon', dungeon_tr), ('base', base_tr), ('castle_inn_inv', castle_inn_inv_tr),
                  ('narrative', narrative_tr), ('small', small_tr)]:
    print(f"  {name}: {len(tr)} keys")
    all_translations.update(tr)

print(f"\nTotal translations to apply: {len(all_translations)}")

# Load es.json
path = 'Localization/es.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply translations (only update if key exists and value is different)
updated = 0
added = 0
skipped = 0
for key, value in all_translations.items():
    if key in data:
        if data[key] != value:
            data[key] = value
            updated += 1
        else:
            skipped += 1
    else:
        # Key doesn't exist in es.json — skip (shouldn't happen)
        print(f"  WARNING: key not in es.json: {key}")
        added += 1

# Write back
with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nes.json: updated {updated}, skipped {skipped} (already correct), warnings {added}")
