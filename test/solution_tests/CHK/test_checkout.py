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
        # checking the value actually matches (not just what the function computes)
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665

    def test_self_discount_offer_checkout(self):
        """Test checkout for buy 2 get 1 free"""
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("FFFFFFF") == 50

    def test_self_discount_offer_checkout_more_qty(self):
        """Test checkout for buy 3 get 1 free"""
        assert checkout_solution.checkout("UUU") == 120
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("UUUUU") == 160
        assert checkout_solution.checkout("UUUUUU") == 200
        assert checkout_solution.checkout("UUUUUUU") == 240
        assert checkout_solution.checkout("UUUUUUUU") == 240
        assert checkout_solution.checkout("UUUUUUUUU") == 280

    def test_mix_and_discount_offer_checkout_more_qty(self):
        """Test checkout for buy 3 x get 1 y free, and y offers"""
        assert checkout_solution.checkout("NNNM") == 120

    def test_offer_all_the_same(self):
        """Test checkout for buy 3 x get 1 y free, and y offers"""
        # assert checkout_solution.checkout("SXYZNNNM") == 182
        assert checkout_solution.checkout("SXYYZ") == 182

