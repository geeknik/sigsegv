"""
Fix issues found in fourth localization audit pass:
1. Remove single-quote wrapping from 15 values (both en/es)
2. Add empty magic shop curse dialogue values
3. Fix 61 placeholder mismatches between en/es
   - Category A: ES dropped placeholders that EN has (code passes args) -> add placeholders to ES
   - Category B: ES added placeholders that EN doesn't have (code passes 0 args) -> remove from ES
"""
import json, re

# === 1. SINGLE-QUOTE WRAPPED VALUES ===
# These keys have values like "'text'" — remove outer single quotes
single_quote_keys = [
    "shop.enchant_level_req",
    "shop.max_enchantments",
    "shop.ocean_flavor",
    "puzzle.wave_quote",
    "magic_shop.curse_intro_2",
    "magic_shop.curse_fortunate",
    "magic_shop.curse_no_gold",
    "magic_shop.curse_remains",
    "magic_shop.curse_aftermath_1",
    "magic_shop.curse_aftermath_2",
    "magic_shop.old_enchant_intro",
    "magic_shop.old_cursed_enchant",
    "magic_shop.old_remove_first",
    "dungeon.riddle_foolish_mortal",
    "dungeon.story_purging_4",
]

# === 2. EMPTY VALUES — add content ===
en_empty_fixes = {
    "magic_shop.curse_intro_3": "\"Let me examine you closely...\"",
    "magic_shop.curse_scene_5": "The dark energy dissipates into nothingness.",
    "magic_shop.curse_aftermath_3": "\"May fortune favor you in your travels.\"",
}

es_empty_fixes = {
    "magic_shop.curse_intro_3": "\"Dejame examinarte de cerca...\"",
    "magic_shop.curse_scene_5": "La energia oscura se disipa en la nada.",
    "magic_shop.curse_aftermath_3": "\"Que la fortuna te favorezca en tus viajes.\"",
}

# === 3. PLACEHOLDER MISMATCHES ===

# Category A: EN has placeholders, ES dropped them. Fix ES to include placeholders.
es_placeholder_fixes = {
    # EN: "Removed {0} from slot {1}." / ES was: "Ranura {0} borrada."
    "ability.removed_from_slot": "{0} eliminado de la ranura {1}.",
    # EN: "You already possess {0}." / ES was: "Ya posees este artefacto."
    "artifact.already_possess": "Ya posees {0}.",
    # EN: "  {0}: You have the artifact. Return to their floor."
    "base.god_have_artifact": "  {0}: Tienes el artefacto. Regresa a su piso.",
    # EN: "{0} allied/defeated/saved/awaiting rescue"
    "base.gods_allied": "{0} aliados",
    "base.gods_awaiting": "{0} esperando rescate",
    "base.gods_defeated": "{0} derrotados",
    "base.gods_saved": "{0} salvados",
    # EN: "Path to redemption: {0}"
    "betrayal.path_to_redemption": "Camino a la redencion: {0}",
    # EN: "City Tax ({0}% to {1})"
    "city.city_tax_to": "Impuesto ({0}% para {1})",
    # EN: "You find {0} healing potion{1} hidden inside!"
    "feature.find_potions": "Encuentras {0} pocion{1} de curacion escondida!",
    # EN: "+{0} poison vial{1}! (Total: {2})"
    "feature.poison_vials": "+{0} frasco{1} de veneno! (Total: {2})",
    # EN: "  Unlocked: {0}/{1} ({2}%)"
    "main_street.achieve_unlocked": "  Desbloqueados: {0}/{1} ({2}%)",
    # EN: "     Unlocked: {0}   +{1} pts"
    "main_street.achieve_unlocked_date": "     Desbloqueado: {0}   +{1} pts",
    # EN: "ADVENTURERS ({0} active) - Page {1}/{2}"
    "main_street.citizens_adventurers": "AVENTUREROS ({0} activos) - Pagina {1}/{2}",
    # EN: "FALLEN ({0}) - Page {1}/{2}"
    "main_street.citizens_fallen": "CAIDOS ({0}) - Pagina {1}/{2}",
    # EN: "The {0} brandishes a {1}!"
    "main_street.combat_test_weapon": "El {0} blande un {1}!",
    # EN: "Select save file to delete (1-{0}) or 0 to cancel: "
    "main_street.delete_select": "Seleccionar partida para eliminar (1-{0}) o 0 para cancelar: ",
    # EN: "{0} carries a confident swagger. Looks like they bested {1} recently."
    "main_street.micro_fight_won": "  {0} presume de una pelea reciente contra {1}.",
    # EN: "Select save file (1-{0}) or 0 to cancel: "
    "main_street.save_select": "Seleccionar partida (1-{0}) o 0 para cancelar: ",
    # EN: "  Time of Day: {0} ({1})"
    "main_street.settings_time_of_day": "  Hora del Dia: {0} ({1})",
    # EN: "  Chivalry: {0}  -  {1}"
    "main_street.story_chivalry": "  Caballerosidad: {0}  -  {1}",
    # EN: "    Combat Effects: {0}"
    "main_street.story_combat_effects": "    Efectos en Combate: {0}",
    # EN: "    {0} Seal of {1} - {2}"
    "main_street.story_seal_name": "    {0} Sello de {1} - {2}",
    # EN: "You have already found the {0}."
    "seals.already_found": "Ya has encontrado {0}.",
}

# Category B: ES added placeholders that EN doesn't have.
# Code passes 0 args for these, so {0} appears literally. Fix ES to match EN pattern (no placeholders).
es_remove_placeholder_fixes = {
    # These are all "label: " style — code appends value separately
    "base.attack_teammate": "  No puedes atacar a tu propio companero de equipo!",
    "base.bank_balance": "  Saldo Bancario: ",
    "base.can_rest": "  Puedes descansar por la noche.",
    "base.debug_personality": "(DEBUG) Ver rasgos de personalidad",
    "base.duel_decline_busy": "  \"No ahora, estoy ocupado.\"",
    "base.duel_decline_strong": "  \"Eres demasiado fuerte para mi.\"",
    "base.duel_decline_weak": "  \"Tu? No pierdas mi tiempo.\"",
    "base.dungeon_watch_floor": "  \"Cuidado con las profundidades... cosas terribles acechan alli.\"",
    "base.faction_crown_bonus": "  * 10% descuento en todas las tiendas",
    "base.faction_faith_bonus": "  * 25% descuento en servicios de curacion",
    "base.faction_shadows_bonus": "  * 20% mejores precios al vender objetos",
    "base.fatigue_exhausted_penalty": " — -10% dano/defensa/XP",
    "base.fatigue_label": "  Fatiga: ",
    "base.fatigue_tired_penalty": " — -5% dano/defensa",
    "base.gold_on_hand": "  Oro en Mano: ",
    "city.total": "Total",
    "main_street.attack_confirm": "  Estas seguro? (S/N)",
    # EN: " - Level {0} {1}" (2 args) / ES: "{0}. {1} (Nivel {2} {3})" (4 args) — fix to match EN's 2 args
    "main_street.attack_npc_info": " - Nivel {0} {1}",
    "main_street.autosave_change_interval": "3. Cambiar intervalo de autoguardado",
    "main_street.micro_gang_huddle": "Miembros de una pandilla se reunen en la esquina, planeando algo.",
    "main_street.quit_inn_desc": "  Posada: sueno protegido con +50% ATQ/DEF si te atacan.",
    # Session stats — EN uses "label: " then code appends value. Match that pattern.
    "main_street.session_damage": "  Dano Infligido:   ",
    "main_street.session_duration": "  Duracion de la Sesion: ",
    "main_street.session_gold": "  Oro Ganado:    ",
    "main_street.session_items": "  Objetos Encontrados:   ",
    "main_street.session_levels": "  Niveles Ganados:  ",
    "main_street.session_monsters": "  Monstruos Derrotados: ",
    "main_street.session_rooms": "  Habitaciones Exploradas: ",
    "main_street.session_xp": "  XP Ganada:      ",
    # Awakening stages — EN is just descriptive text, no args
    "main_street.story_awakening_1": "Agitacion - Algo profundo dentro comienza a moverse",
    "main_street.story_awakening_2": "Ondas - Sientes conexiones entre todas las cosas",
    "main_street.story_awakening_3": "Corrientes - Las profundidades te llaman con susurros antiguos",
    "main_street.story_awakening_4": "Profundidades - Comprendes el dolor del oceano",
    "main_street.story_awakening_5": "Iluminado - Eres uno con la marea eterna",
    # God/seal status — EN is just a status word, no args
    "main_street.story_god_defeated": "DERROTADO",
    "main_street.story_god_encountered": "Encontrado",
    "main_street.story_god_unknown": "Desconocido",
    "main_street.story_seal_found": "Encontrado",
    "main_street.story_seal_hidden": "Oculto en las profundidades...",
    "seals.progress": "Progreso de los Sellos",
    # Ability requires — EN: "Requires Lv{0}" (1 arg), ES had 2 args
    "ability.requires_lv": "Requiere Nv{0}",
}

# inn.items_equipped: EN has {0} and {1} (2 unique), ES used {1} three times
# EN: "Items Equipped: {0}/{1}" — 2 args
# ES should match
es_inn_fix = {
    "inn.items_equipped": "Objetos Equipados: {0}/{1}",
}

# ============ APPLY ALL FIXES ============

for lang in ['en', 'es']:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    added = 0

    # 1. Strip single quotes from wrapped values
    for key in single_quote_keys:
        if key in data:
            val = data[key]
            if val.startswith("'") and val.endswith("'") and len(val) > 2:
                data[key] = val[1:-1]
                fixed += 1

    # 2. Add empty values
    if lang == 'en':
        for key, value in en_empty_fixes.items():
            if key in data and data[key] == "":
                data[key] = value
                fixed += 1
            elif key not in data:
                data[key] = value
                added += 1
    else:
        for key, value in es_empty_fixes.items():
            if key in data and data[key] == "":
                data[key] = value
                fixed += 1
            elif key not in data:
                data[key] = value
                added += 1

    # 3. Placeholder fixes (ES only)
    if lang == 'es':
        for key, value in es_placeholder_fixes.items():
            if key in data and data[key] != value:
                data[key] = value
                fixed += 1

        for key, value in es_remove_placeholder_fixes.items():
            if key in data and data[key] != value:
                data[key] = value
                fixed += 1

        for key, value in es_inn_fix.items():
            if key in data and data[key] != value:
                data[key] = value
                fixed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed} values, added {added} new keys")
