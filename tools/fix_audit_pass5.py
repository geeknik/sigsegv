"""
Fix issues found in fifth localization audit pass:
1. Stray leading quotes on 3 dialogue keys (healer, love_street)
2. Literal \\n in 4 duel/attack keys (code already prepends \\n)
3. Missing apostrophe in ending.dissolution_line_13
4. Truncated ES translations (7 keys)
5. Unicode replacement char in dungeon.merchant_antidote_cure
"""
import json

# === EN FIXES ===
en_fixes = {
    # Stray leading quote — these are "NPC does action. "NPC says thing.""
    # The leading " before {0} is wrong — it's not dialogue, it's narration
    "healer.stay_clean": "{0} smiles warmly. \"Stay clean, my friend.\"",
    "love_street.shrug_loss": "{0} shrugs. \"Your loss, honey.\"",
    "love_street.gigolo_bow": "{0} bows politely. \"Perhaps another time.\"",

    # Literal \n — code already prepends "\n  " so these create doubled newlines
    # Remove the leading \n and extra spaces, keep just the message text
    "base.duel_victory": "You defeated {0} in honorable combat!",
    "base.duel_defeat": "{0} got the better of you...",
    "base.attack_killed": "{0} falls to the ground, lifeless.",
    "base.attack_overpowered": "{0} overpowered you...",

    # Missing apostrophe
    "ending.dissolution_line_13": "\"It'll keep going fine without me. That's kind of",

    # Unicode replacement char (ensure em dash is clean)
    "dungeon.merchant_antidote_cure": "You drink the antidote -- the poison drains from your body!",
}

# === ES FIXES ===
es_fixes = {
    # Mirror the stray quote fixes
    "healer.stay_clean": "{0} sonrie calidamente. \"Mantente limpio, amigo.\"",
    "love_street.shrug_loss": "{0} se encoge de hombros. \"Tu te lo pierdes, cariño.\"",
    "love_street.gigolo_bow": "{0} hace una reverencia. \"Quiza en otra ocasion.\"",

    # Literal \n fixes
    "base.duel_victory": "Derrotaste a {0} en combate honorable!",
    "base.duel_defeat": "{0} te supero...",
    "base.attack_killed": "{0} cae al suelo, sin vida.",
    "base.attack_overpowered": "{0} te derroto...",

    # Truncated Spanish translations — expand to match English meaning
    "main_street.combat_test_victory": "El rufian huye entre las sombras!",
    "main_street.combat_test_escaped": "Te escabulles del peligroso encuentro.",
    "main_street.combat_test_avoided": "Sabiamente evitas la confrontacion.",
    "main_street.cycle_desc_realtime": "Tiempo Real 24 Horas (se reinicia a medianoche)",
    "main_street.cycle_desc_session": "Por Sesion (se reinicia cuando se agotan los turnos)",
    "main_street.story_align_usurper": "Usurpador - Encarnacion de la Oscuridad",
    "main_street.story_awakening_0": "No Despierto - Solo ves la superficie de las cosas",

    # Unicode replacement char fix
    "dungeon.merchant_antidote_cure": "Bebes el antidoto -- el veneno se drena de tu cuerpo!",

    # Mirror apostrophe fix
    "ending.dissolution_line_13": "\"Seguira bien sin mi. Eso es algo asi como",
}

# Apply fixes
for lang, fixes in [('en', en_fixes), ('es', es_fixes)]:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    for key, value in fixes.items():
        if key in data:
            if data[key] != value:
                data[key] = value
                fixed += 1
        else:
            data[key] = value
            fixed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed} values")
