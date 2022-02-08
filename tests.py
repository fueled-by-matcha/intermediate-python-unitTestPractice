# Write your code below:
import surfshop
import unittest

class TestingSuite(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()
  
  @unittest.skip(surfshop.TooManyBoardsError)
  def test_add_surfboards(self):
    for i in range(2,5):
      with unittest.subTest(i = i):
        self.assertEqual(self.cart.add_surfboards(i), 'Successfully added {} surfboard to cart!'.format(str(i)), 'Did not add right amount of surfboards')
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
  
  #@unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.assertTrue(self.cart.apply_locals_discount, "Discount false")

unittest.main()
