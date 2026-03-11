"""
Add all missing localization keys found during the comprehensive audit.
Covers inn.bandit.*, main_street.*, and magic_shop.* categories.
"""
import json

# === INN BANDIT (Aldric recruitment scene) ===
inn_bandit_en = {
    "inn.bandit.sitting_at_bar": "You're sitting at the bar, nursing a drink after a long day.",
    "inn.bandit.bandits_enter": "The door crashes open as a group of armed bandits swagger in.",
    "inn.bandit.leader_threat1": "\"Everyone stay where you are! Hand over your gold,\"",
    "inn.bandit.leader_threat2": "\"or we'll paint these walls with your blood!\"",
    "inn.bandit.draw_weapons": "The bandits draw their weapons, steel glinting in the firelight.",
    "inn.bandit.patrons_scatter": "Patrons scramble for cover, knocking over chairs and mugs.",
    "inn.bandit.chair_scrapes": "*A chair scrapes against the floor...*",
    "inn.bandit.stranger_rises": "A stranger rises slowly from a corner table.",
    "inn.bandit.tattered_armor": "He wears tattered but well-maintained armor,",
    "inn.bandit.battered_shield": "and carries a battered shield that has clearly seen many battles.",
    "inn.bandit.aldric_sporting": "\"Now this doesn't seem very sporting, does it?\"",
    "inn.bandit.leader_stay_out": "\"Stay out of this, old man, unless you want to die!\"",
    "inn.bandit.aldric_i_am_trouble": "\"I AM the trouble you don't want to find.\"",
    "inn.bandit.stranger_efficiency": "The stranger moves with brutal efficiency.",
    "inn.bandit.shield_deflects": "His shield deflects the first blade while his sword disarms another.",
    "inn.bandit.strike_sprawling": "A single powerful strike sends the third bandit sprawling.",
    "inn.bandit.leader_flees": "The bandit leader takes one look and flees into the night.",
    "inn.bandit.wipes_blood": "The stranger wipes blood from his shield and turns to you.",
    "inn.bandit.aldric_reputation": "\"This inn used to have a better reputation.\"",
    "inn.bandit.extends_hand": "He extends a calloused hand.",
    "inn.bandit.aldric_name": "\"Name's Aldric. Former knight, current... wanderer.\"",
    "inn.bandit.aldric_purpose": "\"I've been looking for someone worth fighting alongside.\"",
    "inn.bandit.glances_appraisingly": "He glances at you appraisingly.",
    "inn.bandit.aldric_shield_back": "\"You look like you could use someone to watch your back.\"",
    "inn.bandit.aldric_protecting": "\"And I could use someone worth protecting.\"",
    "inn.bandit.accept_aldric": "Accept Aldric's offer",
    "inn.bandit.decline_aldric": "Politely decline",
    "inn.bandit.aldric_nods_solemnly": "Aldric nods solemnly.",
    "inn.bandit.aldric_find_trouble": "\"Good. I have a feeling we'll find plenty of trouble together.\"",
    "inn.bandit.aldric_got_your_back": "\"But at least now, you've got someone watching your back.\"",
    "inn.bandit.aldric_joined": "*** Aldric has joined your party! ***",
    "inn.bandit.aldric_tank_hint": "(Aldric is a Tank companion - he'll draw enemy attacks and protect you)",
    "inn.bandit.aldric_disappointed": "Aldric looks slightly disappointed, but nods.",
    "inn.bandit.aldric_understand": "\"I understand. Not everyone wants a stranger at their side.\"",
    "inn.bandit.aldric_change_mind": "\"But if you change your mind, you'll find me here.\"",
    "inn.bandit.aldric_recruit_later": "(You can recruit Aldric later by visiting the Inn)",
}

inn_bandit_es = {
    "inn.bandit.sitting_at_bar": "Estas sentado en la barra, tomando un trago tras un largo dia.",
    "inn.bandit.bandits_enter": "La puerta se abre de golpe y un grupo de bandidos armados entra pavoneandose.",
    "inn.bandit.leader_threat1": "\"Todos quietos! Entreguen su oro,\"",
    "inn.bandit.leader_threat2": "\"o pintaremos estas paredes con su sangre!\"",
    "inn.bandit.draw_weapons": "Los bandidos desenvainan sus armas, el acero brillando a la luz del fuego.",
    "inn.bandit.patrons_scatter": "Los clientes corren a cubrirse, tirando sillas y jarras.",
    "inn.bandit.chair_scrapes": "*Una silla raspa contra el suelo...*",
    "inn.bandit.stranger_rises": "Un desconocido se levanta lentamente de una mesa en la esquina.",
    "inn.bandit.tattered_armor": "Lleva una armadura gastada pero bien mantenida,",
    "inn.bandit.battered_shield": "y carga un escudo abollado que claramente ha visto muchas batallas.",
    "inn.bandit.aldric_sporting": "\"Esto no parece muy deportivo, verdad?\"",
    "inn.bandit.leader_stay_out": "\"No te metas, viejo, a menos que quieras morir!\"",
    "inn.bandit.aldric_i_am_trouble": "\"YO SOY el problema que no quieres encontrar.\"",
    "inn.bandit.stranger_efficiency": "El desconocido se mueve con brutal eficiencia.",
    "inn.bandit.shield_deflects": "Su escudo desvía la primera espada mientras su arma desarma a otro.",
    "inn.bandit.strike_sprawling": "Un solo golpe poderoso manda al tercer bandido al suelo.",
    "inn.bandit.leader_flees": "El lider de los bandidos mira y huye en la noche.",
    "inn.bandit.wipes_blood": "El desconocido limpia la sangre de su escudo y se vuelve hacia ti.",
    "inn.bandit.aldric_reputation": "\"Esta posada solia tener mejor reputacion.\"",
    "inn.bandit.extends_hand": "Extiende una mano callosa.",
    "inn.bandit.aldric_name": "\"Me llamo Aldric. Ex caballero, actualmente... vagabundo.\"",
    "inn.bandit.aldric_purpose": "\"He estado buscando a alguien digno de luchar a su lado.\"",
    "inn.bandit.glances_appraisingly": "Te mira evaluandote.",
    "inn.bandit.aldric_shield_back": "\"Parece que necesitas a alguien que te cuide las espaldas.\"",
    "inn.bandit.aldric_protecting": "\"Y yo necesito a alguien que valga la pena proteger.\"",
    "inn.bandit.accept_aldric": "Aceptar la oferta de Aldric",
    "inn.bandit.decline_aldric": "Rechazar cortesmente",
    "inn.bandit.aldric_nods_solemnly": "Aldric asiente solemnemente.",
    "inn.bandit.aldric_find_trouble": "\"Bien. Tengo la sensacion de que encontraremos muchos problemas juntos.\"",
    "inn.bandit.aldric_got_your_back": "\"Pero al menos ahora, alguien te cuida las espaldas.\"",
    "inn.bandit.aldric_joined": "*** Aldric se ha unido a tu grupo! ***",
    "inn.bandit.aldric_tank_hint": "(Aldric es un companero Tanque - atraera ataques enemigos y te protegera)",
    "inn.bandit.aldric_disappointed": "Aldric parece un poco decepcionado, pero asiente.",
    "inn.bandit.aldric_understand": "\"Lo entiendo. No todos quieren a un desconocido a su lado.\"",
    "inn.bandit.aldric_change_mind": "\"Pero si cambias de opinion, me encontraras aqui.\"",
    "inn.bandit.aldric_recruit_later": "(Puedes reclutar a Aldric mas tarde visitando la Posada)",
}

# === MAIN STREET (/health status labels) ===
main_street_en = {
    "main_street.align_good": "Good-Hearted",
    "main_street.align_neutral": "Neutral",
    "main_street.align_noble": "Noble Hero",
    "main_street.align_paragon": "Paragon of Virtue",
    "main_street.align_questionable": "Questionable",
    "main_street.align_usurper": "Usurper - Embodiment of Darkness",
    "main_street.align_villain": "Villain",
    "main_street.awakening_0": "Unawakened - You see only the surface of things",
    "main_street.awakening_1": "Stirring - Something deep within begins to move",
    "main_street.awakening_2": "Ripples - You sense connections between all things",
    "main_street.awakening_3": "Currents - The depths call to you with ancient whispers",
    "main_street.awakening_4": "Depths - You understand the ocean's sorrow",
    "main_street.awakening_5": "Enlightened - You are one with the eternal tide",
    "main_street.awakening_level": "Awakening Level: {0}/5",
    "main_street.awakening_unknown": "Unknown",
    "main_street.chivalry_label": "Chivalry:",
    "main_street.dark_clean": "Clean record",
    "main_street.dark_rumored": "Rumored misdeeds",
    "main_street.dark_suspicious": "Suspicious reputation",
    "main_street.dark_wanted": "WANTED by the Royal Guard!",
    "main_street.darkness_label": "Darkness:",
    "main_street.god_conquered": "Conquered",
    "main_street.god_defeated": "DEFEATED",
    "main_street.god_encountered": "Encountered",
    "main_street.god_known": "Known",
    "main_street.god_somewhere": "Somewhere in the depths...",
    "main_street.god_unknown": "Unknown",
    "main_street.gods_desc": "Ancient beings you may challenge for power or wisdom",
    "main_street.grief_acceptance": "Acceptance - Finding peace",
    "main_street.grief_anger": "Angry - Why did this happen?",
    "main_street.grief_bargaining": "Bargaining - If only...",
    "main_street.grief_denial": "In Denial - Loss seems unreal",
    "main_street.grief_depression": "Depressed - The weight of loss",
    "main_street.grief_label": "Grief:",
    "main_street.grief_none": "At Peace",
    "main_street.hint_creator": "All seals gathered. The Creator awaits in the deepest reaches...",
    "main_street.hint_ending": "You have completed your journey. Seek your ending.",
    "main_street.hint_seals": "The ancient seals await discovery in the dungeon's depths...",
    "main_street.ocean_desc": "Your spiritual awakening through grief, sacrifice, and understanding",
    "main_street.press_return": "Press Enter to return to Main Street...",
    "main_street.seals_collected": "Seals Collected: {0}/7",
    "main_street.seals_desc": "Ancient artifacts that reveal the truth of creation",
}

main_street_es = {
    "main_street.align_good": "Buen Corazon",
    "main_street.align_neutral": "Neutral",
    "main_street.align_noble": "Heroe Noble",
    "main_street.align_paragon": "Paragón de Virtud",
    "main_street.align_questionable": "Cuestionable",
    "main_street.align_usurper": "Usurpador - Encarnacion de la Oscuridad",
    "main_street.align_villain": "Villano",
    "main_street.awakening_0": "No Despierto - Solo ves la superficie de las cosas",
    "main_street.awakening_1": "Agitacion - Algo profundo dentro comienza a moverse",
    "main_street.awakening_2": "Ondas - Sientes conexiones entre todas las cosas",
    "main_street.awakening_3": "Corrientes - Las profundidades te llaman con susurros antiguos",
    "main_street.awakening_4": "Profundidades - Comprendes el dolor del oceano",
    "main_street.awakening_5": "Iluminado - Eres uno con la marea eterna",
    "main_street.awakening_level": "Nivel de Despertar: {0}/5",
    "main_street.awakening_unknown": "Desconocido",
    "main_street.chivalry_label": "Caballeria:",
    "main_street.dark_clean": "Historial limpio",
    "main_street.dark_rumored": "Fechorias rumoreadas",
    "main_street.dark_suspicious": "Reputacion sospechosa",
    "main_street.dark_wanted": "BUSCADO por la Guardia Real!",
    "main_street.darkness_label": "Oscuridad:",
    "main_street.god_conquered": "Conquistado",
    "main_street.god_defeated": "DERROTADO",
    "main_street.god_encountered": "Encontrado",
    "main_street.god_known": "Conocido",
    "main_street.god_somewhere": "En algún lugar de las profundidades...",
    "main_street.god_unknown": "Desconocido",
    "main_street.gods_desc": "Seres ancestrales que puedes desafiar por poder o sabiduria",
    "main_street.grief_acceptance": "Aceptacion - Encontrando paz",
    "main_street.grief_anger": "Enojado - Por que paso esto?",
    "main_street.grief_bargaining": "Negociacion - Si tan solo...",
    "main_street.grief_denial": "Negacion - La perdida parece irreal",
    "main_street.grief_depression": "Deprimido - El peso de la perdida",
    "main_street.grief_label": "Duelo:",
    "main_street.grief_none": "En Paz",
    "main_street.hint_creator": "Todos los sellos reunidos. El Creador espera en las profundidades...",
    "main_street.hint_ending": "Has completado tu viaje. Busca tu final.",
    "main_street.hint_seals": "Los sellos antiguos esperan ser descubiertos en las profundidades...",
    "main_street.ocean_desc": "Tu despertar espiritual a traves del duelo, sacrificio y comprension",
    "main_street.press_return": "Presiona Enter para volver a la Calle Principal...",
    "main_street.seals_collected": "Sellos Recolectados: {0}/7",
    "main_street.seals_desc": "Artefactos ancestrales que revelan la verdad de la creacion",
}

# === MAGIC SHOP (enchanting + disease cures) ===
magic_shop_en = {
    "magic_shop.enchant_examine": "{0} examines your equipment with a practiced eye...",
    "magic_shop.enchant_offer": "\"I can weave enchantments into your gear — for a price.\"",
    "magic_shop.no_equipment_enchant": "You have no equipment to enchant.",
    "magic_shop.come_back_armed": "\"Come back when you have something worth enchanting.\"",
    "magic_shop.select_item_enchant": "Select item to enchant (0 to cancel): ",
    "magic_shop.cursed_no_enchant": "\"I cannot enchant a cursed item!\"",
    "magic_shop.remove_curse_first": "\"Have the curse removed first.\"",
    "magic_shop.beyond_limits": "\"Even my magic has its limits.\"",
    "magic_shop.select_enchantment": "Select enchantment: ",
    "magic_shop.need_gold_enchant": "\"You lack the gold for this enchantment.\"",
    "magic_shop.cures_smallpox": "Cures smallpox",
    "magic_shop.cures_measles": "Cures measles",
}

magic_shop_es = {
    "magic_shop.enchant_examine": "{0} examina tu equipo con ojo experto...",
    "magic_shop.enchant_offer": "\"Puedo tejer encantamientos en tu equipo — por un precio.\"",
    "magic_shop.no_equipment_enchant": "No tienes equipo para encantar.",
    "magic_shop.come_back_armed": "\"Vuelve cuando tengas algo que valga la pena encantar.\"",
    "magic_shop.select_item_enchant": "Selecciona el articulo a encantar (0 para cancelar): ",
    "magic_shop.cursed_no_enchant": "\"No puedo encantar un objeto maldito!\"",
    "magic_shop.remove_curse_first": "\"Haz que eliminen la maldicion primero.\"",
    "magic_shop.beyond_limits": "\"Incluso mi magia tiene limites.\"",
    "magic_shop.select_enchantment": "Selecciona encantamiento: ",
    "magic_shop.need_gold_enchant": "\"No tienes el oro para este encantamiento.\"",
    "magic_shop.cures_smallpox": "Cura la viruela",
    "magic_shop.cures_measles": "Cura el sarampion",
}

# Apply all fixes
for lang in ['en', 'es']:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    added = 0
    if lang == 'en':
        all_keys = {**inn_bandit_en, **main_street_en, **magic_shop_en}
    else:
        all_keys = {**inn_bandit_es, **main_street_es, **magic_shop_es}

    for key, value in all_keys.items():
        if key not in data:
            data[key] = value
            added += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: added {added} missing keys")
