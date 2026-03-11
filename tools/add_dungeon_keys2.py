#!/usr/bin/env python3
"""Add missing dungeon localization keys to en.json and es.json."""

import json
import sys
import os

LOC_DIR = os.path.join(os.path.dirname(__file__), '..', 'Localization')

new_keys = {
    # Wounded adventurer - gain knowledge
    "dungeon.rival_fight_prompt": {
        "en": "(F)ight, (N)egotiate, or (L)eave? ",
        "es": "(L)uchar, (N)egociar, o (D)ejar? "
    },
    # Riddle encounter headers
    "dungeon.riddle_header": {
        "en": "*** RIDDLE GATE ***",
        "es": "*** PUERTA DEL ACERTIJO ***"
    },
    # Puzzle encounter headers
    "dungeon.puzzle_header": {
        "en": "*** ANCIENT PUZZLE ***",
        "es": "*** ANTIGUO ROMPECABEZAS ***"
    },
    "dungeon.puzzle_solved_header": {
        "en": "*** PUZZLE SOLVED! ***",
        "es": "*** ROMPECABEZAS RESUELTO! ***"
    },
    # Mystery event header
    "dungeon.mystery_header": {
        "en": "*** MYSTERIOUS OCCURRENCE ***",
        "es": "*** SUCESO MISTERIOSO ***"
    },
    "dungeon.mystery_xp_plus": {
        "en": "+{0} experience!",
        "es": "+{0} experiencia!"
    },
    # Riddle gate headers
    "dungeon.riddle_gate_header": {
        "en": "THE RIDDLE GATE",
        "es": "LA PUERTA DEL ACERTIJO"
    },
    "dungeon.riddle_solved_header": {
        "en": "RIDDLE SOLVED",
        "es": "ACERTIJO RESUELTO"
    },
    "dungeon.riddle_failed_header": {
        "en": "RIDDLE FAILED",
        "es": "ACERTIJO FALLIDO"
    },
    "dungeon.riddle_foolish_mortal": {
        "en": "'Foolish mortal. There is a price for failure.'",
        "es": "'Mortal insensato. La derrota tiene un precio.'"
    },
    # Lore library header
    "dungeon.lore_library_header": {
        "en": "ANCIENT LORE LIBRARY",
        "es": "BIBLIOTECA DE CONOCIMIENTO ANTIGUO"
    },
    "dungeon.lore_library_always_did": {
        "en": "...or perhaps it always did.",
        "es": "...o tal vez siempre fue as\u00ed."
    },
    # Memory chamber header
    "dungeon.memory_chamber_header": {
        "en": "MEMORY CHAMBER",
        "es": "C\u00c1MARA DE RECUERDOS"
    },
    # Secret boss / hidden chamber
    "dungeon.hidden_chamber_header": {
        "en": "HIDDEN CHAMBER",
        "es": "C\u00c1MARA OCULTA"
    },
    # Memory puzzle header
    "dungeon.memory_puzzle_header": {
        "en": "*** MEMORY PUZZLE ***",
        "es": "*** ROMPECABEZAS DE MEMORIA ***"
    },
    # Beggar header
    "dungeon.beggar_header": {
        "en": "\u2602 BEGGAR ENCOUNTER \u2602",
        "es": "\u2602 ENCUENTRO CON MENDIGO \u2602"
    },
    # Beggar menu labels
    "dungeon.beggar_give_label": {
        "en": "  (G) Give gold          (+Chivalry)",
        "es": "  (G) Dar oro             (+Caballer\u00eda)"
    },
    "dungeon.beggar_rob_label": {
        "en": "  (R) Rob the beggar     (+Darkness)",
        "es": "  (R) Robar al mendigo   (+Oscuridad)"
    },
    "dungeon.beggar_ignore_label": {
        "en": "  (I) Ignore and move on",
        "es": "  (I) Ignorar y seguir"
    },
    "dungeon.beggar_chivalry": {
        "en": "+5 Chivalry",
        "es": "+5 Caballer\u00eda"
    },
    "dungeon.beggar_darkness": {
        "en": "+10 Darkness",
        "es": "+10 Oscuridad"
    },
    # Seal discovery
    "dungeon.seal_ancient_power": {
        "en": "       As you explore the room, an ancient power stirs...",
        "es": "       Al explorar la sala, un poder antiguo se agita..."
    },
    "dungeon.seal_stone_tablet": {
        "en": "  Hidden beneath the dust of ages, you find a stone tablet.",
        "es": "  Oculta bajo el polvo de los siglos, encuentras una tablilla de piedra."
    },
    "dungeon.seal_divine_energy": {
        "en": "  It pulses with divine energy, warm to the touch.",
        "es": "  Pulsa con energ\u00eda divina, c\u00e1lida al tacto."
    },
    "dungeon.seal_seven_seals": {
        "en": "  This is one of the Seven Seals - the truth of the Old Gods.",
        "es": "  Este es uno de los Siete Sellos - la verdad de los Dioses Antiguos."
    },
    "dungeon.seal_press_enter": {
        "en": "  Press Enter to continue...",
        "es": "  Presiona Enter para continuar..."
    },
    # Artifact drop
    "dungeon.artifact_header": {
        "en": "      A DIVINE ARTIFACT PULSES WITH POWER!",
        "es": "      \u00a1UN ARTEFACTO DIVINO PULSA CON PODER!"
    },
    # Wave fragment collected
    "dungeon.wave_fragment_collected": {
        "en": "(Wave Fragment collected: {0})",
        "es": "(Fragmento de Ola recolectado: {0})"
    },
}

def add_keys():
    en_path = os.path.join(LOC_DIR, 'en.json')
    es_path = os.path.join(LOC_DIR, 'es.json')

    with open(en_path, 'r', encoding='utf-8') as f:
        en_data = json.load(f)
    with open(es_path, 'r', encoding='utf-8') as f:
        es_data = json.load(f)

    en_added = 0
    es_added = 0

    for key, vals in new_keys.items():
        if key not in en_data:
            en_data[key] = vals["en"]
            en_added += 1
        if key not in es_data:
            es_data[key] = vals["es"]
            es_added += 1

    with open(en_path, 'w', encoding='utf-8') as f:
        json.dump(en_data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    with open(es_path, 'w', encoding='utf-8') as f:
        json.dump(es_data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"Added {en_added} en keys, {es_added} es keys. en: {len(en_data)}, es: {len(es_data)}")

if __name__ == '__main__':
    add_keys()
