import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

new_en = {
    # Missing CombatEngine keys
    "combat.precise_no_effect": "Precise Strike has no effect in this combat!",
    "combat.nothing_disarm": "Nothing to disarm!",
    "combat.hide_shadows_strike": "You melt into the shadows, ready to strike!",
    "combat.execution_double": "EXECUTION! Double damage to wounded enemy!",
    "combat.last_stand_attack": "LAST STAND! Desperation fuels your attack!",
    "combat.smoke_obscures": "A cloud of smoke obscures you from attack!",
    "combat.berserker_rage_fury": "BERSERKER RAGE! You enter a blood fury!",
    "combat.war_god_fury": "THE WAR GOD'S FURY BURNS WITHIN YOU!",
    "combat.bloodlust_heal": "BLOODLUST! Each kill will heal you!",
    "combat.unstoppable_afflictions": "UNSTOPPABLE! You shrug off all afflictions!",
    "combat.divine_shield_light": "A divine shield of pure light surrounds you!",
    "combat.brilliant_light": "A brilliant light pierces the darkness!",
    "combat.available_spells_label": "Available spells:",
    "combat.first_battle_tip": "TIP: Your First Battle!",

    # DungeonLocation keys
    "dungeon.party_member_entry": "  {0}. {1} (Level {2} {3}) - HP: {4}/{5}",
    "dungeon.remove_who": "Remove who? (#): ",
    "dungeon.removed_from_party": "{0} has been removed from the party.",
    "dungeon.party_full": "Your party is full!",
    "dungeon.merchant_greeting": "A wandering merchant appears!",
    "dungeon.merchant_potions": "  Healing Potions: {0}g each (You have {1})",
    "dungeon.merchant_buy_prompt": "Buy how many? (0 to skip): ",
    "dungeon.merchant_bought": "Bought {0} healing potions for {1}g!",
    "dungeon.merchant_cant_afford": "You can't afford that many!",
    "dungeon.witch_doctor": "A witch doctor offers to cure your ailments!",
    "dungeon.witch_cure_cost": "  Cure disease: {0}g",
    "dungeon.witch_cure_prompt": "Accept healing? (Y/N): ",
    "dungeon.witch_cured": "The witch doctor cures your disease!",
    "dungeon.witch_no_gold": "You don't have enough gold!",
    "dungeon.witch_healthy": "You are already healthy!",
    "dungeon.potion_healed": "Healed {0} HP! (HP: {1}/{2})",
    "dungeon.no_potions": "You don't have any healing potions!",
    "dungeon.mana_potion_restored": "Restored {0} MP! (MP: {1}/{2})",
    "dungeon.no_mana_potions": "You don't have any mana potions!",
    "dungeon.level_too_low": "You must be at least level {0} to access floor {1}!",
    "dungeon.level_too_high": "Floor {0} is too far below your level ({1}). Max accessible: floor {2}.",
    "dungeon.safe_haven": "You find a safe haven to rest!",
    "dungeon.safe_rest_healed": "Rested and recovered {0} HP.",
    "dungeon.camping_header": "=== Camping ===",
    "dungeon.camping_rest": "You set up camp and rest...",
    "dungeon.camping_healed": "Recovered {0} HP from camping.",
    "dungeon.camping_fatigue": "Fatigue reduced by {0}.",
    "dungeon.floor_cleared": "This floor has been cleared!",
    "dungeon.descend_prompt": "Descend to floor {0}? (Y/N): ",
    "dungeon.ascend_prompt": "Ascend to floor {0}? (Y/N): ",
    "dungeon.trap_detected": "You detect a trap! Attempt to disarm? (Y/N): ",
    "dungeon.trap_disarmed": "Trap disarmed successfully!",
    "dungeon.trap_triggered": "The trap triggers! You take {0} damage!",
    "dungeon.trap_sprung": "You spring a trap! {0} damage!",

    # BaseLocation remaining
    "base.none_independent": "None (Independent)",
    "base.send_to_prompt": "Send to: ",

    # GameEngine keys
    "engine.save_complete": "Game saved!",
    "engine.load_complete": "Game loaded!",
    "engine.autosave": "Autosaving...",
    "engine.welcome_back": "Welcome back, {0}!",
    "engine.new_game_created": "New game created!",
    "engine.confirm_quit": "Are you sure you want to quit? (Y/N): ",
    "engine.goodbye": "Goodbye, {0}! Until next time...",

    # CharacterCreation keys
    "charcreate.choose_name": "Choose your name: ",
    "charcreate.name_taken": "That name is already taken!",
    "charcreate.name_invalid": "Invalid name. Use letters only, 2-15 characters.",
    "charcreate.choose_race": "Choose your race:",
    "charcreate.choose_class": "Choose your class:",
    "charcreate.confirm_creation": "Create this character? (Y/N): ",
    "charcreate.character_created": "Character created! Welcome to the world, {0}!",
    "charcreate.reroll_stats": "Reroll stats? (Y/N): ",

    # Arena keys
    "arena.challenge_prompt": "Challenge who? (#): ",
    "arena.no_opponents": "No opponents available right now.",
    "arena.victory": "Victory! You earned {0} XP and {1} gold!",
    "arena.defeat": "You have been defeated!",
    "arena.fled": "You fled from combat!",
    "arena.bet_prompt": "Place a bet? (amount or 0): ",
    "arena.bet_won": "You won your bet! +{0} gold!",
    "arena.bet_lost": "You lost your bet! -{0} gold!",

    # TrainingSystem keys
    "training.skill_header": "=== Skill Training ===",
    "training.points_available": "Training Points Available: {0}",
    "training.skill_entry": "  {0}. {1}: {2}/{3}",
    "training.choose_skill": "Choose skill to train (#, or 0 to exit): ",
    "training.skill_improved": "{0} improved to {1}!",
    "training.skill_maxed": "{0} is already at maximum!",
    "training.no_points": "No training points available!",
    "training.cost_label": "Cost: {0} point(s)",

    # LocationManager keys
    "location.traveling": "Traveling to {0}...",
    "location.cannot_travel": "You cannot travel there right now.",
    "location.arrive": "You arrive at {0}.",
}

new_es = {
    "combat.precise_no_effect": "¡Golpe Preciso no tiene efecto en este combate!",
    "combat.nothing_disarm": "¡Nada que desarmar!",
    "combat.hide_shadows_strike": "¡Te fundes con las sombras, listo para atacar!",
    "combat.execution_double": "¡EJECUCIÓN! ¡Daño doble al enemigo herido!",
    "combat.last_stand_attack": "¡ÚLTIMA RESISTENCIA! ¡La desesperación impulsa tu ataque!",
    "combat.smoke_obscures": "¡Una nube de humo te oculta del ataque!",
    "combat.berserker_rage_fury": "¡FURIA BERSERKER! ¡Entras en una furia sangrienta!",
    "combat.war_god_fury": "¡LA FURIA DEL DIOS DE LA GUERRA ARDE EN TI!",
    "combat.bloodlust_heal": "¡SED DE SANGRE! ¡Cada muerte te sanará!",
    "combat.unstoppable_afflictions": "¡IMPARABLE! ¡Rechazas todas las aflicciones!",
    "combat.divine_shield_light": "¡Un escudo divino de luz pura te rodea!",
    "combat.brilliant_light": "¡Una luz brillante atraviesa la oscuridad!",
    "combat.available_spells_label": "Hechizos disponibles:",
    "combat.first_battle_tip": "CONSEJO: ¡Tu Primera Batalla!",

    "dungeon.party_member_entry": "  {0}. {1} (Nivel {2} {3}) - PV: {4}/{5}",
    "dungeon.remove_who": "¿Remover a quién? (#): ",
    "dungeon.removed_from_party": "{0} ha sido removido del grupo.",
    "dungeon.party_full": "¡Tu grupo está lleno!",
    "dungeon.merchant_greeting": "¡Aparece un mercader ambulante!",
    "dungeon.merchant_potions": "  Pociones curativas: {0}g cada una (Tienes {1})",
    "dungeon.merchant_buy_prompt": "¿Cuántas comprar? (0 para omitir): ",
    "dungeon.merchant_bought": "¡Compradas {0} pociones curativas por {1}g!",
    "dungeon.merchant_cant_afford": "¡No puedes pagar tantas!",
    "dungeon.witch_doctor": "¡Un brujo ofrece curar tus males!",
    "dungeon.witch_cure_cost": "  Curar enfermedad: {0}g",
    "dungeon.witch_cure_prompt": "¿Aceptar curación? (S/N): ",
    "dungeon.witch_cured": "¡El brujo cura tu enfermedad!",
    "dungeon.witch_no_gold": "¡No tienes suficiente oro!",
    "dungeon.witch_healthy": "¡Ya estás saludable!",
    "dungeon.potion_healed": "¡Curado {0} PV! (PV: {1}/{2})",
    "dungeon.no_potions": "¡No tienes pociones curativas!",
    "dungeon.mana_potion_restored": "¡Restaurado {0} PM! (PM: {1}/{2})",
    "dungeon.no_mana_potions": "¡No tienes pociones de maná!",
    "dungeon.level_too_low": "¡Debes ser al menos nivel {0} para acceder al piso {1}!",
    "dungeon.level_too_high": "El piso {0} está demasiado lejos de tu nivel ({1}). Máximo accesible: piso {2}.",
    "dungeon.safe_haven": "¡Encuentras un refugio seguro para descansar!",
    "dungeon.safe_rest_healed": "Descansaste y recuperaste {0} PV.",
    "dungeon.camping_header": "=== Acampar ===",
    "dungeon.camping_rest": "Montas un campamento y descansas...",
    "dungeon.camping_healed": "Recuperaste {0} PV acampando.",
    "dungeon.camping_fatigue": "Fatiga reducida en {0}.",
    "dungeon.floor_cleared": "¡Este piso ha sido limpiado!",
    "dungeon.descend_prompt": "¿Descender al piso {0}? (S/N): ",
    "dungeon.ascend_prompt": "¿Ascender al piso {0}? (S/N): ",
    "dungeon.trap_detected": "¡Detectas una trampa! ¿Intentar desarmar? (S/N): ",
    "dungeon.trap_disarmed": "¡Trampa desarmada exitosamente!",
    "dungeon.trap_triggered": "¡La trampa se activa! ¡Recibes {0} de daño!",
    "dungeon.trap_sprung": "¡Caes en una trampa! ¡{0} de daño!",

    "base.none_independent": "Ninguna (Independiente)",
    "base.send_to_prompt": "Enviar a: ",

    "engine.save_complete": "¡Juego guardado!",
    "engine.load_complete": "¡Juego cargado!",
    "engine.autosave": "Autoguardando...",
    "engine.welcome_back": "¡Bienvenido de vuelta, {0}!",
    "engine.new_game_created": "¡Nuevo juego creado!",
    "engine.confirm_quit": "¿Estás seguro de que quieres salir? (S/N): ",
    "engine.goodbye": "¡Adiós, {0}! Hasta la próxima...",

    "charcreate.choose_name": "Elige tu nombre: ",
    "charcreate.name_taken": "¡Ese nombre ya está en uso!",
    "charcreate.name_invalid": "Nombre inválido. Usa solo letras, 2-15 caracteres.",
    "charcreate.choose_race": "Elige tu raza:",
    "charcreate.choose_class": "Elige tu clase:",
    "charcreate.confirm_creation": "¿Crear este personaje? (S/N): ",
    "charcreate.character_created": "¡Personaje creado! ¡Bienvenido al mundo, {0}!",
    "charcreate.reroll_stats": "¿Relanzar estadísticas? (S/N): ",

    "arena.challenge_prompt": "¿Desafiar a quién? (#): ",
    "arena.no_opponents": "No hay oponentes disponibles ahora.",
    "arena.victory": "¡Victoria! ¡Ganaste {0} XP y {1} oro!",
    "arena.defeat": "¡Has sido derrotado!",
    "arena.fled": "¡Huiste del combate!",
    "arena.bet_prompt": "¿Hacer una apuesta? (cantidad o 0): ",
    "arena.bet_won": "¡Ganaste tu apuesta! +{0} oro!",
    "arena.bet_lost": "¡Perdiste tu apuesta! -{0} oro!",

    "training.skill_header": "=== Entrenamiento de Habilidades ===",
    "training.points_available": "Puntos de Entrenamiento Disponibles: {0}",
    "training.skill_entry": "  {0}. {1}: {2}/{3}",
    "training.choose_skill": "Elige habilidad a entrenar (#, o 0 para salir): ",
    "training.skill_improved": "¡{0} mejorada a {1}!",
    "training.skill_maxed": "¡{0} ya está al máximo!",
    "training.no_points": "¡No hay puntos de entrenamiento disponibles!",
    "training.cost_label": "Costo: {0} punto(s)",

    "location.traveling": "Viajando a {0}...",
    "location.cannot_travel": "No puedes viajar allí ahora.",
    "location.arrive": "Llegas a {0}.",
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
