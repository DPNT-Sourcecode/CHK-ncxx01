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


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """Get checkout value

    :param skus: String (comma separated string of skus)

    :rtype: Int
    """
    separated_items = skus.split(",")
    items = []
    for item in separated_items:
        # handling non uniform separation via commas (hence, the strip)
        stripped_item = item.strip()
        if stripped_item not in PRICING_TABLE.keys():
            return -1
        else:
            items.append(stripped_item)
    
    total_val = 0
    for sku in set(items):
        qty = items.count(sku)
        price = PRICING_TABLE[sku]["price"]

        offer = PRICING_TABLE[sku].get("special_offers")

        if not offer:
            total_val += qty * price


    return total_val