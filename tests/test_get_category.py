import unittest
from unittest.mock import patch
from entity.category import Category
from services.get_category import get_all_categories


# Create a mock for the database connection and cursor
class MockCursor:
    def execute(self, query):
        pass

    def fetchall(self):
        return [(1, 'Category 1', 'Description 1', 101), (2, 'Category 2', 'Description 2', 102)]

class MockConnection:
    def cursor(self):
        return MockCursor()

def open_connection():
    return MockConnection()

class TestGetAllCategories(unittest.TestCase):

    @patch('helpers.connection.open_connection', side_effect=open_connection)
    def test_get_all_categories(self, mock_open_connection):
        # Call the function to get categories
        categories = get_all_categories()

        # Check that the result is a list
        self.assertIsInstance(categories, list)

        # Check that each item in the list is an instance of Category
        for category in categories:
            self.assertIsInstance(category, Category)

        # You can add more specific assertions based on your expected data
        # For example:
        self.assertEqual(len(categories), 5)
        self.assertEqual(categories[0].categoria, 'Category 1')
        self.assertEqual(categories[0].descricao, 'Description 1')
        self.assertEqual(categories[0].idtipocategoria, 101)

if __name__ == '__main__':
    unittest.main()
