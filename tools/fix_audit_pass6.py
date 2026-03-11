"""
Fix issues found in sixth localization audit pass:
1. BUG: base.rel_in_love = "bright_magenta" (color name, not display text)
2. BUG: 8 missing street_encounter.romance.admirer_* keys (code uses different names than JSON)
3. Missing apostrophes in 4 keys
4. Remove 16 leaked comment-as-key entries
"""
import json

# === EN FIXES ===
en_fixes = {
    # BUG: Value is a color name, not the relationship label
    "base.rel_in_love": "In Love",

    # Missing apostrophes
    "companion.gone": "  That's it. They're gone.",
    "ending.dissolution_not_ready_1": "Not ready yet, huh? That's fine.",
    "street.challenge_phrase_2": "I've heard about you. Fight me!",
    "street.guard_darkness_note": "  (They're looking for you — Darkness: {0})",
}

# Missing admirer keys — code uses street_encounter.romance.admirer_* but JSON has street.admirer_*
# Add the keys the code actually references, using values from the existing street.admirer_* keys
en_new = {
    "street_encounter.romance.admirer_maiden": "Lovely maiden",
    "street_encounter.romance.admirer_beautiful": "Beautiful stranger",
    "street_encounter.romance.admirer_mysterious_w": "Mysterious woman",
    "street_encounter.romance.admirer_charming_w": "Charming lady",
    "street_encounter.romance.admirer_handsome": "Handsome stranger",
    "street_encounter.romance.admirer_dashing": "Dashing rogue",
    "street_encounter.romance.admirer_mysterious_m": "Mysterious man",
    "street_encounter.romance.admirer_charming_m": "Charming gentleman",
}

# === ES FIXES ===
es_fixes = {
    # BUG: Same color name leak
    "base.rel_in_love": "Enamorado",

    # Mirror apostrophe fixes (Spanish doesn't use apostrophes but fix the translations)
    "companion.gone": "  Eso es todo. Se fueron.",
    "ending.dissolution_not_ready_1": "Aun no estas listo, eh? Esta bien.",
    "street.challenge_phrase_2": "He oido de ti. Pelea conmigo!",
    "street.guard_darkness_note": "  (Te estan buscando — Oscuridad: {0})",
}

es_new = {
    "street_encounter.romance.admirer_maiden": "Bella doncella",
    "street_encounter.romance.admirer_beautiful": "Hermosa desconocida",
    "street_encounter.romance.admirer_mysterious_w": "Mujer misteriosa",
    "street_encounter.romance.admirer_charming_w": "Dama encantadora",
    "street_encounter.romance.admirer_handsome": "Apuesto desconocido",
    "street_encounter.romance.admirer_dashing": "Picaro audaz",
    "street_encounter.romance.admirer_mysterious_m": "Hombre misterioso",
    "street_encounter.romance.admirer_charming_m": "Caballero encantador",
}

# Comment keys to remove (leaked as JSON entries with empty values)
comment_keys_to_remove = [
    "// Dialogue System - UI",
    "// Magic Shop - Accessory Shop",
    "// Magic Shop - BBS Menu",
    "// Magic Shop - Curse Removal",
    "// Magic Shop - Dark Arts",
    "// Magic Shop - Disease Cures",
    "// Magic Shop - Equipment Enchanting",
    "// Magic Shop - Healing Potions",
    "// Magic Shop - Identify",
    "// Magic Shop - Love Spells",
    "// Magic Shop - Mana Potions",
    "// Magic Shop - Old Enchant Method",
    "// Magic Shop - Price Modifiers",
    "// Magic Shop - Scrying",
    "// Magic Shop - Talk to Owner",
    "// Magic Shop - Visual Menu",
]

for lang in ['en', 'es']:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixes = en_fixes if lang == 'en' else es_fixes
    new_keys = en_new if lang == 'en' else es_new

    fixed = 0
    added = 0
    removed = 0

    # Apply value fixes
    for key, value in fixes.items():
        if key in data:
            if data[key] != value:
                data[key] = value
                fixed += 1

    # Add missing keys
    for key, value in new_keys.items():
        if key not in data:
            data[key] = value
            added += 1

    # Remove leaked comment keys
    for key in comment_keys_to_remove:
        if key in data:
            del data[key]
            removed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed}, added {added}, removed {removed}")
