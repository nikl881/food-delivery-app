from django.test import TestCase
from .order import OrderForm

# form test on name input, for payment app in Orderform (Orderform / checkout)

class TestPaymentForm(TestCase):

    def test_can_create_an_item_with_a_name(self):
        
        form = OrderForm({'name': 'This is a Tests'})
        self.assertTrue(form.is_valid())
    
        
# form test on required fields in Orderform, for payment app (Orderform / checkout)        
    
    def test_correct_message_for_missing_name(self):
        
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This is a field required field!'])