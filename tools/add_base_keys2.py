import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

new_en = {
    # Trade confirm/send
    "base.trade_send_prefix": "Send ",
    "base.trade_items_count": "{0} item(s) ",
    "base.trade_gold_amount": "+ {0} gold ",
    "base.trade_to_confirm": "to {0}? (Y/N): ",
    "base.trade_package_sent": "Package sent to {0}!",

    # Bounty format strings
    "base.bounty_amount_prompt": "  Bounty amount (min {0}, you have {1}g): ",
    "base.bounty_min_amount": "  Minimum bounty is {0} gold.",
    "base.bounty_placed": "\n  Bounty of {0} gold placed on {1}!",
    "base.bounty_total": "  {0} active bounties totaling {1} gold!",
    "base.bounty_entry": "  {0} gold - posted by {1}",
    "base.bounty_target_entry": "  {0} - {1} gold",

    # Auction: Grimjaw dialogue
    "base.auction_slow_day": "\"Slow day. You selling or just wasting my time?\"",
    "base.auction_few_things": "\"Got a few things worth looking at. Browse the board.\"",
    "base.auction_plenty": "\"Plenty of goods today! Step up, step up!\"",
    "base.auction_and_others": " and {0} others",
    "base.auction_talk": " Talk ({0})",

    # Auction item details format
    "base.auction_type": "  Type: {0}    Value: {1}g",
    "base.auction_req_level": "\n  You must be level {0}+ to use this item. (You are level {1})",
    "base.auction_need_more": "\n  You need {0} more gold to buy this.",
    "base.auction_buy_confirm": "\n  Buy for {0} gold? (Y/N): ",
    "base.auction_purchased": "\n  Purchased {0} for {1} gold!",
    "base.auction_purchased_error": "\n  Purchased item but couldn't add to inventory. Gold was deducted.",
    "base.auction_requires_level": "  Requires Level {0}+",
    "base.auction_requires_str": "  Requires {0} Strength",

    # Sell on auction
    "base.auction_fee_label": "  Fee: ",
    "base.auction_fee_detail": "  ({0}% base + {1}% tax)",
    "base.auction_need_fee": "\n  You need {0} gold for the listing fee. You have {1}.",
    "base.auction_list_confirm": "\n  List {0} for {1}g ({2}, fee: {3}g)? (Y/N): ",
    "base.auction_listed": "\n  {0} listed for {1} gold! Fee: {2}g. Expires in {3}.",

    # My listings
    "base.auction_gold_awaiting": "\n  Gold awaiting collection: {0}g ({1} item{2})",
    "base.auction_expired_count": "  Expired items to collect: {0} item{1}",
    "base.auction_sold_uncollected": "SOLD - COLLECT GOLD",
    "base.auction_sold_collected": "SOLD - COLLECTED",
    "base.auction_expired_collect": "EXPIRED - COLLECT ITEM",
    "base.auction_expired_collected": "EXPIRED - COLLECTED",
    "base.auction_gold_collected": "\n  Collected {0} gold from auction sales!",
    "base.auction_items_collected": "\n  Collected {0} expired item(s) back to your inventory.",
    "base.auction_collected_back": "  Collected {0} back to your inventory.",
}

new_es = {
    "base.trade_send_prefix": "Enviar ",
    "base.trade_items_count": "{0} objeto(s) ",
    "base.trade_gold_amount": "+ {0} oro ",
    "base.trade_to_confirm": "a {0}? (S/N): ",
    "base.trade_package_sent": "\u00a1Paquete enviado a {0}!",

    "base.bounty_amount_prompt": "  Cantidad de recompensa (m\u00edn {0}, tienes {1}g): ",
    "base.bounty_min_amount": "  La recompensa m\u00ednima es {0} oro.",
    "base.bounty_placed": "\n  \u00a1Recompensa de {0} oro puesta sobre {1}!",
    "base.bounty_total": "  \u00a1{0} recompensas activas totalizando {1} oro!",
    "base.bounty_entry": "  {0} oro - publicado por {1}",
    "base.bounty_target_entry": "  {0} - {1} oro",

    "base.auction_slow_day": "\"D\u00eda lento. \u00bfVendes o solo pierdes mi tiempo?\"",
    "base.auction_few_things": "\"Hay algunas cosas que vale la pena ver. Revisa el tabl\u00f3n.\"",
    "base.auction_plenty": "\"\u00a1Muchos productos hoy! \u00a1Pasen, pasen!\"",
    "base.auction_and_others": " y {0} m\u00e1s",
    "base.auction_talk": " Hablar ({0})",

    "base.auction_type": "  Tipo: {0}    Valor: {1}g",
    "base.auction_req_level": "\n  Debes ser nivel {0}+ para usar este objeto. (Eres nivel {1})",
    "base.auction_need_more": "\n  Necesitas {0} m\u00e1s oro para comprar esto.",
    "base.auction_buy_confirm": "\n  \u00bfComprar por {0} oro? (S/N): ",
    "base.auction_purchased": "\n  \u00a1Comprado {0} por {1} oro!",
    "base.auction_purchased_error": "\n  Objeto comprado pero no se pudo a\u00f1adir al inventario. El oro fue deducido.",
    "base.auction_requires_level": "  Requiere Nivel {0}+",
    "base.auction_requires_str": "  Requiere {0} Fuerza",

    "base.auction_fee_label": "  Tarifa: ",
    "base.auction_fee_detail": "  ({0}% base + {1}% impuesto)",
    "base.auction_need_fee": "\n  Necesitas {0} oro para la tarifa de listado. Tienes {1}.",
    "base.auction_list_confirm": "\n  \u00bfListar {0} por {1}g ({2}, tarifa: {3}g)? (S/N): ",
    "base.auction_listed": "\n  \u00a1{0} listado por {1} oro! Tarifa: {2}g. Expira en {3}.",

    "base.auction_gold_awaiting": "\n  Oro esperando recolecci\u00f3n: {0}g ({1} objeto{2})",
    "base.auction_expired_count": "  Objetos expirados por recoger: {0} objeto{1}",
    "base.auction_sold_uncollected": "VENDIDO - COBRAR ORO",
    "base.auction_sold_collected": "VENDIDO - COBRADO",
    "base.auction_expired_collect": "EXPIRADO - RECOGER OBJETO",
    "base.auction_expired_collected": "EXPIRADO - RECOGIDO",
    "base.auction_gold_collected": "\n  \u00a1Cobrado {0} oro de ventas de subasta!",
    "base.auction_items_collected": "\n  \u00a1Recogidos {0} objeto(s) expirado(s) a tu inventario!",
    "base.auction_collected_back": "  \u00a1Recogido {0} de vuelta a tu inventario!",
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
