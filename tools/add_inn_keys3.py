import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

new_en = {
    # PlayHighLowDice remaining
    "inn.tie_returned": "It's a tie! Your bet is returned.",
    "inn.you_win": "You win! +{0} gold!",
    "inn.double_nothing": "Double or nothing? Current pot: {0}g ",
    "inn.max_double_down": "Maximum double-downs reached. Collecting winnings!",
    "inn.you_lose": "You lose! -{0} gold.",
    "inn.gold_remaining": "Gold remaining: {0}",

    # PlaySkullAndBones
    "inn.sb_rules1": "Rules: Draw bone tiles to reach 21 without going over.",
    "inn.sb_rules2": "Face tiles (Skull, Crown, Sword) = 10. Dealer stands on 17.",
    "inn.not_enough_gold_bet": "You don't have that much gold!",
    "inn.invalid_bet": "Invalid bet.",
    "inn.sb_your_tiles": "Your tiles: {0} = {1}",
    "inn.sb_natural21": "SKULL & BONES! Natural 21!",
    "inn.sb_hit": "[H]",
    "inn.sb_or": "it or ",
    "inn.sb_stand": "[S]",
    "inn.sb_drew": "You drew: {0} ({1}) \u2014 Total: {2}",
    "inn.sb_bust": "BUST! You went over 21.",
    "inn.sb_bust_lose": "You lose {0} gold. Remaining: {1}",
    "inn.sb_dealer_turn": "Dealer's turn...",
    "inn.sb_dealer_total": "Dealer's total: {0}",
    "inn.sb_dealer_busts": "Dealer busts! You win {0} gold!",
    "inn.sb_beats_dealer": "Skull & Bones beats dealer! You win {0} gold!",
    "inn.sb_you_beat": "You beat the dealer! You win {0} gold!",
    "inn.sb_push": "Push! Bet returned.",
    "inn.sb_dealer_wins": "Dealer wins. You lose {0} gold.",

    # PlayArmWrestling
    "inn.aw_enough_today": "\"You've had enough for today, friend. Come back tomorrow.\"",
    "inn.aw_no_interested": "No one seems interested in arm wrestling right now.",
    "inn.aw_challenger_slams": "{0} (Level {1}, STR {2}) slams their",
    "inn.aw_challenger_grins": "elbow on the table and grins at you.",
    "inn.aw_wager_challenge": "\"{0} gold says I can put you down.\"",
    "inn.aw_need_gold": "You need {0} gold to accept the challenge.",
    "inn.aw_accept_challenge": "Accept the challenge? ({0}g) ",
    "inn.aw_back_away": "You back away from the table.",
    "inn.aw_clasp_hands": "You clasp hands...",
    "inn.aw_three_two_one": "Three... two... one... GO!",
    "inn.aw_you_slam": "You slam {0}'s arm to the table!",
    "inn.aw_you_win": "You win {0} gold!",
    "inn.aw_they_slam": "{0} forces your arm down with a grunt!",
    "inn.aw_you_lose": "You lose {0} gold.",
    "inn.aw_draw": "Neither of you can budge! It's a draw.",
    "inn.aw_matches_today": "Arm wrestling matches today: {0}/{1}",

    # RentRoom
    "inn.rent_need_gold": "You need {0} gold for a room. You have {1} on hand and {2} in the bank.",
    "inn.rent_room_cost": "\n  Room cost: {0} gold",
    "inn.rent_healed_logout": "  You will be healed fully and logged out safely.",
    "inn.rent_sleep_bonus": "  Sleeping at the Inn grants +50% ATK/DEF if you're attacked.\n",
    "inn.rent_guards_hired": "  Guards hired: {0}/{1}",
    "inn.rent_done_hiring": " Done hiring",
    "inn.rent_gold_summary": "\n  Your gold: {0} (bank: {1})  |  Room: {2}  |  Guards: {3}  |  Total: {4}",
    "inn.rent_cant_afford_guard": "  You can't afford that guard.",
    "inn.rent_hired_guard": "  Hired {0}! (HP: {1})",
    "inn.rent_total_cost": "\n  Total cost: {0} gold (Room: {1} + Guards: {2})",
    "inn.rent_confirm": "  Rent this room and log out? (y/N): ",
    "inn.rent_cancelled": "  You decide not to rent a room.",
    "inn.rent_cant_afford": "  You can't afford this!",
    "inn.rent_bank_withdraw": "  ({0}g withdrawn from your bank account)",
    "inn.rent_shadow_fades": "  The Blessing of Shadows fades as you rest...",
    "inn.rent_room_desc1": "\n  The innkeeper shows you to a private room upstairs.",
    "inn.rent_room_desc2": "  You lock the heavy door and collapse into a real bed.",
    "inn.rent_guards_position": "  Your {0} guard(s) take position outside your door.",
    "inn.rent_deep_sleep": "\n  You drift into a deep, protected sleep... (logging out)",

    # AttackInnSleeper
    "inn.atk_not_available": "Not available.",
    "inn.atk_no_sleepers": "No vulnerable sleepers at the Inn.",
    "inn.atk_sleeping_guests": "Inn \u2014 Sleeping Guests",
    "inn.atk_who_attack": "\nWho do you attack? (number or name, blank to cancel): ",
    "inn.atk_no_such_sleeper": "No such sleeper.",

    # AttackInnSleepingNPC
    "inn.atk_no_longer_here": "They are no longer here.",
    "inn.atk_pick_lock": "\n  You pick the lock to {0}'s room at the Inn...\n",
    "inn.atk_steal_gold": "You rifle through their belongings and steal {0} gold!",
    "inn.atk_leave_body": "\nYou leave {0}'s body in their room.",
    "inn.atk_faction_plummet": "Your standing with {0} has plummeted! (-250)",
    "inn.atk_fought_off": "{0} fought you off \u2014 the Inn's thick walls muffled the struggle!",

    # AttackInnSleepingPlayer
    "inn.atk_cant_load": "Could not load their data.",
    "inn.atk_sneak_toward": "\n  You sneak toward {0}'s room at the Inn...\n",
    "inn.atk_guard_blocks": "\n  A {0} blocks your path!",
    "inn.atk_cut_down_guard": "  You cut down the {0}!",
    "inn.atk_guard_repels": "  The {0} drives you back! Attack failed!",
    "inn.atk_reach_target": "\n  You reach {0}...\n",
    "inn.atk_steal_item": "You also take their {0}!",
    "inn.atk_player_fought_off": "{0} fought you off even in their sleep!",
}

new_es = {
    "inn.tie_returned": "\u00a1Empate! Tu apuesta es devuelta.",
    "inn.you_win": "\u00a1Ganaste! +{0} oro!",
    "inn.double_nothing": "\u00bfDoble o nada? Bote actual: {0}g ",
    "inn.max_double_down": "\u00a1M\u00e1ximo de doblajes alcanzado. \u00a1Cobrando ganancias!",
    "inn.you_lose": "\u00a1Perdiste! -{0} oro.",
    "inn.gold_remaining": "Oro restante: {0}",

    "inn.sb_rules1": "Reglas: Saca fichas de hueso para llegar a 21 sin pasarte.",
    "inn.sb_rules2": "Fichas de cara (Calavera, Corona, Espada) = 10. El dealer se planta en 17.",
    "inn.not_enough_gold_bet": "\u00a1No tienes tanto oro!",
    "inn.invalid_bet": "Apuesta inv\u00e1lida.",
    "inn.sb_your_tiles": "Tus fichas: {0} = {1}",
    "inn.sb_natural21": "\u00a1CALAVERA Y HUESOS! \u00a121 natural!",
    "inn.sb_hit": "[P]",
    "inn.sb_or": "edir o ",
    "inn.sb_stand": "[Q]",
    "inn.sb_drew": "Sacaste: {0} ({1}) \u2014 Total: {2}",
    "inn.sb_bust": "\u00a1PASASTE! Te pasaste de 21.",
    "inn.sb_bust_lose": "Pierdes {0} oro. Restante: {1}",
    "inn.sb_dealer_turn": "Turno del dealer...",
    "inn.sb_dealer_total": "Total del dealer: {0}",
    "inn.sb_dealer_busts": "\u00a1El dealer se pasa! \u00a1Ganas {0} oro!",
    "inn.sb_beats_dealer": "\u00a1Calavera y Huesos vence al dealer! \u00a1Ganas {0} oro!",
    "inn.sb_you_beat": "\u00a1Vences al dealer! \u00a1Ganas {0} oro!",
    "inn.sb_push": "\u00a1Empate! Apuesta devuelta.",
    "inn.sb_dealer_wins": "El dealer gana. Pierdes {0} oro.",

    "inn.aw_enough_today": "\"Ya tuviste suficiente por hoy, amigo. Vuelve ma\u00f1ana.\"",
    "inn.aw_no_interested": "Nadie parece interesado en luchar de brazos ahora.",
    "inn.aw_challenger_slams": "{0} (Nivel {1}, FUE {2}) golpea la mesa",
    "inn.aw_challenger_grins": "con el codo y te sonr\u00ede.",
    "inn.aw_wager_challenge": "\"{0} oro dice que te puedo vencer.\"",
    "inn.aw_need_gold": "Necesitas {0} oro para aceptar el desaf\u00edo.",
    "inn.aw_accept_challenge": "\u00bfAceptar el desaf\u00edo? ({0}g) ",
    "inn.aw_back_away": "Te alejas de la mesa.",
    "inn.aw_clasp_hands": "Se toman de las manos...",
    "inn.aw_three_two_one": "\u00a1Tres... dos... uno... YA!",
    "inn.aw_you_slam": "\u00a1Aplastas el brazo de {0} contra la mesa!",
    "inn.aw_you_win": "\u00a1Ganas {0} oro!",
    "inn.aw_they_slam": "\u00a1{0} fuerza tu brazo hacia abajo con un gruñido!",
    "inn.aw_you_lose": "Pierdes {0} oro.",
    "inn.aw_draw": "\u00a1Ninguno cede! Es un empate.",
    "inn.aw_matches_today": "Luchas de brazo hoy: {0}/{1}",

    "inn.rent_need_gold": "Necesitas {0} oro para una habitaci\u00f3n. Tienes {1} en mano y {2} en el banco.",
    "inn.rent_room_cost": "\n  Costo de habitaci\u00f3n: {0} oro",
    "inn.rent_healed_logout": "  Ser\u00e1s curado completamente y desconectado de forma segura.",
    "inn.rent_sleep_bonus": "  Dormir en la posada otorga +50% ATK/DEF si te atacan.\n",
    "inn.rent_guards_hired": "  Guardias contratados: {0}/{1}",
    "inn.rent_done_hiring": " Terminar contrataci\u00f3n",
    "inn.rent_gold_summary": "\n  Tu oro: {0} (banco: {1})  |  Habitaci\u00f3n: {2}  |  Guardias: {3}  |  Total: {4}",
    "inn.rent_cant_afford_guard": "  No puedes pagar ese guardia.",
    "inn.rent_hired_guard": "  \u00a1Contratado {0}! (PV: {1})",
    "inn.rent_total_cost": "\n  Costo total: {0} oro (Habitaci\u00f3n: {1} + Guardias: {2})",
    "inn.rent_confirm": "  \u00bfAlquilar esta habitaci\u00f3n y desconectarse? (s/N): ",
    "inn.rent_cancelled": "  Decides no alquilar una habitaci\u00f3n.",
    "inn.rent_cant_afford": "  \u00a1No puedes pagarlo!",
    "inn.rent_bank_withdraw": "  ({0}g retirados de tu cuenta bancaria)",
    "inn.rent_shadow_fades": "  La Bendici\u00f3n de las Sombras se desvanece al descansar...",
    "inn.rent_room_desc1": "\n  El posadero te muestra una habitaci\u00f3n privada arriba.",
    "inn.rent_room_desc2": "  Cierras la pesada puerta y te desplomas en una cama real.",
    "inn.rent_guards_position": "  Tus {0} guardia(s) toman posici\u00f3n fuera de tu puerta.",
    "inn.rent_deep_sleep": "\n  Te sumerges en un sue\u00f1o profundo y protegido... (desconectando)",

    "inn.atk_not_available": "No disponible.",
    "inn.atk_no_sleepers": "No hay durmientes vulnerables en la posada.",
    "inn.atk_sleeping_guests": "Posada \u2014 Hu\u00e9spedes Dormidos",
    "inn.atk_who_attack": "\n\u00bfA qui\u00e9n atacas? (n\u00famero o nombre, vac\u00edo para cancelar): ",
    "inn.atk_no_such_sleeper": "No existe ese durmiente.",

    "inn.atk_no_longer_here": "Ya no est\u00e1n aqu\u00ed.",
    "inn.atk_pick_lock": "\n  Fuerzas la cerradura de la habitaci\u00f3n de {0} en la posada...\n",
    "inn.atk_steal_gold": "\u00a1Registras sus pertenencias y robas {0} oro!",
    "inn.atk_leave_body": "\nDejas el cuerpo de {0} en su habitaci\u00f3n.",
    "inn.atk_faction_plummet": "\u00a1Tu reputaci\u00f3n con {0} se ha desplomado! (-250)",
    "inn.atk_fought_off": "\u00a1{0} te rechaz\u00f3 \u2014 las gruesas paredes de la posada amortiguaron la lucha!",

    "inn.atk_cant_load": "No se pudieron cargar sus datos.",
    "inn.atk_sneak_toward": "\n  Te acercas sigilosamente a la habitaci\u00f3n de {0} en la posada...\n",
    "inn.atk_guard_blocks": "\n  \u00a1Un {0} bloquea tu camino!",
    "inn.atk_cut_down_guard": "  \u00a1Derribas al {0}!",
    "inn.atk_guard_repels": "  \u00a1El {0} te rechaza! \u00a1Ataque fallido!",
    "inn.atk_reach_target": "\n  Llegas hasta {0}...\n",
    "inn.atk_steal_item": "\u00a1Tambi\u00e9n tomas su {0}!",
    "inn.atk_player_fought_off": "\u00a1{0} te rechaz\u00f3 incluso dormido!",
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
