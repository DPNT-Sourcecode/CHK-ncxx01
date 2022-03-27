from solutions.CHK import checkout_solution


PRICES = checkout_solution.PRICING_TABLE


class TestHello():
    """Class to test sum_solution"""

    def test_invalid_item_list(self):
        """Return -1 if item not in price list table"""
        assert checkout_solution.checkout("F, G, A") == -1

    def test_no_offer_checkout(self):
        """Total checkout value for items with no offers"""
        sku_list = ["C", "D", "D"]
        assert checkout_solution.checkout("".join(sku_list)) == \
            checkout_solution.compute_price(sku_list, PRICES)

    def test_offer_checkout(self):
        """Total checkout value for items with special offers"""
        sku_list = ["C", "B", "B"]
        assert checkout_solution.checkout("".join(sku_list)) == \
            checkout_solution.compute_price(sku_list, PRICES)

