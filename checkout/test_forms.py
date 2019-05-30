from django.test import TestCase
from .forms import OrderForm

# form test on name input, for payment app in Orderform (Orderform / checkout)

class TestOrderform(TestCase):

        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'full_name': 'Create Tests'})
        self.assertTrue(form.is_valid())
        
        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'phone_number': '12345678'})
        self.assertTrue(form.is_valid())
         
        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'country': 'country'})
        self.assertTrue(form.is_valid())
        
        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'postcode': 'AAAA1234'})
        self.assertTrue(form.is_valid())
        
        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'town_or_city': 'City name'})
        self.assertTrue(form.is_valid())
        
        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'street_address1': 'Adres here'})
        self.assertTrue(form.is_valid())
        
        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'street_address2': 'Adres2 here'})
        self.assertTrue(form.is_valid())
        
        def test_can_create_an_item_with_just_a_name(self):
        form = OrderForm({'country': 'country'})
        self.assertTrue(form.is_valid())
    
# form test on required fields in Orderform, for payment app (Orderform / checkout)        
    
    def test_correct_message_for_missing_name(self):
        
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])