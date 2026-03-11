"""
Add all 447 missing base.* keys to en.json and es.json.
Keys extracted from git diff of BaseLocation.cs.
"""
import json

with open('tools/base_keys_extracted.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# Fix known bad extractions
extracted['base.also_here'] = 'Also here'

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

# Spanish translations for each key
es_translations = {
    # Activities
    "base.activity_alley_lurk": "acechando en las sombras",
    "base.activity_alley_watch": "vigilando el callejón",
    "base.activity_alley_whisper": "susurrando a una figura encapuchada",
    "base.activity_armor_chainmail": "admirando una cota de malla",
    "base.activity_armor_gauntlets": "probándose unos guanteletes",
    "base.activity_armor_shield": "inspeccionando un escudo",
    "base.activity_auction_appraise": "tasando objetos para vender",
    "base.activity_auction_bid": "pujando en una subasta",
    "base.activity_auction_browse": "revisando las subastas",
    "base.activity_castle_court": "atendiendo asuntos de la corte",
    "base.activity_castle_courtier": "hablando con un cortesano",
    "base.activity_castle_guard": "haciendo guardia cerca de la sala del trono",
    "base.activity_church_candle": "encendiendo una vela en el altar",
    "base.activity_church_pray": "rezando en silencio",
    "base.activity_church_priest": "hablando con uno de los sacerdotes",
    "base.activity_healer_potions": "revisando las pociones curativas",
    "base.activity_healer_waiting": "esperando para ver al sanador",
    "base.activity_inn_chat": "charlando con los demás clientes",
    "base.activity_inn_corner": "sentado solo en una mesa del rincón",
    "base.activity_inn_drink": "tomando una bebida en la barra",
    "base.activity_magic_crystal": "mirando en una bola de cristal",
    "base.activity_magic_potion": "oliendo una poción sospechosa",
    "base.activity_magic_scroll": "estudiando un pergamino con interés",
    "base.activity_street_business": "ocupándose de sus asuntos",
    "base.activity_street_lean": "recostado contra una pared, observando",
    "base.activity_street_stroll": "paseando por la calle",
    "base.activity_street_talk": "hablando con un amigo",
    "base.activity_weapon_blade": "examinando una espada en la pared",
    "base.activity_weapon_haggle": "regateando precios",
    "base.activity_weapon_mace": "probando el peso de una maza",
    # Afflictions
    "base.affliction_addicted": "  - Adicto (Nivel {0})",
    "base.affliction_blind": "  - Ciego",
    "base.affliction_haunted": "  - Atormentado por {0} demonio(s)",
    "base.affliction_leprosy": "  - Lepra",
    "base.affliction_measles": "  - Sarampión",
    "base.affliction_plague": "  - Plaga",
    "base.affliction_poisoned": "  - Envenenado (Nivel {0})",
    "base.affliction_smallpox": "  - Viruela",
    # Alignment
    "base.align_evil": "(Malvado)",
    "base.align_good": "(Bueno)",
    "base.align_neutral": "(Neutral)",
    # General
    "base.already_full_health": "  ¡Ya estás a plena salud!",
    "base.also_here": "También aquí",
    "base.ambush_blocked": "¡No pudiste escapar! ¡Bloquean tu camino!",
    "base.ambush_defeated": "¡Derrotaste a {0}!",
    "base.ambush_disengaged": "¡Lograste desengancharte del combate!",
    "base.ambush_escaped": "¡Logras escapar entre la multitud!",
    "base.ambush_faction_found": "¡Un miembro de {0} te ha encontrado!",
    "base.ambush_fight": "]uchar - Enfrentar al emboscador",
    "base.ambush_run": "]uir  - Intentar huir (puede fallar)",
    "base.antidote_used": "¡Bebes un antídoto — el veneno drena de tu cuerpo!",
    "base.antidotes_remaining": "Antídotos restantes: {0}/{1}",
    "base.armor_class": "  |  Clase de Armadura: ",
    "base.ask_dungeons": " Preguntar sobre las mazmorras",
    "base.ask_dungeons_to": "  Le preguntas a {0} sobre las mazmorras...",
    "base.ask_rumors": " Preguntar sobre rumores",
    "base.ask_rumors_to": "  Le preguntas a {0} si ha oído rumores interesantes...",
    "base.attack_confirm": "  ¿Estás SEGURO de que quieres atacar? (S/N): ",
    "base.attack_dangerous": "  {0} es nivel {1}. Esto parece extremadamente peligroso.",
    "base.attack_darkness": "  La oscuridad crece dentro de ti... (+{0} Oscuridad)",
    "base.attack_killed": "  ¡Has matado a {0}!",
    "base.attack_looted": "  Saqueaste {0} de oro de su cuerpo.",
    "base.attack_lunge": "  ¡Te lanzas contra {0}!",
    "base.attack_npc": " Atacar PNJ",
    "base.attack_overpowered": "  ¡{0} te domina sin esfuerzo!",
    "base.attack_reconsider": "  Reconsideras y te retiras.",
    "base.attack_remember": "  La gente recordará este acto...",
    "base.attack_teammate": "  ¡{0} es tu compañero de equipo! No puedes atacar aliados.",
    "base.attack_treacherous": "  ¡Ataque traicionero!",
    "base.available_actions": "Acciones disponibles:",
    "base.awakening_awakened": "Despierto",
    "base.awakening_aware": "Consciente",
    "base.awakening_dormant": "Dormido",
    "base.awakening_enlightened": "Iluminado",
    "base.awakening_illuminated": "Iluminado",
    "base.awakening_seeking": "Buscando",
    "base.awakening_stirring": "Agitándose",
    "base.awakening_transcendent": "Trascendente",
    "base.bank_balance": "  Banco: {0} de oro",
    "base.bc_anchor_road": "Anchor Road",
    "base.bc_armor_shop": "Tienda de Armaduras",
    "base.bc_bank": "Banco",
    "base.bc_castle": "Castillo",
    "base.bc_church": "Iglesia",
    "base.bc_dark_alley": "Callejón Oscuro",
    "base.bc_home": "Hogar",
    "base.bc_magic_shop": "Tienda Mágica",
    "base.bc_main_street": "Calle Principal",
    "base.bc_prison": "Prisión",
    "base.bc_the_inn": "La Posada",
    "base.bc_unknown": "Desconocido",
    "base.bc_weapon_shop": "Tienda de Armas",
    "base.bonuses": "Bonificaciones:",
    "base.buff_arcane_mastery": "  Maestría Arcana: +15% daño de hechizos",
    "base.buff_potion_mastery": "  Maestría en Pociones: +50% curación con pociones",
    "base.buff_tricksters_luck": "  Suerte del Embaucador: 20% prob. de bono aleatorio",
    "base.can_rest": "  (Puedes descansar después de las {0})",
    "base.castle_under_attack": "*** ¡URGENTE: CASTILLO BAJO ATAQUE! ***",
    "base.challenge_duel": " Desafiar a un duelo",
    "base.chat_with_them": " Charlar con ellos",
    "base.combat_begins": "¡Comienza el combate!",
    "base.combat_speed_set": "Velocidad de combate establecida a {0}",
    "base.compact_disabled": "  Modo Compacto DESACTIVADO",
    "base.compact_enabled": "  Modo Compacto ACTIVADO",
    "base.continue_on_way": "Continúas tu camino.",
    "base.debug_personality": "  Personalidad: {0}",
    "base.decide_not_talk": "  Decides no hablar con nadie.",
    "base.deep_conversation": " Conversación profunda",
    "base.deposed": "  ¡Has sido DEPUESTO! ¡Ya no eres el monarca!",
    "base.duel_accepted": "  ¡{0} acepta tu desafío!",
    "base.duel_challenge": "  Desafías a {0} a un duelo!",
    "base.duel_decline_busy": "  {0} dice: \\\"No ahora, estoy ocupado.\\\"",
    "base.duel_decline_strong": "  {0} se burla: \\\"Eres demasiado fuerte para mí.\\\"",
    "base.duel_decline_weak": "  {0} se ríe: \\\"¿Tú? No pierdas mi tiempo.\\\"",
    "base.duel_defeat": "  ¡Fuiste derrotado por {0}!",
    "base.duel_honorably": "  ¡Peleaste honorablemente! (+1 Caballería)",
    "base.duel_victory": "  ¡Venciste a {0} en duelo!",
    "base.dungeon_get_stronger": "  \\\"Hazte más fuerte antes de ir más profundo.\\\"",
    "base.dungeon_good_luck": "  \\\"¡Buena suerte ahí abajo!\\\"",
    "base.dungeon_not_ready": "  \\\"No estás listo para eso todavía. Mantente en los pisos superiores.\\\"",
    "base.dungeon_upper_ok": "  \\\"Los pisos superiores deberían estar bien para ti.\\\"",
    "base.dungeon_watch_floor": "  \\\"Cuidado con el piso {0}... cosas terribles acechan allí.\\\"",
    "base.dungeon_you_experienced": "  \\\"Eres bastante experimentado. Los pisos profundos te esperan.\\\"",
    "base.effect_magic_ac": "  CA Mágica +{0}",
    "base.effect_raging": "  ¡EN FURIA!",
    "base.effect_smite": "  Castigo Divino: {0} carga(s)",
    "base.effect_stoneskin": "  Piel de Piedra: {0} golpe(s) restante(s)",
    "base.equipment_totals": "  Totales del Equipo:",
    "base.establishment_closed": "  ¡Este establecimiento ha sido CERRADO por decreto real!",
    "base.establishment_closed_by": "  Por orden de {0} {1}, esta ubicación está prohibida.",
    "base.exits": "Salidas:",
    "base.experience_label": "  Experiencia: ",
    "base.faction_crown_bonus": "  Corona: +{0}% daño, +{1}% defensa",
    "base.faction_faith_bonus": "  Fe: +{0}% curación, +{1}% defensa",
    "base.faction_shadows_bonus": "  Sombras: +{0}% crítico, +{1}% evasión",
    "base.fame_label": "Fama: ",
    "base.fame_legendary": "Legendario",
    "base.fame_nobody": "Nadie",
    "base.fame_notable": "Notable",
    "base.fame_renowned": "Renombrado",
    "base.fame_unknown": "Desconocido",
    "base.fame_well_known": "Bien Conocido",
    "base.fatigue_exhausted_penalty": "AGOTADO: -{0}% daño/defensa/XP",
    "base.fatigue_label": "Fatiga: {0}/100",
    "base.fatigue_tired_penalty": "CANSADO: -{0}% daño/defensa",
    "base.female": "Femenino",
    "base.for_help": "  Escribe ? para ayuda y /comandos para ver todos los comandos.",
    "base.gear_inspect_who": "¿Inspeccionar equipo de quién?",
    "base.gear_selection_prompt": "Selecciona (# o nombre, 0 para ti): ",
    "base.god_have_artifact": "  ¡Tienes el artefacto!",
    "base.god_seek_artifact": "  Busca el artefacto en el piso de la mazmorra {0}",
    "base.gods_allied": "Aliados",
    "base.gods_awaiting": "Esperando",
    "base.gods_defeated": "Derrotados",
    "base.gods_none": "Ninguno",
    "base.gods_saved": "Salvados",
    "base.gold_on_hand": "  Oro en mano: {0}",
    "base.guard_challenging": "¡está desafiando a {0} {1} por el trono!",
    "base.guard_crown_remembers": "La corona recordará esta traición.",
    "base.guard_honor_bound": "Como Guardia Real, ¡estás obligado por honor a defender la corona!",
    "base.guard_level": "Nivel",
    "base.guard_loyalty_dropped": "¡Tu lealtad ha caído a {0}%!",
    "base.guard_loyalty_unquestioned": "¡Tu lealtad a la corona no será cuestionada!",
    "base.guard_messenger": "¡Un mensajero te busca con noticias urgentes!",
    "base.guard_rush_castle": "¡Corres hacia el castillo, espada en mano!",
    "base.guard_rush_prompt": "¿Correr a defender el trono? (S/N): ",
    "base.guard_rush_question": "¿Correrás al castillo para ayudar en la defensa?",
    "base.guard_stripped": "*** ¡Has sido DESPOJADO de tu cargo de Guardia Real! ***",
    "base.guard_turn_away": "Te alejas de tu deber...",
}

# For keys not manually translated, auto-generate placeholder
# (We'll add the English value and mark es for manual review later)
added_en = 0
added_es = 0

for key, value in extracted.items():
    if key not in en:
        en[key] = value
        added_en += 1
    if key not in es:
        if key in es_translations:
            es[key] = es_translations[key]
        else:
            # Use English as fallback (the system falls back anyway)
            es[key] = value
        added_es += 1

with open('Localization/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, ensure_ascii=False, indent=2)

print(f"Added {added_en} en keys, {added_es} es keys")
print(f"Total: en={len(en)}, es={len(es)}")
print(f"(Spanish translations provided for {len(es_translations)} keys, rest use English fallback)")
