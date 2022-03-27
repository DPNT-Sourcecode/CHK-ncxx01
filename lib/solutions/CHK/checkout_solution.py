import collections
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
            "special_offers": [
                {
                    "quantity": 2,
                    "deal_type": "mix",
                    "free_items": [
                        {
                            "item": "B",
                            "free_quantity": 1
                        }
                    ]
                    # "deal_price": 40
                }
            ]
        }
}


def effective_offer_list(actual_qty, offer_qty_list):
    """Return only the quantities that are applicable

    :param actual_qty: Integer
    :param offer_qty_list: List

    :rtype: List
    """
    ret_list = []
    for qty in offer_qty_list:
        if qty <= actual_qty:
            ret_list.append(qty)
    return ret_list


def get_offer_based_on_quantity(offer_list, quantity):
    """Fetch specific offer based on offer quantity

    :param offer_list: List
    :param quantity: Integer

    :rtype: Dictionary
    """
    for offer in offer_list:
        if offer["quantity"] == quantity:
            return offer


def compute_price(list_items, price_dict):
    """Compute price based on list of items and price table

    :param list_items: List
    :param price_dict: Dictionary

    :rtype: Integer
    """
    total_val = 0
    set_items = set(list_items)
    for sku in set_items:
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

            if not list_unordered:
                total_val += qty * price
            else:
                list_unordered.sort()
                # descending order of offer quantity
                qty_list_ordered = list_unordered[::-1]

                qty_available = qty
                for offer_qty in qty_list_ordered:

                    if qty_available >= offer_qty:

                        eff_offer = get_offer_based_on_quantity(offers, offer_qty)
                        if eff_offer["deal_type"] == "discount":
                                
                            offer_multiple = qty_available // offer_qty
                            total_val += offer_multiple * eff_offer["deal_price"]
                            
                            offer_remainder = qty_available % offer_qty
                            qty_available = offer_remainder
                        
                        elif eff_offer["deal_type"] == "mix":
                            free_items = eff_offer["free_items"]
                            free_skus = [item["item"] for item in free_items]

                            available_for_discount = list(set_items.intersection(set(free_skus)))

                            print(available_for_discount)

                            raise Exception
                            
                            # offer_multiple = qty_available // offer_qty





                
                total_val += qty_available * price

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





