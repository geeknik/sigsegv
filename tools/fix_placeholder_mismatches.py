"""
Fix placeholder mismatches where JSON has {0}/{1} but code passes no args,
or where JSON values were extracted as full format strings but code uses them as labels.
"""
import json

# EN fixes: remove placeholders from values where code doesn't pass args
en_fixes = {
    # Leaked C# format expression
    "common.lvl": "Lvl",

    # {0}/{1} but no args passed
    "arena.victory": "Victory!",
    "engine.goodbye": "Goodbye! Until next time...",
    "dungeon.trap_triggered": "A trap has been triggered!",
    "dungeon.bbs_level": "Level",
    "combat.rage_effect": "RAGE! Increased damage this round!",
    "training.skill_improved": "Skill Improved!",
    "inventory.equip_confirm": "Equip this item? (Y/N): ",

    # Full format strings used as labels
    "base.potions_remaining": "Potions remaining",
    "base.time_label": "Time",
    "inventory.value": "Value",

    # Guard bribe menu option - no amount passed
    "street_encounter.guard.opt_bribe": "ribe",

    # Duelist dialogue keys called without args but have {0}
    "dungeon.duelist_decline_known_2": "\"Maybe next time, friend.\"",
    "dungeon.duelist_decline_new_2": "\"Perhaps we'll meet again.\"",
    "dungeon.duelist_insult_known_2": "\"You DARE?! After all our duels?!\"",
    "dungeon.duelist_insult_known_3": "\"I'll teach you some manners!\"",
    "dungeon.duelist_insult_new_2": "\"You'll regret those words!\"",
    "dungeon.duelist_loss1_2": "\"Well fought... I'll be back stronger.\"",
    "dungeon.duelist_loss3_2": "\"Three losses... but I learn from each one.\"",
    "dungeon.duelist_loss_default_2": "\"This isn't over between us.\"",

    # Type 1: args passed but value has no placeholder - add placeholders
    "combat.backstab_shadows": "You slip into the shadows behind {0}...",
    "combat.status_label": "Status: {0}",
    "street_encounter.challenge.walks_up": "{0} walks up to you with a confident stride.",
    "street_encounter.mugging.thugs_emerge": "{0} thugs emerge from the shadows!",

    # inventory.type and inventory.requires already have {0} — check if called without args
    # inventory.comparison already has {0} — check if called without args
    # Leaving these as-is since the code may use them correctly in other paths

    # inn keys
    "inn.interact_relationship": "Relationship: {0}",
    "inn.npc_regret_decision": "{0} accepts your challenge!",

    # encounter.cosmic.reward - called without args
    "encounter.cosmic.reward": "Gained XP and Wisdom!",

    # base keys called without args
    "base.system_message": "*** SYSTEM MESSAGE ***",

    # inventory keys called without args
    "inventory.type": "Type",
    "inventory.comparison": "COMPARISON",
    "inventory.requires": "Requires",
    "inventory.req_level": "Level",
}

# ES fixes
es_fixes = {
    "common.lvl": "Nvl",
    "arena.victory": "Victoria!",
    "engine.goodbye": "Adios! Hasta la proxima...",
    "dungeon.trap_triggered": "Se ha activado una trampa!",
    "dungeon.bbs_level": "Nivel",
    "combat.rage_effect": "FURIA! Dano aumentado esta ronda!",
    "training.skill_improved": "Habilidad Mejorada!",
    "inventory.equip_confirm": "Equipar este objeto? (S/N): ",
    "base.potions_remaining": "Pociones restantes",
    "base.time_label": "Hora",
    "inventory.value": "Valor",
    "street_encounter.guard.opt_bribe": "obornar",
    "dungeon.duelist_decline_known_2": "\"Quiza la proxima, amigo.\"",
    "dungeon.duelist_decline_new_2": "\"Quiza nos volvamos a encontrar.\"",
    "dungeon.duelist_insult_known_2": "\"TE ATREVES?! Despues de todos nuestros duelos?!\"",
    "dungeon.duelist_insult_known_3": "\"Te ensenare modales!\"",
    "dungeon.duelist_insult_new_2": "\"Te arrepentiras de esas palabras!\"",
    "dungeon.duelist_loss1_2": "\"Bien peleado... volvere mas fuerte.\"",
    "dungeon.duelist_loss3_2": "\"Tres derrotas... pero aprendo de cada una.\"",
    "dungeon.duelist_loss_default_2": "\"Esto no ha terminado entre nosotros.\"",
    "combat.backstab_shadows": "Te deslizas en las sombras detras de {0}...",
    "combat.status_label": "Estado: {0}",
    "street_encounter.challenge.walks_up": "{0} se acerca a ti con paso confiado.",
    "street_encounter.mugging.thugs_emerge": "{0} matones emergen de las sombras!",
    "inn.interact_relationship": "Relacion: {0}",
    "inn.npc_regret_decision": "{0} acepta tu desafio!",
    "encounter.cosmic.reward": "Ganaste XP y Sabiduria!",
    "base.system_message": "*** MENSAJE DEL SISTEMA ***",
    "inventory.type": "Tipo",
    "inventory.comparison": "COMPARACION",
    "inventory.requires": "Requiere",
    "inventory.req_level": "Nivel",
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
