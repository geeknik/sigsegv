"""
Fix issues found in seventh localization audit pass:
1. BUG: dungeon.god_intro_veloura_5 = "magenta" (color name, not text)
2. BUG: dungeon.god_intro_manwe_5 = key name itself
3. Missing apostrophes (3 keys)
"""
import json

en_fixes = {
    # Color name leaked as display text — should be dialogue like other gods' _5 keys
    "dungeon.god_intro_veloura_5": "The Goddess of Love weeps:",

    # Key name as value (placeholder never filled in)
    "dungeon.god_intro_manwe_5": "The Creator speaks:",

    # Missing apostrophes
    "ending.quote_secret": "\"I'm done. And that's ok.\"",
    "street.challenge_phrase_5": "My sword needs blood. You'll do.",
    "street.throne_quote": "  \"Your time's up. I'm taking that throne.\"",
}

es_fixes = {
    "dungeon.god_intro_veloura_5": "La Diosa del Amor llora:",
    "dungeon.god_intro_manwe_5": "El Creador habla:",
    "ending.quote_secret": "\"Ya termine. Y eso esta bien.\"",
    "street.challenge_phrase_5": "Mi espada necesita sangre. Tu serviras.",
    "street.throne_quote": "  \"Se te acabo el tiempo. Voy a tomar ese trono.\"",
}

for lang, fixes in [('en', en_fixes), ('es', es_fixes)]:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    for key, value in fixes.items():
        if key in data and data[key] != value:
            data[key] = value
            fixed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed} values")
