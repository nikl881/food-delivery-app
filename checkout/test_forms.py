from django.test import TestCase
from .forms import OrderForm

# form test on name input, for payment app in Orderform (Orderform / checkout)

class TestOrderform(TestCase):

    def test_can_create_an_item_with_a_name(self):
        
        form = OrderForm({'full_name': 'Create Tests'})
        self.assertFalse(form.is_valid())
    
# form test on required fields in Orderform, for payment app (Orderform / checkout)        
    
    def test_correct_message_for_missing_name(self):
        
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])