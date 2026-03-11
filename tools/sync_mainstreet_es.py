#!/usr/bin/env python3
"""Generate Spanish translations for all missing main_street.* keys."""
import json

en = json.load(open('Localization/en.json', 'r', encoding='utf-8'))
es = json.load(open('Localization/es.json', 'r', encoding='utf-8'))

t = {
    # Ambient
    "main_street.ambient_merchant": "Un mercader pregona el precio de sus mercancías.",
    "main_street.ambient_crowd": "La multitud se mueve y murmura a tu alrededor.",
    "main_street.ambient_bell": "Una campana lejana marca la hora.",
    "main_street.ambient_cart": "Las ruedas de un carro traquetean sobre los adoquines.",
    "main_street.ambient_bread": "El viento trae el olor de pan fresco de un puesto cercano.",
    "main_street.ambient_dog": "Un perro ladra en algún callejón.",
    "main_street.ambient_guards": "Dos guardias intercambian palabras al pasar.",

    # Description
    "main_street.desc_standing": "Estás de pie en la calle principal de {0}.",
    "main_street.desc_air": "El aire {0} está {1}.",
    "main_street.bbs_desc": " Las calles {0} de {1}. El aire está {2}.",
    "main_street.you_notice": " Notas: ",
    "main_street.and_others": ", y {0} otro{1}",
    "main_street.new_adventurer_prefix": "¿Nuevo aventurero? Presiona ",
    "main_street.new_adventurer_key": "[D]",
    "main_street.new_adventurer_suffix": " para entrar a las Mazmorras!",
    "main_street.training_points": "¡Tienes {0} puntos de entrenamiento! ¡Visita al Maestro de Nivel para gastarlos!",

    # Companion teasers
    "main_street.vex_teaser1": "  Un extraño de dedos ágiles se mueve entre la multitud.",
    "main_street.vex_teaser2": "  Te ve, guiña un ojo y desaparece entre la multitud.",
    "main_street.lyris_teaser1": "  Una mujer encapuchada pasa entre la multitud, sus labios moviéndose en oración silenciosa.",
    "main_street.lyris_teaser2": "  Te mira brevemente. Algo en sus ojos te inquieta.",
    "main_street.god_slayer_buff": "El poder divino fluye a través de ti. ({0} combates restantes)",

    # BBS
    "main_street.bbs_main_street": "CALLE PRINCIPAL",
    "main_street.numpad_hint": " Numpad: 1=Sanador 2=Misiones 3=Armas 4=Armadura 5=Templo 6=Castillo 7=Hogar 8=Maestro",
    "main_street.level_eligible_sr": "¡Eres elegible para subir de nivel! ¡Visita a tu Maestro para avanzar!",
    "main_street.level_eligible": "     * ¡Eres elegible para subir de nivel! ¡Visita a tu Maestro para avanzar! *    ",
    "main_street.team_corner_level_req": "Debes ser nivel 5 o superior para acceder al Rincón de Equipos.",

    # Navigation
    "main_street.nav_temple": "Entras al Templo de los Dioses...",
    "main_street.nav_love_street": "Te diriges a la Calle del Amor...",
    "main_street.nav_dark_alley": "Te diriges al Callejón Oscuro...",
    "main_street.nav_settlement": "Te diriges más allá de las puertas al asentamiento...",
    "main_street.nav_team_corner": "Te diriges al Rincón de Equipos de Aventureros...",
    "main_street.invalid_choice": "¡Opción inválida! Escribe ? para ayuda.",

    # Good Deeds
    "main_street.good_deeds_title": "Buenas Obras",
    "main_street.good_deeds_divider": "==========",
    "main_street.your_chivalry": "Tu Caballerosidad: {0}",
    "main_street.deeds_left": "Buenas obras restantes hoy: {0}",
    "main_street.available_deeds": "Buenas obras disponibles:",
    "main_street.deed_give_gold": "1. Dar oro a los pobres",
    "main_street.deed_help_temple": "2. Ayudar en el templo",
    "main_street.deed_orphanage": "3. Voluntariado en el orfanato",
    "main_street.deed_prompt": "Elige una obra (1-3, 0 para cancelar): ",
    "main_street.deed_done_today": "Has hecho suficiente bien por hoy.",
    "main_street.deed_giving_gold": "dando oro a los pobres",
    "main_street.deed_helping_temple": "ayudando en el templo",
    "main_street.deed_volunteering": "siendo voluntario en el orfanato",
    "main_street.deed_generic": "realizando una buena obra",
    "main_street.deed_chivalry_gain": "¡Ganas caballerosidad por {0}!",

    # Fame
    "main_street.fame_subtitle": "  Los Más Grandes Héroes del Reino",
    "main_street.fame_your_rank": "  Tu Rango: #{0} de {1} - {2} (Nivel {3})",
    "main_street.fame_page": "  Página {0}/{1}",

    # Citizens
    "main_street.citizens_adventurers": "Adventureros y Ciudadanos:",
    "main_street.citizens_no_adventurers": "No hay aventureros registrados aún.",
    "main_street.citizens_fallen": "Los Caídos:",
    "main_street.citizens_no_fallen": "Ningún aventurero ha caído aún.",
    "main_street.citizens_you_tag": " (tú)",

    # Achievements
    "main_street.achieve_unlocked": "Desbloqueados: {0}/{1}",
    "main_street.achieve_points": "Puntos: {0}",
    "main_street.achieve_categories_label": "Categorías:",
    "main_street.achieve_combat": "1. Combate",
    "main_street.achieve_progression": "2. Progresión",
    "main_street.achieve_economy": "3. Economía",
    "main_street.achieve_exploration": "4. Exploración",
    "main_street.achieve_social": "5. Social",
    "main_street.achieve_challenge": "6. Desafío",
    "main_street.achieve_secret": "7. Secreto",
    "main_street.achieve_all": "8. Todos",
    "main_street.achieve_categories_visual": "1. Combate  2. Progresión  3. Economía  4. Exploración",
    "main_street.achieve_categories_visual2": "5. Social   6. Desafío    7. Secreto   8. Todos",
    "main_street.achieve_select_prompt": "Seleccionar categoría (0 para volver): ",
    "main_street.achieve_unlocked_date": "Desbloqueado: {0}",
    "main_street.achieve_more_prompt": "[M]ás, o cualquier tecla para volver",
    "main_street.achieve_header": "Logros - {0}",

    # Attack
    "main_street.attack_no_targets": "No hay nadie para atacar aquí.",
    "main_street.attack_who_question": "¿A quién deseas atacar?",
    "main_street.attack_npc_info": "{0}. {1} (Nivel {2} {3})",
    "main_street.attack_cancel": "0. Cancelar",
    "main_street.attack_prompt": "Objetivo: ",
    "main_street.attack_approach": "Te acercas a {0} con intención hostil...",
    "main_street.attack_warning": "¡ADVERTENCIA: Atacar a un ciudadano es un crimen grave!",
    "main_street.attack_confirm": "¿Realmente atacar a {0}? (S/N): ",
    "main_street.attack_victory": "¡Has derrotado a {0}!",
    "main_street.attack_defeat": "¡{0} te ha derrotado!",
    "main_street.attack_cancel_decision": "Decides no atacar.",
    "main_street.attack_change_mind": "Cambias de opinión.",

    # Quit/Sleep
    "main_street.quit_where_sleep": "¿Dónde quieres dormir?",
    "main_street.quit_dormitory_desc": "Dormitorio (gratis, inseguro)",
    "main_street.quit_inn_desc": "Posada ({0} oro, seguro)",
    "main_street.quit_home_desc": "Hogar (gratis, seguro)",
    "main_street.quit_home_sleep": "Te retiras a tu hogar para dormir...",
    "main_street.quit_street_sleep": "Te acurrucas en el dormitorio para descansar...",
    "main_street.quit_dormitory_sleep": "Te acurrucas en el dormitorio para descansar...",

    # Session stats
    "main_street.session_duration": "Duración de la Sesión: {0}",
    "main_street.session_monsters": "Monstruos Derrotados: {0}",
    "main_street.session_damage": "Daño Infligido: {0}",
    "main_street.session_levels": "Niveles Ganados: {0}",
    "main_street.session_xp": "XP Ganada: {0}",
    "main_street.session_gold": "Oro Ganado: {0}",
    "main_street.session_items": "Objetos Encontrados: {0}",
    "main_street.session_items_detail": "Objetos Encontrados: {0} ({1} equipados)",
    "main_street.session_rooms": "Habitaciones Exploradas: {0}",
    "main_street.saving_progress": "Guardando progreso...",
    "main_street.thanks_playing": "¡Gracias por jugar Usurper Reborn!",
    "main_street.press_exit": "Presiona cualquier tecla para salir...",

    # Settings
    "main_street.settings_current": "Configuración actual:",
    "main_street.settings_daily_cycle": "Ciclo Diario: {0}",
    "main_street.settings_time_of_day": "Hora del Día: {0}",
    "main_street.settings_autosave": "Autoguardado: {0}",
    "main_street.settings_current_day": "Día Actual: {0}",
    "main_street.settings_options": "Opciones:",
    "main_street.settings_change_cycle": "1. Cambiar Ciclo Diario",
    "main_street.settings_time_note": "   (La hora del día avanza automáticamente según el ciclo)",
    "main_street.settings_configure_autosave": "2. Configurar Autoguardado",
    "main_street.settings_save_now": "3. Guardar Ahora",
    "main_street.settings_load_save": "4. Cargar Partida",
    "main_street.settings_delete_saves": "5. Eliminar Partidas",
    "main_street.settings_view_info": "6. Ver Información del Juego",
    "main_street.settings_force_reset": "7. Forzar Reinicio Diario",
    "main_street.settings_game_prefs": "8. Preferencias de Juego",
    "main_street.settings_back": "0. Volver",
    "main_street.settings_prompt": "Elige una opción: ",
    "main_street.settings_invalid": "Opción inválida.",

    # Preferences
    "main_street.prefs_current": "Preferencias actuales:",
    "main_street.prefs_speed_instant": "Instantánea",
    "main_street.prefs_speed_fast": "Rápida",
    "main_street.prefs_speed_normal": "Normal",
    "main_street.prefs_combat_speed": "Velocidad de Combate: {0}",
    "main_street.prefs_auto_heal": "Auto-Curación: {0}",
    "main_street.prefs_skip_intimate": "Saltar Escenas Íntimas: {0}",
    "main_street.prefs_skip_enabled": "Activado (desvanecer a negro)",
    "main_street.prefs_skip_disabled": "Desactivado (contenido completo)",
    "main_street.prefs_enabled": "Activado",
    "main_street.prefs_disabled": "Desactivado",
    "main_street.prefs_options": "Opciones:",
    "main_street.prefs_change_speed": "1. Cambiar Velocidad de Combate",
    "main_street.prefs_toggle_heal": "2. Alternar Auto-Curación",
    "main_street.prefs_toggle_intimate": "3. Alternar Escenas Íntimas",
    "main_street.prefs_back": "0. Volver",
    "main_street.prefs_prompt": "Elige una opción: ",
    "main_street.prefs_autoheal_toggled": "Auto-curación {0}.",
    "main_street.prefs_intimate_fade": "Las escenas íntimas ahora se desvanecerán a negro.",
    "main_street.prefs_intimate_fade2": "Las escenas íntimas ahora se desvanecen a negro.",
    "main_street.prefs_intimate_full": "Las escenas íntimas ahora mostrarán contenido completo.",

    # Speed
    "main_street.speed_choose": "Elige velocidad de combate:",
    "main_street.speed_normal_title": "1. Normal",
    "main_street.speed_normal_desc1": "   Velocidad estándar del juego",
    "main_street.speed_normal_desc2": "   Mejor para la primera partida",
    "main_street.speed_fast_title": "2. Rápida",
    "main_street.speed_fast_desc1": "   Animaciones y retrasos reducidos",
    "main_street.speed_fast_desc2": "   Buena para jugadores experimentados",
    "main_street.speed_instant_title": "3. Instantánea",
    "main_street.speed_instant_desc1": "   Sin retrasos de animación",
    "main_street.speed_instant_desc2": "   Máxima velocidad",
    "main_street.speed_prompt": "Elige velocidad (1-3): ",
    "main_street.speed_changed": "Velocidad de combate configurada a {0}.",

    # Cycle
    "main_street.cycle_available": "Ciclos diarios disponibles:",
    "main_street.cycle_session_title": "1. Por Sesión",
    "main_street.cycle_session_desc1": "   Un día del juego por sesión de juego",
    "main_street.cycle_session_desc2": "   Clásico estilo BBS",
    "main_street.cycle_realtime_title": "2. Tiempo Real",
    "main_street.cycle_realtime_desc1": "   El tiempo del juego sigue el reloj real",
    "main_street.cycle_realtime_desc2": "   El mundo vive mientras juegas",
    "main_street.cycle_accel4_title": "3. Acelerado (4x)",
    "main_street.cycle_accel4_desc1": "   Los días pasan 4 veces más rápido",
    "main_street.cycle_accel4_desc2": "   Buen equilibrio de progresión",
    "main_street.cycle_accel8_title": "4. Acelerado (8x)",
    "main_street.cycle_accel8_desc1": "   Los días pasan 8 veces más rápido",
    "main_street.cycle_accel8_desc2": "   Progresión más rápida",
    "main_street.cycle_accel12_title": "5. Acelerado (12x)",
    "main_street.cycle_accel12_desc1": "   Los días pasan 12 veces más rápido",
    "main_street.cycle_accel12_desc2": "   Ritmo muy rápido",
    "main_street.cycle_endless_title": "6. Sin Fin",
    "main_street.cycle_endless_desc1": "   Sin límites diarios",
    "main_street.cycle_endless_desc2": "   Juego libre sin restricciones",
    "main_street.cycle_prompt": "Elige ciclo (1-6): ",
    "main_street.cycle_changed": "Ciclo diario cambiado a {0}.",
    "main_street.cycle_desc_session": "Por Sesión",
    "main_street.cycle_desc_realtime": "Tiempo Real",
    "main_street.cycle_desc_accel4": "Acelerado (4x)",
    "main_street.cycle_desc_accel8": "Acelerado (8x)",
    "main_street.cycle_desc_accel12": "Acelerado (12x)",
    "main_street.cycle_desc_endless": "Sin Fin",
    "main_street.cycle_desc_unknown": "Desconocido",

    # Autosave
    "main_street.autosave_current": "Autoguardado actual: {0}",
    "main_street.autosave_enable": "1. Activar Autoguardado",
    "main_street.autosave_disable": "1. Desactivar Autoguardado",
    "main_street.autosave_change_interval": "2. Cambiar Intervalo (actual: cada {0} turnos)",
    "main_street.autosave_back": "0. Volver",
    "main_street.autosave_prompt": "Opción: ",
    "main_street.autosave_enabled": "Autoguardado activado.",
    "main_street.autosave_disabled": "Autoguardado desactivado.",
    "main_street.autosave_interval_prompt": "Guardar cada cuántos turnos (5-100): ",
    "main_street.autosave_interval_set": "Intervalo de autoguardado configurado a cada {0} turnos.",
    "main_street.autosave_interval_invalid": "Número inválido. El intervalo debe ser entre 5 y 100.",

    # Save/Load
    "main_street.save_available": "Partidas disponibles:",
    "main_street.save_select": "Seleccionar partida para cargar (0 para cancelar): ",
    "main_street.save_loading": "Cargando {0}...",
    "main_street.save_load_note1": "Nota: Cargar una partida reemplazará tu progreso actual.",
    "main_street.save_load_note2": "Tu partida actual se guardará automáticamente primero.",
    "main_street.delete_warning": "¡ADVERTENCIA: ¡Esto no se puede deshacer!",
    "main_street.delete_select": "Seleccionar partida para eliminar (0 para cancelar): ",
    "main_street.delete_success": "Partida eliminada exitosamente.",
    "main_street.delete_fail": "Error al eliminar la partida.",
    "main_street.delete_cancelled": "Eliminación cancelada.",
    "main_street.reset_description1": "Esto forzará un reinicio diario, restaurando:",
    "main_street.reset_description2": "  - Usos de curación, hierbas, descanso, encuentros diarios",
    "main_street.reset_completed": "¡Reinicio diario completado!",
    "main_street.reset_cancelled": "Reinicio cancelado.",

    # Mail
    "main_street.mail_checking": "Revisando correo...",
    "main_street.mail_return": "Presiona cualquier tecla para volver...",
    "main_street.help_return": "Presiona cualquier tecla para volver...",

    # Story / Health
    "main_street.story_seals_desc": "Sellos antiguos de poder, ocultos en las profundidades de la mazmorra.",
    "main_street.story_seals_collected": "Sellos Recolectados: {0}/6",
    "main_street.story_seal_found": "[✓] {0}",
    "main_street.story_seal_hidden": "[?] Sello oculto en el piso {0}",
    "main_street.story_seal_name": "Sello {0}: {1}",
    "main_street.story_gods_desc": "Seres antiguos que acechan en las profundidades de la mazmorra.",
    "main_street.story_god_defeated": "[✓] {0} - Derrotado",
    "main_street.story_god_encountered": "[!] {0} - Encontrado",
    "main_street.story_god_unknown": "[?] ??? - Piso {0}",
    "main_street.story_god_conquered": "Derrotado",
    "main_street.story_god_known": "Encontrado",
    "main_street.story_god_hidden": "Oculto",
    "main_street.story_ocean_desc": "Tu despertar espiritual a las verdades ocultas del mundo.",
    "main_street.story_awakening_level": "Nivel de Despertar: {0}",
    "main_street.story_awakening_0": "Dormido (0/7)",
    "main_street.story_awakening_1": "Agitado ({0}/7)",
    "main_street.story_awakening_2": "Despertar ({0}/7)",
    "main_street.story_awakening_3": "Consciente ({0}/7)",
    "main_street.story_awakening_4": "Iluminado ({0}/7)",
    "main_street.story_awakening_5": "Trascendente ({0}/7)",
    "main_street.story_grief_none": "Sin Duelo Activo",
    "main_street.story_grief_denial": "Negación",
    "main_street.story_grief_anger": "Ira",
    "main_street.story_grief_bargaining": "Negociación",
    "main_street.story_grief_depression": "Depresión",
    "main_street.story_grief_acceptance": "Aceptación",
    "main_street.story_grief_label": "Duelo: {0}",
    "main_street.story_combat_effects": "Efectos en Combate:",

    # Alignment
    "main_street.story_align_paragon": "Parangón",
    "main_street.story_align_noble": "Noble",
    "main_street.story_align_good": "Bueno",
    "main_street.story_align_neutral": "Neutral",
    "main_street.story_align_questionable": "Cuestionable",
    "main_street.story_align_villain": "Villano",
    "main_street.story_align_usurper": "Usurpador",
    "main_street.story_chivalry": "Caballerosidad: {0}",
    "main_street.story_dark_wanted": "Buscado",
    "main_street.story_dark_suspicious": "Sospechoso",
    "main_street.story_dark_rumored": "Rumoreado",
    "main_street.story_dark_clean": "Limpio",
    "main_street.story_darkness": "Oscuridad: {0} ({1})",

    # Story hints
    "main_street.story_hint_seals": "Pista: Busca los sellos restantes en los pisos indicados.",
    "main_street.story_hint_creator": "Pista: Has reunido los sellos. Busca al Creador en lo más profundo.",
    "main_street.story_hint_ending": "Pista: ¿Has desbloqueado todos los finales posibles?",
    "main_street.story_return": "Presiona cualquier tecla para volver...",

    # Micro events
    "main_street.micro_married_walk": "  {0} y {1} pasean juntos, tomados de la mano.",
    "main_street.micro_lovers_walk": "  {0} y {1} intercambian miradas tímidas al cruzarse.",
    "main_street.micro_fight_won": "  {0} presume de una pelea reciente, mostrando sus moretones con orgullo.",
    "main_street.micro_saw_death": "  {0} está sentado en silencio, mirando al vacío. Presenciaron algo terrible.",
    "main_street.micro_was_attacked": "  {0} cojea, con vendajes frescos — la víctima de un ataque reciente.",
    "main_street.micro_angry": "  {0} camina con el ceño fruncido, murmurando sobre alguna afrenta.",
    "main_street.micro_joyful": "  {0} sonríe mientras pasea — parece que les va bien.",
    "main_street.micro_sad": "  {0} camina cabizbajo, claramente cargando algún peso.",
    "main_street.micro_fearful": "  {0} se apresura mirando por encima del hombro nerviosamente.",
    "main_street.micro_gang_huddle": "  Miembros de {0} se reúnen en la esquina, planeando algo.",
    "main_street.micro_enemies_wary": "  {0} y {1} se miran con cautela desde lados opuestos de la calle.",
    "main_street.micro_role_defender": "  {0} está de guardia cerca de la puerta, vigilando a los transeúntes.",
    "main_street.micro_role_merchant": "  {0} regatea con un vendedor ambulante por suministros.",
    "main_street.micro_role_healer": "  {0} atiende a un ciudadano herido al borde del camino.",
    "main_street.micro_role_explorer": "  {0} revisa un mapa desgastado, planeando su próxima expedición.",

    # Time/Weather
    "main_street.time_morning": "mañanero",
    "main_street.time_afternoon": "de tarde",
    "main_street.time_evening": "vespertino",
    "main_street.time_night": "nocturno",
    "main_street.weather_clear": "despejado",
    "main_street.weather_cloudy": "nublado",
    "main_street.weather_misty": "brumoso",
    "main_street.weather_cool": "fresco",
    "main_street.weather_warm": "cálido",
    "main_street.weather_breezy": "ventoso",

    # Dev menu
    "main_street.dev_access_denied": "Acceso denegado.",
    "main_street.dev_shimmer": "El aire resplandece un momento...",
    "main_street.dev_reality": "La realidad se tuerce brevemente y luego se estabiliza.",

    # Say
    "main_street.say_prompt": "Decir: ",
    "main_street.say_you": "Dices: \"{0}\"",

    # Combat test
    "main_street.combat_test_header": "Combate de Prueba",
    "main_street.combat_test_intro": "Esto generará un monstruo de tu nivel para práctica.",
    "main_street.combat_test_weapon": "Tu arma: {0}",
    "main_street.combat_test_confirm": "¿Continuar? (S/N): ",
    "main_street.combat_test_temple": "Visita el templo si necesitas curación.",
    "main_street.combat_test_summary": "Resumen de combate:",
    "main_street.combat_test_outcome": "Resultado: {0}",
    "main_street.combat_test_victory": "Victoria",
    "main_street.combat_test_escaped": "Escapó",
    "main_street.combat_test_avoided": "Evitado",
}

missing = [k for k in en if k not in es]
added = 0
still_missing = []
for k in missing:
    if k in t:
        es[k] = t[k]
        added += 1
    else:
        still_missing.append(k)

with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, ensure_ascii=False, indent=2)

print(f"Added {added} Spanish translations. es.json now has {len(es)} keys.")
if still_missing:
    print(f"Still missing {len(still_missing)} keys:")
    for k in still_missing:
        print(f"  {k}: {en[k][:80]}")
