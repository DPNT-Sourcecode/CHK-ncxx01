"""
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""

PRICING_TABLE = {
    "A": {
            "price": 50, 
            "special_offers": {
                "quantity": 3,
                "deal_price": 130
            }
        },
    "B": {
            "price": 30, 
            "special_offers": {
                "quantity": 2,
                "deal_price": 45
            }
        },
    "C": {"price": 20},
    "D": {"price": 15}
}

def compute_price(list_items, price_dict):
    """Compute price based on list of items and price table

    :param list_items: List
    :param price_dict: Dictionary

    :rtype: Integer
    """
    total_val = 0
    for sku in set(list_items):
        if sku not in price_dict.keys():
            return -1

        qty = list_items.count(sku)
        print(qty)
        price = price_dict[sku]["price"]
        print(price)

        offer = price_dict[sku].get("special_offers")
        if not offer:
            total_val += qty * price
        else:
            print("offer")
            offer_qty = offer["quantity"]

            if qty < offer_qty:
                total_val += qty * price
            else:
                offer_multiple = offer_qty // qty
                offer_remainder = offer_qty % qty
                total_val += offer_multiple * offer["deal_price"]
                total_val += price * offer_remainder

    return total_val


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """Get checkout value

    :param skus: String

    :rtype: Int
    """
    return compute_price(
        [char for char in skus.strip()], 
        PRICING_TABLE)
