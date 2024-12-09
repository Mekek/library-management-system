import unittest
from datetime import datetime
from models import Library, Book


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.library = Library(storage_path="test_storage.json")
        book = Book(book_id=1, title="Sample Book", author="Author", year=2020)
        self.library.add_book(book)

    def tearDown(self):
        # Удаляем временные данные
        import os
        if os.path.exists("test_storage.json"):
            os.remove("test_storage.json")

    def test_is_year_valid(self):
        current_year = datetime.now().year

        self.assertTrue(self.library.is_year_valid(str(current_year)))
        self.assertTrue(self.library.is_year_valid(str(current_year - 1)))
        self.assertFalse(self.library.is_year_valid(str(current_year + 1)))
        self.assertFalse(self.library.is_year_valid("invalid_year"))

    def test_is_id_valid(self):
        self.assertTrue(self.library.is_id_valid(1))
        self.assertFalse(self.library.is_id_valid(99))
        self.assertFalse(self.library.is_id_valid(-1))
        self.assertFalse(self.library.is_id_valid("invalid_id"))


if __name__ == "__main__":
    unittest.main()
