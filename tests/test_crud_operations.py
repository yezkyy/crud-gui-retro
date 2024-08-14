import unittest
from app import crud_operations

class TestCrudOperations(unittest.TestCase):

    def setUp(self):
        crud_operations.create_table()

    def test_create_item(self):
        crud_operations.create_item("Test Item", "Test Description")
        items = crud_operations.read_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][1], "Test Item")

    def test_update_item(self):
        crud_operations.create_item("Old Name", "Old Description")
        items = crud_operations.read_items()
        item_id = items[0][0]
        crud_operations.update_item(item_id, "New Name", "New Description")
        updated_items = crud_operations.read_items()
        self.assertEqual(updated_items[0][1], "New Name")

    def test_delete_item(self):
        crud_operations.create_item("Test Item", "Test Description")
        items = crud_operations.read_items()
        item_id = items[0][0]
        crud_operations.delete_item(item_id)
        items_after_deletion = crud_operations.read_items()
        self.assertEqual(len(items_after_deletion), 0)

if __name__ == '__main__':
    unittest.main()