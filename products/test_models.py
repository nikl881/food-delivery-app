from django.test import TestCase
from .models import Product

# testing models 

class TestModelProduct(TestCase):

    def test_done_defaults_to_False(self):
        Product = Product(name="Create a Test")
        Product.save()
        self.assertEqual(Product.name, "Create a Test")
        self.assertFalse(Product.done)
    
    def test_can_create_an_item_with_a_name_and_status(self):
        Product = Product(name="Create a Test", done=True)
        Product.save()
        self.assertEqual(Product.name, "Create a Test")
        self.assertTrue(Product.done)