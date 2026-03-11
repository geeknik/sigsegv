#!/usr/bin/env python3
"""Add AnchorRoadLocation localization keys to en.json and es.json."""
import json, os

LOC_DIR = os.path.join(os.path.dirname(__file__), '..', 'Localization')

NEW_KEYS = {
    "anchor_road.bbs_bounty": "Bounty",
    "anchor_road.bbs_gang_war": "GangWar",
    "anchor_road.bbs_gauntlet": "Gauntlet",
    "anchor_road.bbs_claim_town": "ClaimTown",
    "anchor_road.bbs_flee_town": "FleeTown",
    "anchor_road.bbs_prison": "Prison",
    "anchor_road.bbs_return": "Return",
    "anchor_road.gold_amount": "{0} gold",
}

NEW_KEYS_ES = {
    "anchor_road.bbs_bounty": "Recompensa",
    "anchor_road.bbs_gang_war": "GuerraBandas",
    "anchor_road.bbs_gauntlet": "Desafío",
    "anchor_road.bbs_claim_town": "ReclamarCiudad",
    "anchor_road.bbs_flee_town": "HuirCiudad",
    "anchor_road.bbs_prison": "Prisión",
    "anchor_road.bbs_return": "Volver",
    "anchor_road.gold_amount": "{0} oro",
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
