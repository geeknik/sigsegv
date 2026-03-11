#!/usr/bin/env python3
"""Add ArenaLocation localization keys to en.json and es.json."""
import json, os

LOC_DIR = os.path.join(os.path.dirname(__file__), '..', 'Localization')

NEW_KEYS = {
    "arena.lb_wl_format": "{0}W/{1}L",
    "arena.notify_attack_won": "[Arena] {0} attacked you in the Arena and won! They stole {1} of your gold.",
    "arena.notify_attack_lost": "[Arena] {0} attacked you in the Arena but your shadow defeated them! You gained {1} gold.",
}

NEW_KEYS_ES = {
    "arena.lb_wl_format": "{0}V/{1}D",
    "arena.notify_attack_won": "[Arena] ¡{0} te atacó en la Arena y ganó! Robaron {1} de tu oro.",
    "arena.notify_attack_lost": "[Arena] ¡{0} te atacó en la Arena pero tu sombra los derrotó! Ganaste {1} de oro.",
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
