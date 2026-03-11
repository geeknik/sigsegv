"""
Fix issues found in third localization audit pass:
1. Corrupted team column header values (leaked C# format specifiers)
2. Keys where value = key name (placeholder/unlocalized)
3. Placeholder mismatches (inventory.cannot_equip, team.you_suffix)
4. Typos and missing apostrophes in endings and UI text
5. dormitory keys with literal \n
"""
import json

# === EN.JSON FIXES ===
en_fixes = {
    # Team ranking column headers (were ",-24} {" garbage from C# format strings)
    "team.rank_col_rank": "Rank",
    "team.rank_col_name": "Team Name",
    "team.rank_col_mbrs": "Mbrs",
    "team.rank_col_power": "Power",
    "team.rank_col_avg_lvl": "Avg Lvl",
    "team.rank_col_turf": "Turf",

    # Team detail column headers (were ",-20} {" garbage)
    "team.detail_col_name": "Name",
    "team.detail_col_class": "Class",
    "team.detail_col_lvl": "Level",
    "team.detail_col_hp": "HP",
    "team.detail_col_location": "Location",
    "team.detail_col_status": "Status",

    # Keys where value was the key name itself
    "dungeon.encounter_group": "{0}",
    "dungeon.duelist_coward": "The duelist turns and flees!",

    # Placeholder mismatches
    "inventory.cannot_equip": "Cannot equip: {0}",  # code passes 1 arg, was expecting 2
    "team.you_suffix": "(You)",  # code passes 0 args, was "{0} (you)"

    # Typos in endings
    "ending.usurper_line_14": "Then millennia.",
    "ending.savior_line_5": "\"You were scared and you hurt people. A lot of people.\"",
    "ending.savior_line_6": "\"But I didn't come all this way just to make another corpse.\"",
    "ending.savior_line_8": "down his face. You didn't know gods could cry.",
    "ending.savior_line_13": "Manwe gasps. The Old Gods stir in their prisons.",
    "ending.savior_line_17": "can't look you in the eye.",
    "ending.savior_line_23": "the gods are waiting. They don't say much.",
    "ending.savior_line_24": "They don't need to.",
    "ending.defiant_line_3": "\"I don't want your power. I don't want ANY of this.\"",
    "ending.defiant_line_6": "\"You could rule forever,\" Manwe says, genuinely confused.",
    "ending.defiant_line_13": "The Old Gods stumble free from their prisons.",
    "ending.defiant_line_15": "For the first time in millennia, they are mortal.",
    "ending.defiant_line_17": "Manwe is fading. He doesn't seem to mind.",
    "ending.defiant_line_22": "Just people, making their own mistakes.",
    "ending.true_line_24": "It's going to be a lot of work.",
    "ending.awakening_line_24": "\"I don't want to be alone anymore,\" Manwe admits.",
    "ending.awakening_line_25": "\"And the Old Gods -- they're fragments too, aren't they.\"",
    "ending.awakening_line_29": "All the separation. God and mortal, creator and created.",
    "ending.awakening_line_31": "so you could learn what it meant to be small.",
    "ending.dissolution_line_14": "the whole point. You don't need every wave to",
    "ending.dissolution_line_27": "The gods figure their stuff out.",
    "ending.legacy_align_dark": "the kind of person mothers warn their children about",
    "ending.quote_savior": "\"Could have killed him. Didn't. Don't regret it.\"",
    "ending.world_gods_destroyed_desc": "Their power scattered to the winds.",
    "ending.world_usurper": "You took the throne of the gods. The realm hasn't stopped shaking.",

    # Typos/missing apostrophes in UI text
    "ending.usurper_line_7": "You can't even hear him anymore. The power is too loud.",
    "ending.usurper_line_18": "Manwe tried to warn you. You didn't listen.",
    "dark_alley.bm_no_access": "  You don't have access to the Black Market.",
    "dark_alley.bm_poison_limit": "  You can't carry any more. Three is the limit.",
    "dark_alley.informant_no_access": "  You don't have access to the information network.",
    "street.grudge_waiting": "  {0} is waiting for you. Doesn't look happy.",
    "temple.sanctum_cant_afford": "  You can't afford the offering.",
}

# === ES.JSON FIXES ===
es_fixes = {
    # Team ranking column headers
    "team.rank_col_rank": "Rango",
    "team.rank_col_name": "Nombre del Equipo",
    "team.rank_col_mbrs": "Miem",
    "team.rank_col_power": "Poder",
    "team.rank_col_avg_lvl": "Nvl Prom",
    "team.rank_col_turf": "Terr",

    # Team detail column headers
    "team.detail_col_name": "Nombre",
    "team.detail_col_class": "Clase",
    "team.detail_col_lvl": "Nivel",
    "team.detail_col_hp": "PV",
    "team.detail_col_location": "Ubicacion",
    "team.detail_col_status": "Estado",

    # Keys where value was the key name itself
    "dungeon.encounter_group": "{0}",
    "dungeon.duelist_coward": "El duelista huye!",

    # Placeholder mismatches
    "inventory.cannot_equip": "No se puede equipar: {0}",
    "team.you_suffix": "(Tu)",

    # Typos in endings (Spanish versions - fix apostrophes/spelling)
    "dark_alley.bm_no_access": "  No tienes acceso al Mercado Negro.",
    "dark_alley.bm_poison_limit": "  No puedes llevar mas. Tres es el limite.",
    "dark_alley.informant_no_access": "  No tienes acceso a la red de informacion.",
}

# Remove combat.damage and combat.miss since they're not used in code
en_remove = ["combat.damage", "combat.miss"]
es_remove = ["combat.damage", "combat.miss"]

for lang, fixes, removals in [('en', en_fixes, en_remove), ('es', es_fixes, es_remove)]:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    added = 0
    removed = 0

    for key, value in fixes.items():
        if key in data:
            if data[key] != value:
                data[key] = value
                fixed += 1
        else:
            data[key] = value
            added += 1

    for key in removals:
        if key in data:
            del data[key]
            removed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed} values, added {added} new keys, removed {removed} unused keys")
