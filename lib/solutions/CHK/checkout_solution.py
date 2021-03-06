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
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
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
                }
            ]
        },
    "F": {
            "price": 10,
            "special_offers": [
                {
                    "quantity": 2,
                    "deal_type": "self",
                    "free_items": [
                        {
                            "free_quantity": 1
                        }
                    ]
                }
            ]
        },
    "G": {"price": 20},
    "H": {
            "price": 10,
            "special_offers": [
                {
                    "quantity": 5,
                    "deal_type": "discount",
                    "deal_price": 45
                },
                {
                    "quantity": 10,
                    "deal_type": "discount",
                    "deal_price": 80
                }
            ]
        }, 
    "I": {"price": 35},
    "J": {"price": 60},
    "K": {
            "price": 70,
            "special_offers": [
                {
                    "quantity": 2,
                    "deal_type": "discount",
                    "deal_price": 120
                }
            ]
        }, 
    "L": {"price": 90},
    "M": {"price": 15},
    "N": {
            "price": 40,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "mix",
                    "free_items": [
                        {
                            "item": "M",
                            "free_quantity": 1
                        }
                    ]
                }
            ]
        },
    "O": {"price": 10},
    "P": {
            "price": 50,
            "special_offers": [
                {
                    "quantity": 5,
                    "deal_type": "discount",
                    "deal_price": 200
                }
            ]
        },
    "Q": {
            "price": 30,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 80
                }
            ]
        },
    "R": {
            "price": 50,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "mix",
                    "free_items": [
                        {
                            "item": "Q",
                            "free_quantity": 1
                        }
                    ]
                }
            ]
        },
    "S": {
            "price": 20,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 45
                }
            ]
        },
    "T": {
            "price": 20,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 45
                }
            ]
        },
    "U": {
            "price": 40,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "self",
                    "free_items": [
                        {
                            "free_quantity": 1
                        }
                    ]
                }
            ]
        },
    "V": {
            "price": 50,
            "special_offers": [
                {
                    "quantity": 2,
                    "deal_type": "discount",
                    "deal_price": 90
                },
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 130
                }
            ]
        },
    "W": {"price": 20},
    "X": {
            "price": 17,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 45
                }
            ]
        },
    "Y": {
            "price": 20,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 45
                }
            ]
        },
    "Z": {
            "price": 21,
            "special_offers": [
                {
                    "quantity": 3,
                    "deal_type": "discount",
                    "deal_price": 45
                }
            ]
        }
}

ALL_THE_SAME = {
    ("S", "T", "X", "Y", "Z"): {
        "min_quantity": 3,
        # highest value
        # "replacement": "Z"
    }
}

def resolve_all_the_same(skus):
    """Resolve sku string with buy any x
    
    :param skus: String

    :rtype: String
    """
    eff_skus = skus
    count_track_skus = [sk for sk in skus]
    for k in ALL_THE_SAME.keys():
        qty_count = 0

        sk_dict = {}

        min_qty = ALL_THE_SAME[k]["min_quantity"]
        len_candidate_str = ""
        for sku in skus:
            if sku in k:
                sk_dict[sku] = PRICING_TABLE[sku]["price"]
                len_candidate_str = f"{len_candidate_str}{sku}"
                qty_count += 1

        if qty_count >= min_qty:
            
            print("lencr", len_candidate_str)

            repl_str = ""
            ats_skus = ""
            # ats_skus = "".join([sk for sk in sk_dict.keys()])
            for sk in sk_dict.keys():
                ats_skus = f"{ats_skus}{sk}"
                eff_skus = eff_skus.replace(sk, "")
            
            print(ats_skus)
            print("eff ----", eff_skus, "----")

            len_str = len(len_candidate_str)
            print(len_str)
            max_sku =  max(sk_dict, key=sk_dict.get)

            offer_multiple = len_str // min_qty
            print("multiple", offer_multiple)
            for i in range(offer_multiple):
                for j in range(min_qty):
                    repl_str = f"{repl_str}{max_sku}"
            print(repl_str)
            
            offer_remainder = len_str % min_qty
            print("rem", offer_remainder)
            for x in range(offer_remainder):
                min_sku =  min(sk_dict, key=sk_dict.get)
                print(min_sku)
                min_sku_count = count_track_skus.count(min_sku)
                if min_sku_count > 0:
                    repl_str = f"{repl_str}{min_sku}"
                    # print(count_track_skus)
                    count_track_skus.remove(min_sku)
                    print(count_track_skus)
                    if count_track_skus.count(min_sku) == 0:
                        del sk_dict[min_sku]
                else:
                    # print(sk_dict)
                    del sk_dict[min_sku]
                    # print(sk_dict)

            # print(min_sku, max_sku, ats_skus, min_qty, len_str)
            # print(offer_multiple, offer_remainder, repl_str)
            if repl_str:
                eff_skus = f"{eff_skus}{repl_str}"
            print(eff_skus, "\n")
            # raise Exception

    return eff_skus

    

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


def get_free_item_obj(free_items, sku):
    """Fetch free item obj 

    :param free_items: List
    :param sku: String

    :rtype: Dictionary
    """
    for item in free_items:
        if item["item"] == sku:
            return item


def compute_price(list_items, price_dict):
    """Compute price based on list of items and price table

    :param list_items: List
    :param price_dict: Dictionary

    :rtype: Integer
    """
    total_val = 0
    set_items = set(list_items)
    free_val = 0
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

                        elif eff_offer["deal_type"] == "self":
                            total_val += qty_available * price
                            free_factor = eff_offer["free_items"][0]["free_quantity"]
                            discount = 0
                            if qty_available > offer_qty:
                                offer_multiple = qty_available // (offer_qty + free_factor)
                                
                                for i in range(offer_multiple):
                                    discount += free_factor * price
                                
                            total_val = total_val - discount
                            qty_available = 0
                        
                        elif eff_offer["deal_type"] == "mix":
                            offer_multiple = qty_available // offer_qty

                            total_val += qty_available * price
                            qty_available = 0

                            free_items = eff_offer["free_items"]
                            free_skus = [item["item"] for item in free_items]

                            available_for_discount = list(
                                set_items.intersection(set(free_skus)))

                            if available_for_discount:
                                for sk in available_for_discount:
                                    sk_item = get_free_item_obj(free_items, sk)
                                    sk_price = PRICING_TABLE[sk]["price"]
                                    sk_offers = PRICING_TABLE[sk].get("special_offers")
                                    sk_count = list_items.count(sk)

                                    sk_disc_count = sk_item["free_quantity"]
                                    # non discounted price
                                    total_sk_price = sk_price * sk_count

                                    sk_count_track = sk_count
                                    for i in range(offer_multiple):
                                        if sk_count_track >= sk_disc_count:
                                            free_val += sk_price * sk_disc_count
                                            sk_count_track = sk_count_track - 1

                                    if sk_offers:
                                        # dealing with only 1 offer, 
                                        sk_offer = sk_offers[0]
                                        sk_offer_qty = sk_offer["quantity"]
                                        sk_offer_price = sk_offer["deal_price"]
                                        sk_offer_multiple = sk_count // sk_offer_qty
                                        sk_offer_remainder = sk_count % sk_offer_qty

                                        eff_sk_price = (sk_offer_multiple * sk_offer_price) + \
                                            (sk_offer_remainder * sk_price)
                                        
                                        sk_offer_savings = total_sk_price - eff_sk_price

                                        if sk_offer_savings > free_val:
                                            free_val = 0
                                        else:
                                            remaining_offer_multiple = sk_count_track // sk_offer_qty
                                            if remaining_offer_multiple > 0:
                                                print(remaining_offer_multiple)
                                                remaining_sk_price = sk_count_track * sk_price
                                                remaining_disc_price = remaining_offer_multiple * sk_offer_price
                                                free_val += remaining_sk_price - remaining_disc_price

                                            free_val = free_val - sk_offer_savings
                                    

                total_val += qty_available * price
    total_val = total_val - free_val
    return total_val


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """Get checkout value

    :param skus: String

    :rtype: Int
    """
    eff_skus = resolve_all_the_same(skus.strip())
    # print("\n")
    # print(eff_skus)

    return compute_price(
        [char for char in eff_skus], 
        PRICING_TABLE)
