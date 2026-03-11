#!/usr/bin/env python3
"""Add CharacterCreationSystem localization keys to en.json and es.json."""
import json, sys, os

LOC_DIR = os.path.join(os.path.dirname(__file__), '..', 'Localization')

NEW_KEYS = {
    "charcreate.prestige_req_savior": "Savior ending",
    "charcreate.prestige_req_defiant": "Defiant ending",
    "charcreate.prestige_req_usurper": "Usurper ending",
    "charcreate.abort": "Abort",
    "charcreate.mana_per_level_label": "+{0}/level",
}

NEW_KEYS_ES = {
    "charcreate.prestige_req_savior": "Final Salvador",
    "charcreate.prestige_req_defiant": "Final Desafiante",
    "charcreate.prestige_req_usurper": "Final Usurpador",
    "charcreate.abort": "Cancelar",
    "charcreate.mana_per_level_label": "+{0}/nivel",
}

def add_keys(filepath, new_keys):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    added = 0
    for key, value in new_keys.items():
        if key not in data:
            data[key] = value
            added += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return added

en_path = os.path.join(LOC_DIR, 'en.json')
es_path = os.path.join(LOC_DIR, 'es.json')
en_added = add_keys(en_path, NEW_KEYS)
es_added = add_keys(es_path, NEW_KEYS_ES)
print(f"en.json: added {en_added} keys")
print(f"es.json: added {es_added} keys")
