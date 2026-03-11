"""
Fix critical localization value bugs found during comprehensive audit.
"""
import json

# Fixes for en.json
en_fixes = {
    # BUG: base.male says "Female" instead of "Male"
    "base.male": "Male",

    # BUG: Leaked C# ternary expression
    "base.stat_in_relationship": "In a relationship ({0} lovers)",

    # BUG: Leaked C# expression {1 + teammates.Count}
    "dungeon.bbs_party_count": " Party({0}): ",

    # BUG: Leaked C# ternary for pluralization
    "dungeon.treasure_potions": "You also find {0} healing potions!",

    # BUG: Leaked C# concatenation " + duelist.Name + "
    "dungeon.duelist_first_1": "\"Well met, {0}! I am a wandering duelist.\"",
    "dungeon.duelist_first_2": "\"They call me {0}. I seek worthy opponents in these depths.\"",
    "dungeon.duelist_first_3": "\"Shall we test our blades?\"",

    # Duelist win/loss dialogues with duplicate placeholder values
    "dungeon.duelist_win1_1": "{0} kneels before you, offering their blade in salute.",
    "dungeon.duelist_win1_2": "\"A worthy victory! I shall remember this.\"",
    "dungeon.duelist_win3_1": "{0} laughs despite the loss!",
    "dungeon.duelist_win3_2": "\"Three times, {0}! You have my respect.\"",
    "dungeon.duelist_win3_3": "\"I'll train harder for our next meeting.\"",
    "dungeon.duelist_win5_1": "{0} bows deeply, a gesture of ultimate respect.",
    "dungeon.duelist_win5_2": "\"You have mastered me. I am honored to be your rival.\"",
    "dungeon.duelist_win_default_1": "{0} accepts defeat gracefully.",
    "dungeon.duelist_win_default_2": "\"Well fought. Until next time.\"",

    # Duelist winning/losing/even dialogue
    "dungeon.duelist_winning_1": "\"Ah, {0}! My rival returns! You've bested me before...\"",
    "dungeon.duelist_winning_2": "\"The score stands {0} to {1} in your favor.\"",
    "dungeon.duelist_winning_3": "\"But today I am stronger! En garde!\"",
    "dungeon.duelist_losing_1": "\"Well, well... {0} returns for another lesson!\"",
    "dungeon.duelist_losing_2": "\"I've defeated you {0} times now. Care to try again?\"",
    "dungeon.duelist_losing_3": "\"Perhaps today your luck changes!\"",
    "dungeon.duelist_even_1": "\"Ah, {0}! Evenly matched as always!\"",
    "dungeon.duelist_even_2": "\"We're tied at {0} victories each.\"",
    "dungeon.duelist_even_3": "\"Time to break the tie!\"",
}

# Fixes for es.json
es_fixes = {
    "base.male": "Masculino",
    "base.stat_in_relationship": "En una relacion ({0} amantes)",
    "dungeon.bbs_party_count": " Grupo({0}): ",
    "dungeon.treasure_potions": "Tambien encuentras {0} pociones de curacion!",
    "dungeon.duelist_first_1": "\"Bien hallado, {0}! Soy un duelista errante.\"",
    "dungeon.duelist_first_2": "\"Me llaman {0}. Busco oponentes dignos en estas profundidades.\"",
    "dungeon.duelist_first_3": "\"Probamos nuestras espadas?\"",
    "dungeon.duelist_win1_1": "{0} se arrodilla ante ti, ofreciendo su espada en saludo.",
    "dungeon.duelist_win1_2": "\"Una victoria digna! Lo recordare.\"",
    "dungeon.duelist_win3_1": "{0} rie a pesar de la derrota!",
    "dungeon.duelist_win3_2": "\"Tres veces, {0}! Tienes mi respeto.\"",
    "dungeon.duelist_win3_3": "\"Entrenare mas duro para nuestro proximo encuentro.\"",
    "dungeon.duelist_win5_1": "{0} se inclina profundamente, un gesto de respeto supremo.",
    "dungeon.duelist_win5_2": "\"Me has dominado. Es un honor ser tu rival.\"",
    "dungeon.duelist_win_default_1": "{0} acepta la derrota con gracia.",
    "dungeon.duelist_win_default_2": "\"Bien luchado. Hasta la proxima.\"",
    "dungeon.duelist_winning_1": "\"Ah, {0}! Mi rival regresa! Me has vencido antes...\"",
    "dungeon.duelist_winning_2": "\"El marcador esta {0} a {1} a tu favor.\"",
    "dungeon.duelist_winning_3": "\"Pero hoy soy mas fuerte! En guardia!\"",
    "dungeon.duelist_losing_1": "\"Vaya, vaya... {0} vuelve por otra leccion!\"",
    "dungeon.duelist_losing_2": "\"Te he derrotado {0} veces. Quieres intentarlo de nuevo?\"",
    "dungeon.duelist_losing_3": "\"Quiza hoy cambie tu suerte!\"",
    "dungeon.duelist_even_1": "\"Ah, {0}! Parejos como siempre!\"",
    "dungeon.duelist_even_2": "\"Estamos empatados con {0} victorias cada uno.\"",
    "dungeon.duelist_even_3": "\"Hora de desempatar!\"",
}

for lang, fixes in [('en', en_fixes), ('es', es_fixes)]:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    added = 0
    for key, value in fixes.items():
        if key in data:
            if data[key] != value:
                data[key] = value
                fixed += 1
        else:
            data[key] = value
            added += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed} values, added {added} new keys")
