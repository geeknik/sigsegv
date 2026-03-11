import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

new_en = {
    # Combat UI labels
    "combat.status_effects_label": "Status Effects:",
    "combat.choose_action": "Choose action: ",
    "combat.flee_label": "Flee ",
    "combat.disarm_label": "Disarm ",
    "combat.hide_label": "Hide ",
    "combat.save_label": "Save",
    "combat.enemies_label": "Enemies:",
    "combat.status_label": "Status: ",
    "combat.choose_cancel": "Choose (0 to cancel): ",
    "combat.replace_yn": "Replace it? (Y/N): ",
    "combat.choose_target": "Choose target: ",
    "combat.choose_aid": "Choose aid method: ",
    "combat.choose_spell": "Choose spell: ",
    "combat.target_label": "Target: ",
    "combat.enter_ability_num": "Enter ability number (0 to cancel): ",
    "combat.enter_spell_num": "Enter spell number (0 to cancel): ",
    "combat.which_potion": "Which potion?",
    "combat.target_all_yn": "Target all monsters? (Y/N): ",
    "combat.available_abilities": "Available Abilities:",
    "combat.available_spells": "Available Spells:",
    "combat.select_healing_spell": "Select healing spell:",
    "combat.select_heal_target": "Select heal target:",
    "combat.select_target": "Select target:",
    "combat.team_xp_distribution": "Team XP Distribution:",
    "combat.equipment_salvaged": "Equipment salvaged:",

    # Combat errors/validation
    "combat.invalid_target": "Invalid target!",
    "combat.invalid_choice": "Invalid choice.",
    "combat.invalid_spell": "Invalid spell.",
    "combat.invalid_action": "Invalid action, please try again",
    "combat.invalid_option": "Please choose a valid option.",
    "combat.monster_already_dead": "That monster is already dead!",
    "combat.no_spells_yet": "You don't know any spells yet!",
    "combat.invalid_choice_excl": "Invalid choice!",
    "combat.unknown_ability": "Unknown ability!",
    "combat.invalid_target_list": "Invalid target. Enter a number from the list above.",
    "combat.mana_already_full": "Your mana is already full!",
    "combat.already_cast_spell": "You have already cast a spell this round!",
    "combat.cant_cast_spell": "You cannot cast this spell right now!",
    "combat.invalid_spell_selection": "Invalid spell selection!",
    "combat.no_abilities_yet": "You haven't learned any abilities yet!",
    "combat.cant_use_ability": "Cannot use that ability right now!",
    "combat.no_castable_spells": "You don't know any spells you can cast!",
    "combat.spell_cancelled": "Spell cancelled.",
    "combat.quickbar_empty": "That quickbar slot is empty!",
    "combat.not_available_pvp": "That action is not available in PvP combat.",
    "combat.no_matching_ability": "No matching ability available — using basic attack.",

    # Sunforged Blade
    "combat.sunforged_guides": "The Sunforged Blade guides your strike true!",
    "combat.sunforged_blazes": "The Sunforged Blade blazes with holy fire!",

    # Combat narrative
    "combat.backstab_no_effect": "Backstab has no effect in this combat!",
    "combat.monster_no_mercy": "The monster shows no mercy!",
    "combat.monster_pity": "The monster takes pity on you and lets you live!",
    "combat.monk_nods": "The monk nods and continues on his way.",
    "combat.monk_bows": "The monk bows and departs.",
    "combat.auto_combat_pause": "Combat will pause if you take manual control.",
    "combat.smoke_bomb": "You throw a smoke bomb and vanish into the haze!",

    # Loot equip
    "combat.one_handed_where": "This is a one-handed weapon. Where would you like to equip it?",
    "combat.both_rings_occupied": "Both ring slots are occupied. Which ring would you like to replace?",

    # Death/resurrection
    "combat.alive_but_cost": "You are alive. But at what cost?",
    "combat.more_challenges": "The dungeons hold many more challenges...",
    "combat.darkness_claims": "The darkness claims you.",
    "combat.gods_heard_prayers": "The gods have heard your prayers!",
    "combat.temple_priests_chant": "Temple priests chant sacred words...",
    "combat.magic_pulls_soul": "Their magic pulls your soul back from the void!",
    "combat.cold_presence": "You feel a cold presence...",
    "combat.death_claims": "Death claims you...",
    "combat.item_slips": "An item slips from your grasp as you fall!",

    # Berserker rage
    "combat.berserker_rage": "Your eyes turn red with fury! No retreat, no mercy!",
    "combat.berserker_fight_death": "You will fight until death - yours or theirs!",
    "combat.berserker_subsides": "The blood rage subsides as your enemy falls...",
    "combat.berserker_not_enough": "Your berserker rage was not enough...",
    "combat.berserker_glorious": "You fall in glorious battle!",

    # Ability effects
    "combat.acid_ignores_armor": "The acid ignores armor!",
    "combat.critical_from_shadows": "Critical strike from the shadows!",
    "combat.vanish_puff_smoke": "You vanish in a puff of smoke!",
    "combat.prepare_dodge": "You prepare to dodge the next attack!",
    "combat.melody_steels": "The melody steels your resolve! (+10 Attack for 3 rounds)",
    "combat.will_unbreakable": "Your will becomes unbreakable! Status effects cannot touch you!",
    "combat.reckless_swing": "Reckless swing! You leave yourself exposed!",
    "combat.divine_energy": "Divine energy radiates from your weapon!",
    "combat.strike_vital": "You strike a vital point!",
    "combat.melt_shadows": "You melt into the shadows, nearly impossible to hit!",
    "combat.blend_surroundings": "You blend perfectly with your surroundings!",
    "combat.holy_light": "Holy light washes over you!",
    "combat.vanish_completely": "You vanish completely! Your next attack will strike from the shadows!",
    "combat.shadows_embrace": "Shadows embrace you. Noctura's power flows through you!",
    "combat.become_legend": "You become the legend! Songs of power flow through you!",
    "combat.status_immunity_fades": "Your status immunity fades.",
    "combat.manage_escape": "You manage to escape!",
    "combat.last_stand": "Last Stand! Fighting with desperate strength!",

    # Defense/tactical
    "combat.raise_guard": "You raise your guard, preparing to deflect incoming blows.",
    "combat.power_attack_no_effect": "Power Attack has no effect in this combat!",
    "combat.precise_strike_no_effect": "Precise Strike has no effect in this combat!",
    "combat.missile_misses": "Your missile misses the target.",
    "combat.bloodthirsty_rage": "You fly into a bloodthirsty rage!",
    "combat.smite_no_effect": "Smite has no effect in this combat!",
    "combat.out_of_smites": "You are out of smite charges!",
    "combat.nothing_to_disarm": "Nothing to disarm!",
    "combat.disarm_failed": "Disarm attempt failed!",
    "combat.hide_shadows": "You melt into the shadows, ready to strike!",
    "combat.hide_failed": "You fail to find cover and remain exposed.",

    # Taming
    "combat.tame_respect": "It gazes at you with newfound respect...",
    "combat.tame_fight_alongside": "It will fight by your side for this battle!",
    "combat.tame_too_strong": "The creature's will is too strong...",

    # Disease
    "combat.contracted_plague": "You have contracted the plague!",
}

new_es = {
    "combat.status_effects_label": "Efectos de Estado:",
    "combat.choose_action": "Elige acción: ",
    "combat.flee_label": "Huir ",
    "combat.disarm_label": "Desarmar ",
    "combat.hide_label": "Esconderse ",
    "combat.save_label": "Guardar",
    "combat.enemies_label": "Enemigos:",
    "combat.status_label": "Estado: ",
    "combat.choose_cancel": "Elige (0 para cancelar): ",
    "combat.replace_yn": "¿Reemplazar? (S/N): ",
    "combat.choose_target": "Elige objetivo: ",
    "combat.choose_aid": "Elige método de ayuda: ",
    "combat.choose_spell": "Elige hechizo: ",
    "combat.target_label": "Objetivo: ",
    "combat.enter_ability_num": "Número de habilidad (0 para cancelar): ",
    "combat.enter_spell_num": "Número de hechizo (0 para cancelar): ",
    "combat.which_potion": "¿Qué poción?",
    "combat.target_all_yn": "¿Atacar a todos los monstruos? (S/N): ",
    "combat.available_abilities": "Habilidades Disponibles:",
    "combat.available_spells": "Hechizos Disponibles:",
    "combat.select_healing_spell": "Seleccionar hechizo de curación:",
    "combat.select_heal_target": "Seleccionar objetivo de curación:",
    "combat.select_target": "Seleccionar objetivo:",
    "combat.team_xp_distribution": "Distribución de XP del Equipo:",
    "combat.equipment_salvaged": "Equipo recuperado:",

    "combat.invalid_target": "¡Objetivo inválido!",
    "combat.invalid_choice": "Opción inválida.",
    "combat.invalid_spell": "Hechizo inválido.",
    "combat.invalid_action": "Acción inválida, inténtalo de nuevo",
    "combat.invalid_option": "Por favor elige una opción válida.",
    "combat.monster_already_dead": "¡Ese monstruo ya está muerto!",
    "combat.no_spells_yet": "¡Aún no conoces ningún hechizo!",
    "combat.invalid_choice_excl": "¡Opción inválida!",
    "combat.unknown_ability": "¡Habilidad desconocida!",
    "combat.invalid_target_list": "Objetivo inválido. Ingresa un número de la lista.",
    "combat.mana_already_full": "¡Tu maná ya está al máximo!",
    "combat.already_cast_spell": "¡Ya lanzaste un hechizo esta ronda!",
    "combat.cant_cast_spell": "¡No puedes lanzar este hechizo ahora!",
    "combat.invalid_spell_selection": "¡Selección de hechizo inválida!",
    "combat.no_abilities_yet": "¡Aún no has aprendido ninguna habilidad!",
    "combat.cant_use_ability": "¡No puedes usar esa habilidad ahora!",
    "combat.no_castable_spells": "¡No conoces hechizos que puedas lanzar!",
    "combat.spell_cancelled": "Hechizo cancelado.",
    "combat.quickbar_empty": "¡Esa ranura de acceso rápido está vacía!",
    "combat.not_available_pvp": "Esa acción no está disponible en combate JcJ.",
    "combat.no_matching_ability": "No hay habilidad disponible — usando ataque básico.",

    "combat.sunforged_guides": "¡La Espada Forjada por el Sol guía tu golpe!",
    "combat.sunforged_blazes": "¡La Espada Forjada por el Sol arde con fuego sagrado!",

    "combat.backstab_no_effect": "¡La puñalada por la espalda no tiene efecto en este combate!",
    "combat.monster_no_mercy": "¡El monstruo no muestra piedad!",
    "combat.monster_pity": "¡El monstruo se apiada de ti y te deja vivir!",
    "combat.monk_nods": "El monje asiente y sigue su camino.",
    "combat.monk_bows": "El monje hace una reverencia y se va.",
    "combat.auto_combat_pause": "El combate se pausará si tomas control manual.",
    "combat.smoke_bomb": "¡Lanzas una bomba de humo y desapareces en la bruma!",

    "combat.one_handed_where": "Esta es un arma a una mano. ¿Dónde quieres equiparla?",
    "combat.both_rings_occupied": "Ambas ranuras de anillo están ocupadas. ¿Cuál quieres reemplazar?",

    "combat.alive_but_cost": "Estás vivo. Pero ¿a qué precio?",
    "combat.more_challenges": "Las mazmorras guardan muchos más desafíos...",
    "combat.darkness_claims": "La oscuridad te reclama.",
    "combat.gods_heard_prayers": "¡Los dioses han escuchado tus plegarias!",
    "combat.temple_priests_chant": "Los sacerdotes del templo entonan palabras sagradas...",
    "combat.magic_pulls_soul": "¡Su magia trae tu alma de vuelta del vacío!",
    "combat.cold_presence": "Sientes una presencia fría...",
    "combat.death_claims": "La muerte te reclama...",
    "combat.item_slips": "¡Un objeto se te escapa al caer!",

    "combat.berserker_rage": "¡Tus ojos se vuelven rojos de furia! ¡Sin retirada, sin piedad!",
    "combat.berserker_fight_death": "¡Lucharás hasta la muerte — la tuya o la de ellos!",
    "combat.berserker_subsides": "La furia sanguínea se calma cuando tu enemigo cae...",
    "combat.berserker_not_enough": "Tu furia berserker no fue suficiente...",
    "combat.berserker_glorious": "¡Caes en gloriosa batalla!",

    "combat.acid_ignores_armor": "¡El ácido ignora la armadura!",
    "combat.critical_from_shadows": "¡Golpe crítico desde las sombras!",
    "combat.vanish_puff_smoke": "¡Desapareces en una nube de humo!",
    "combat.prepare_dodge": "¡Te preparas para esquivar el próximo ataque!",
    "combat.melody_steels": "¡La melodía fortalece tu determinación! (+10 Ataque por 3 rondas)",
    "combat.will_unbreakable": "¡Tu voluntad se vuelve inquebrantable! ¡Los efectos de estado no pueden tocarte!",
    "combat.reckless_swing": "¡Golpe temerario! ¡Te dejas expuesto!",
    "combat.divine_energy": "¡Energía divina irradia de tu arma!",
    "combat.strike_vital": "¡Golpeas un punto vital!",
    "combat.melt_shadows": "¡Te fundes con las sombras, casi imposible de golpear!",
    "combat.blend_surroundings": "¡Te mezclas perfectamente con tu entorno!",
    "combat.holy_light": "¡La luz sagrada te envuelve!",
    "combat.vanish_completely": "¡Desapareces completamente! ¡Tu próximo ataque será desde las sombras!",
    "combat.shadows_embrace": "Las sombras te abrazan. ¡El poder de Noctura fluye a través de ti!",
    "combat.become_legend": "¡Te conviertes en la leyenda! ¡Canciones de poder fluyen a través de ti!",
    "combat.status_immunity_fades": "Tu inmunidad a estados se desvanece.",
    "combat.manage_escape": "¡Logras escapar!",
    "combat.last_stand": "¡Última resistencia! ¡Luchando con fuerza desesperada!",

    "combat.raise_guard": "Alzas tu guardia, preparándote para desviar los golpes entrantes.",
    "combat.power_attack_no_effect": "¡El Ataque Poderoso no tiene efecto en este combate!",
    "combat.precise_strike_no_effect": "¡El Golpe Preciso no tiene efecto en este combate!",
    "combat.missile_misses": "Tu proyectil falla el objetivo.",
    "combat.bloodthirsty_rage": "¡Te lanzas en una furia sanguinaria!",
    "combat.smite_no_effect": "¡Castigar no tiene efecto en este combate!",
    "combat.out_of_smites": "¡Te quedaste sin cargas de castigar!",
    "combat.nothing_to_disarm": "¡Nada que desarmar!",
    "combat.disarm_failed": "¡Intento de desarme fallido!",
    "combat.hide_shadows": "¡Te fundes con las sombras, listo para atacar!",
    "combat.hide_failed": "No encuentras cobertura y quedas expuesto.",

    "combat.tame_respect": "Te mira con nuevo respeto...",
    "combat.tame_fight_alongside": "¡Luchará a tu lado en esta batalla!",
    "combat.tame_too_strong": "La voluntad de la criatura es demasiado fuerte...",

    "combat.contracted_plague": "¡Has contraído la plaga!",
}

for k, v in new_en.items():
    en[k] = v
for k, v in new_es.items():
    es[k] = v

with open('Localization/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_en)} en keys, {len(new_es)} es keys. en: {len(en)}, es: {len(es)}")
