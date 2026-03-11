#!/usr/bin/env python3
"""Add TeamCornerLocation localization keys to en.json and es.json."""
import json, sys, os

LOC_DIR = os.path.join(os.path.dirname(__file__), '..', 'Localization')

NEW_KEYS = {
    # BBS menu labels (compact mode)
    "team.bbs_rankings": "Rankings",
    "team.bbs_password": "Password",
    "team.bbs_info": "Info",
    "team.bbs_examine": "Examine",
    "team.bbs_your_team": "YourTeam",
    "team.bbs_create": "Create",
    "team.bbs_join": "Join",
    "team.bbs_quit_team": "QuitTeam",
    "team.bbs_apply": "Apply",
    "team.bbs_recruit_npc": "RecruitNPC",
    "team.bbs_sack_member": "SackMember",
    "team.bbs_equip_mbr": "EquipMbr",
    "team.bbs_message": "Message",
    "team.bbs_resurrect": "Resurrect",
    "team.bbs_recruit_ally": "RecruitAlly",
    "team.bbs_team_battle": "TeamBattle",
    "team.bbs_hq": "HQ",
    "team.bbs_main_street": "MainStreet",

    # Column headers
    "team.col_num": "#",
    "team.col_name": "Name",
    "team.col_class": "Class",
    "team.col_level": "Lvl",
    "team.col_cost": "Cost",
    "team.col_wage": "Wage/Day",
    "team.col_level_full": "Level",
    "team.col_status": "Status",
    "team.col_team": "Team",
    "team.col_members": "Members",

    # Equipment slot labels
    "team.slot_main_hand": "Main Hand",
    "team.slot_off_hand": "Off Hand",
    "team.slot_head": "Head",
    "team.slot_body": "Body",
    "team.slot_arms": "Arms",
    "team.slot_hands": "Hands",
    "team.slot_legs": "Legs",
    "team.slot_feet": "Feet",
    "team.slot_cloak": "Cloak",
    "team.slot_neck": "Neck",
    "team.slot_left_ring": "Left Ring",
    "team.slot_right_ring": "Right Ring",

    # Which hand prompt (visual mode)
    "team.which_hand_visual": "Which hand? [",
    "team.which_hand_main": "]ain hand or [",
    "team.which_hand_off": "]ff hand?",

    # Stat display in examine
    "team.examine_level": "  Level: {0}  Class: {1}  Race: {2}",
    "team.examine_hp": "  HP: {0}/{1}  Mana: {2}/{3}",
    "team.examine_stats1": "  STR: {0}  DEX: {1}  AGI: {2}  CON: {3}",
    "team.examine_stats2": "  INT: {0}  WIS: {1}  CHA: {2}  DEF: {3}",

    # War history
    "team.war_win": "WIN",
    "team.war_loss": "LOSS",
    "team.war_vs": "vs {0} ",
    "team.war_record": "({0}-{1}) {2}g",

    # HQ upgrade prompt
    "team.pay_from_prompt": "  Pay from [",
    "team.pay_vault": "]ault or [",
    "team.pay_personal": "]ersonal gold? ",

    # HQ facility display
    "team.facility_lv": "Lv {0}",
    "team.facility_upgrade_cost": "[Upgrade: {0}g]",

    # News
    "team.news_war_result": "Team {0} won the war between {1} and {2}! ({3}-{4})",

    # HQ upgrade definitions
    "team.upgrade_armory": "Armory",
    "team.upgrade_armory_desc": "+5% attack per level",
    "team.upgrade_barracks": "Barracks",
    "team.upgrade_barracks_desc": "+5% defense per level",
    "team.upgrade_training": "Training Grounds",
    "team.upgrade_training_desc": "+5% XP bonus per level",
    "team.upgrade_vault": "Vault",
    "team.upgrade_vault_desc": "+50,000 vault capacity/lv",
    "team.upgrade_infirmary": "Infirmary",
    "team.upgrade_infirmary_desc": "+10% healing per level",
}

NEW_KEYS_ES = {
    "team.bbs_rankings": "Ranking",
    "team.bbs_password": "Clave",
    "team.bbs_info": "Info",
    "team.bbs_examine": "Examinar",
    "team.bbs_your_team": "TuEquipo",
    "team.bbs_create": "Crear",
    "team.bbs_join": "Unirse",
    "team.bbs_quit_team": "Salir",
    "team.bbs_apply": "Aplicar",
    "team.bbs_recruit_npc": "ReclutarNPC",
    "team.bbs_sack_member": "Despedir",
    "team.bbs_equip_mbr": "Equipar",
    "team.bbs_message": "Mensaje",
    "team.bbs_resurrect": "Resucitar",
    "team.bbs_recruit_ally": "ReclutarAliado",
    "team.bbs_team_battle": "Batalla",
    "team.bbs_hq": "CG",
    "team.bbs_main_street": "CallePrinc",

    "team.col_num": "#",
    "team.col_name": "Nombre",
    "team.col_class": "Clase",
    "team.col_level": "Niv",
    "team.col_cost": "Costo",
    "team.col_wage": "Salario/Día",
    "team.col_level_full": "Nivel",
    "team.col_status": "Estado",
    "team.col_team": "Equipo",
    "team.col_members": "Miembros",

    "team.slot_main_hand": "Mano Principal",
    "team.slot_off_hand": "Mano Secundaria",
    "team.slot_head": "Cabeza",
    "team.slot_body": "Cuerpo",
    "team.slot_arms": "Brazos",
    "team.slot_hands": "Manos",
    "team.slot_legs": "Piernas",
    "team.slot_feet": "Pies",
    "team.slot_cloak": "Capa",
    "team.slot_neck": "Cuello",
    "team.slot_left_ring": "Anillo Izq.",
    "team.slot_right_ring": "Anillo Der.",

    "team.which_hand_visual": "¿Qué mano? [",
    "team.which_hand_main": "] principal o [",
    "team.which_hand_off": "] secundaria?",

    "team.examine_level": "  Nivel: {0}  Clase: {1}  Raza: {2}",
    "team.examine_hp": "  PV: {0}/{1}  Maná: {2}/{3}",
    "team.examine_stats1": "  FUE: {0}  DES: {1}  AGI: {2}  CON: {3}",
    "team.examine_stats2": "  INT: {0}  SAB: {1}  CAR: {2}  DEF: {3}",

    "team.war_win": "VICTORIA",
    "team.war_loss": "DERROTA",
    "team.war_vs": "vs {0} ",
    "team.war_record": "({0}-{1}) {2}g",

    "team.pay_from_prompt": "  Pagar del [",
    "team.pay_vault": "]óveda o [",
    "team.pay_personal": "]oro personal? ",

    "team.facility_lv": "Nv {0}",
    "team.facility_upgrade_cost": "[Mejora: {0}g]",

    "team.news_war_result": "¡El equipo {0} ganó la guerra entre {1} y {2}! ({3}-{4})",

    "team.upgrade_armory": "Armería",
    "team.upgrade_armory_desc": "+5% ataque por nivel",
    "team.upgrade_barracks": "Barracas",
    "team.upgrade_barracks_desc": "+5% defensa por nivel",
    "team.upgrade_training": "Campo de Entrenamiento",
    "team.upgrade_training_desc": "+5% bonif. XP por nivel",
    "team.upgrade_vault": "Bóveda",
    "team.upgrade_vault_desc": "+50.000 capacidad/nv",
    "team.upgrade_infirmary": "Enfermería",
    "team.upgrade_infirmary_desc": "+10% curación por nivel",
}

def add_keys(filepath, new_keys):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    added = 0
    for key, value in new_keys.items():
        if key not in data:
            data[key] = value
            added += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return added

en_path = os.path.join(LOC_DIR, 'en.json')
es_path = os.path.join(LOC_DIR, 'es.json')

en_added = add_keys(en_path, NEW_KEYS)
es_added = add_keys(es_path, NEW_KEYS_ES)

print(f"en.json: added {en_added} keys")
print(f"es.json: added {es_added} keys")
