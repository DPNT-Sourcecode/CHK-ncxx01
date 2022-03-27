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
    item_qty = {}
    for item in separated_items:
        stripped_item = item.strip()
        if stripped_item not in PRICING_TABLE.keys():
            return -1
        else:
            effective_item_list.
    



    # effective_sku_list = [s.strip() for s in separated_items]


    return 0