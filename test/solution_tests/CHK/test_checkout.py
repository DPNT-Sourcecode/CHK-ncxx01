from solutions.CHK import checkout_solution


PRICES = checkout_solution.PRICING_TABLE


class TestHello():
    """Class to test sum_solution"""

    def test_invalid_item_list(self):
        """Return -1 if item not in price list table"""
        # checking the value actually matches (not just what the function computes)
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

    def test_offer_checkout_complex(self):
        """Total checkout value for items with special offers type"""
        sku_list = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"]
        # checking the value actually matches (not just what the function computes)
        assert checkout_solution.checkout("".join(sku_list)) == 580

    def test_offer_checkout_not_enough_for_offer(self):
        """Total checkout value for items with special offers type but not enough quantity for offer"""
        sku_list = ["A", "A", "E"]
        # checking the value actually matches (not just what the function computes)
        assert checkout_solution.checkout("".join(sku_list)) == 140

    def test_mix_no_offer_checkout(self):
        """Test checkout for buy 2 x get 1 y free (but no y)"""
        sku_list = ["A", "A", "E", "E"]
        # checking the value actually matches (not just what the function computes)
        assert checkout_solution.checkout("".join(sku_list)) == 180

    def test_mix_offer_checkout(self):
        """Test checkout for buy 2 x get 1 y free"""
        sku_list = ["A", "A", "E", "E", "B", "B"]
        # checking the value actually matches (not just what the function computes)
        assert checkout_solution.checkout("".join(sku_list)) == 210

    def test_mix_and_discount_offer_checkout(self):
        """Test checkout for buy 2 x get 1 y free, and y offers"""
        sku_list = ["A", "A", "E", "E", "B", "B", "B"]
        # checking the value actually matches (not just what the function computes)
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455

"""
Some requests have failed (2/40). Here are some of them:
 - {"method":"checkout","params":["AAAAAEEBAAABB"],"id":"CHK_R2_040"}, expected: 455, got: 470
 - {"method":"checkout","params":["ABCDECBAABCABBAAAEEAA"],"id":"CHK_R2_001"}, expected: 665, got: 695
"""