from django.test import TestCase
from .models import Product

# will test models 

class TestModelProduct(TestCase):

    def test_done_defaults_to_False(self):
        test_Product = Product(name="Create a Test")
        self.assertEqual(test_Product.name, "Create a Test")
        
        test_Product = Product(description="some description")
        self.assertEqual(test_Product.description, "some description")
        
        test_Product = Product(price="4.00")
        self.assertEqual(test_Product.price, "4.00")
        
        test_Product = Product(image="")
        self.assertEqual(test_Product.image, "")

