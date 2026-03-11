"""
Fix issues found in eighth localization audit pass:
1. 16 placeholder keys (value = key name) — fill with correct text from git history
2. God intro duplicate dialogue lines — make _4 and _5 unique spoken dialogue
3. Remove orphaned menu.dungeon key
"""
import json

en_fixes = {
    # === PLACEHOLDER KEYS (value was key name) — restored from original code ===

    # Story sequences
    "dungeon.story_whispers_3": "Why do you descend, wave?",
    "dungeon.story_whispers_4": "What do you seek in the deep?",
    "dungeon.story_oracle_7": "The Seal of Fate reveals what I could not speak.",

    # Manwe intro
    "dungeon.god_intro_manwe_4": "You have come at last, my wayward child.",
    "dungeon.god_intro_manwe_6": "I AM the beginning. And perhaps... the end.",

    # Town reactions — Maelketh
    "dungeon.react_maelketh_def_agg_2": "\"Killed a god of war with pure rage. What does that make them?\"",
    "dungeon.react_maelketh_def_hum_2": "\"They say you bowed before the god of war... and still won.\"",
    "dungeon.react_maelketh_sav_2": "\"Maelketh remembers honor. The endless wars can finally end.\"",
    "dungeon.react_maelketh_other_2": "\"They faced the god of war and walked away. On their own terms.\"",

    # Town reactions — Veloura
    "dungeon.react_veloura_def_agg_2": "\"They killed the goddess of love. What happens to us now?\"",

    # Town reactions — Thorgrim
    "dungeon.react_thorgrim_def_defy_3": "\"If they can defy the god of law... what stops them defying ours?\"",
    "dungeon.react_thorgrim_def_hon_2": "\"Justice was served today, by one who understands it.\"",
    "dungeon.react_thorgrim_sav_2": "\"Thorgrim's law is restored. The courts will remember this day.\"",
    "dungeon.react_thorgrim_other_2": "\"Fair dealings with the god of law. That takes backbone.\"",

    # Town reactions — Aurelion
    "dungeon.react_aurelion_def_def_2": "\"The god of light... gone. Who will guide us through the darkness?\"",

    # Town reactions — Terravok
    "dungeon.react_terravok_def_resp_2": "\"What it cost to break the unbreakable... only the mountain knows.\"",

    # === GOD INTRO DUPLICATES — make _4/_5 actual spoken dialogue ===
    # Pattern: _3 = attribution, _4 = first dialogue (bright), _5 = second dialogue (dim)

    # Maelketh — God of War
    # _3 stays "The God of War speaks:" (attribution)
    "dungeon.god_intro_maelketh_4": "\"Another warrior seeks glory in my domain.\"",

    # Veloura — Goddess of Love (all 3 were identical attribution)
    # _3 stays as attribution
    "dungeon.god_intro_veloura_4": "\"Love is the cruelest wound of all... and the deepest.\"",
    "dungeon.god_intro_veloura_5": "\"Will you heal what is broken, or shatter it further?\"",

    # Thorgrim — God of Law
    "dungeon.god_intro_thorgrim_4": "\"You stand before the court of eternity. How do you plead?\"",
    "dungeon.god_intro_thorgrim_5": "\"Every soul must answer for what they have done.\"",

    # Noctura — Goddess of Shadows
    "dungeon.god_intro_noctura_4": "\"The darkness remembers every secret you have buried.\"",
    "dungeon.god_intro_noctura_5": "\"Come... let me show you what hides in your own shadow.\"",

    # Aurelion — God of Light
    "dungeon.god_intro_aurelion_4": "\"My light fades... but even a dying star can burn.\"",
    "dungeon.god_intro_aurelion_5": "\"Will you carry this flame, or let it go out forever?\"",

    # Terravok — God of Earth
    "dungeon.god_intro_terravok_4": "\"Mountains do not bow. Neither shall I.\"",
}

es_fixes = {
    # Story sequences
    "dungeon.story_whispers_3": "Por que desciendes, ola?",
    "dungeon.story_whispers_4": "Que buscas en las profundidades?",
    "dungeon.story_oracle_7": "El Sello del Destino revela lo que no pude decir.",

    # Manwe intro
    "dungeon.god_intro_manwe_4": "Al fin has llegado, hijo prodigo.",
    "dungeon.god_intro_manwe_6": "YO SOY el principio. Y quiza... el final.",

    # Town reactions — Maelketh
    "dungeon.react_maelketh_def_agg_2": "\"Mato a un dios de la guerra con pura furia. Que los convierte eso?\"",
    "dungeon.react_maelketh_def_hum_2": "\"Dicen que te inclinaste ante el dios de la guerra... y aun asi ganaste.\"",
    "dungeon.react_maelketh_sav_2": "\"Maelketh recuerda el honor. Las guerras interminables al fin pueden terminar.\"",
    "dungeon.react_maelketh_other_2": "\"Enfrentaron al dios de la guerra y se fueron. En sus propios terminos.\"",

    # Town reactions — Veloura
    "dungeon.react_veloura_def_agg_2": "\"Mataron a la diosa del amor. Que nos pasara ahora?\"",

    # Town reactions — Thorgrim
    "dungeon.react_thorgrim_def_defy_3": "\"Si pueden desafiar al dios de la ley... que les impide desafiar la nuestra?\"",
    "dungeon.react_thorgrim_def_hon_2": "\"Se hizo justicia hoy, por alguien que la entiende.\"",
    "dungeon.react_thorgrim_sav_2": "\"La ley de Thorgrim fue restaurada. Los tribunales recordaran este dia.\"",
    "dungeon.react_thorgrim_other_2": "\"Trato justo con el dios de la ley. Eso requiere agallas.\"",

    # Town reactions — Aurelion
    "dungeon.react_aurelion_def_def_2": "\"El dios de la luz... se fue. Quien nos guiara en la oscuridad?\"",

    # Town reactions — Terravok
    "dungeon.react_terravok_def_resp_2": "\"Lo que costo romper lo irrompible... solo la montana lo sabe.\"",

    # God intro dialogue
    "dungeon.god_intro_maelketh_4": "\"Otro guerrero busca gloria en mi dominio.\"",

    "dungeon.god_intro_veloura_4": "\"El amor es la herida mas cruel de todas... y la mas profunda.\"",
    "dungeon.god_intro_veloura_5": "\"Sanaras lo que esta roto, o lo destrozaras mas?\"",

    "dungeon.god_intro_thorgrim_4": "\"Estas ante el tribunal de la eternidad. Como te declaras?\"",
    "dungeon.god_intro_thorgrim_5": "\"Toda alma debe responder por lo que ha hecho.\"",

    "dungeon.god_intro_noctura_4": "\"La oscuridad recuerda cada secreto que has enterrado.\"",
    "dungeon.god_intro_noctura_5": "\"Ven... dejame mostrarte lo que se oculta en tu propia sombra.\"",

    "dungeon.god_intro_aurelion_4": "\"Mi luz se desvanece... pero incluso una estrella moribunda puede arder.\"",
    "dungeon.god_intro_aurelion_5": "\"Llevaras esta llama, o dejaras que se apague para siempre?\"",

    "dungeon.god_intro_terravok_4": "\"Las montanas no se inclinan. Yo tampoco.\"",
}

# Remove orphaned menu.dungeon (only in a code comment, real key is menu.action.dungeon)
remove_keys = ["menu.dungeon"]

for lang in ['en', 'es']:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixes = en_fixes if lang == 'en' else es_fixes
    fixed = 0
    removed = 0

    for key, value in fixes.items():
        if key in data:
            if data[key] != value:
                data[key] = value
                fixed += 1
        else:
            data[key] = value
            fixed += 1

    for key in remove_keys:
        if key in data:
            del data[key]
            removed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed}, removed {removed}")
