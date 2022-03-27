"""
Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+

"""

PRICING_TABLE = {
    "A": {
            "price": 50, 
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 130
                },
                {
                    "quantity": 5,
                    "deal_type": "discount",
                    "deal_price": 200
                }
            ]
        },
    "B": {
            "price": 30, 
            "special_offers": [
                {
                    "quantity": 2,
                    "deal_type": "discount",
                    "deal_price": 45
                }
            ]
        },
    "C": {"price": 20},
    "D": {"price": 15},
    "E": {
            "price": 40,
            # "special_offers": [
            #     {
            #         "quantity": 2,
            #         "deal_type": "mix",
            #         "free_items": [
            #             {
            #                 "item": "B"
            #                 "free_quantity": 1
            #             }
            #         ]
            #         "deal_price": 40
            #     }
            # ]
        }
}


def effective_offer_list(actual_qty, qty_list):
    """Return only the quantities that are applicable

    :param actual_qty: Integer
    :param qty_list: List

    :rtype: List
    """
    ret_list = []
    for qty in qty_list:
        if qty <= actual_qty:
            ret_list.append(qty)
    return ret_list

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

        # quantity in order
        qty = list_items.count(sku)
        # standard price
        price = price_dict[sku]["price"]
        # list of offers (if any)
        offers = price_dict[sku].get("special_offers")
        if not offers:
            total_val += qty * price
        else:
            offer_qty_list = []
            for offer in offers:
                offer_qty_list.append(offer["quantity"])
            list_unordered = effective_offer_list(qty, offer_qty_list)
            print(list_unordered)
            if not list_unordered:
                total_val += qty * price
            else:
                list_unordered.sort()
                # descending order of offer quantity
                qty_list_ordered = list_unordered[::-1]

                qty_available = qty
                for offer_qty in qty_list_ordered:

                    print("available ", qty_available)
                    print("offer qty ", offer_qty)
 
                    if qty_available < offer_qty:
                        total_val += qty_available * price
                    else:
                        offer_multiple = qty_available // offer_qty
                        print("offer multiple ", offer_multiple)
                        print("deal price", offer["deal_price"])
                        total_val += offer_multiple * offer["deal_price"]
                        
                        offer_remainder = qty_available % offer_qty
                        qty_available = offer_remainder 
                        print(total_val)  
                        

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