from django.test import TestCase
from .products import Item

# test models
class TestItemModel(TestCase):

    def test_done_defaults_to_False(self):
        item = Item(name="Create Test")
        item.save()
        self.assertEqual(item.name, "Create Test")
        self.assertFalse(item.done)
    
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Create Test", done=True)
        item.save()
        self.assertEqual(item.name, "Create  Test")
        self.assertTrue(item.done)