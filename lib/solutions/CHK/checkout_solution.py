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
    "A": {"price": 50, "special_offers": ""},
    "B": {"price": 30, "special_offers": ""},
    "C": {"price": 20},
    "D": {"price": 15}
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()

