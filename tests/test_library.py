import unittest
from models import Library, Book
import os
import json


class TestLibrary(unittest.TestCase):
    def setUp(self):
        # Создаем временный файл для тестов
        self.test_file = "test_storage.json"
        with open(self.test_file, "w") as f:
            json.dump([], f)

        self.library = Library(storage_path=self.test_file)

    def tearDown(self):
        # Удаляем тестовый файл после выполнения тестов
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        book = Book(book_id=1, title="Test Book", author="Author", year=2020)
        self.library.add_book(book)

        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_add_book_duplicate(self):
        book1 = Book(book_id=1, title="Test Book", author="Author", year=2020)
        book2 = Book(book_id=1, title="Duplicate Test Book", author="Author", year=2021)
        self.library.add_book(book1)

        with self.assertRaises(ValueError):
            self.library.add_book(book2)

    def test_delete_book(self):
        book = Book(book_id=1, title="Test Book", author="Author", year=2020)
        self.library.add_book(book)
        self.library.delete_book(1)

        self.assertEqual(len(self.library.books), 0)

    def test_is_id_exist(self):
        book = Book(book_id=1, title="Test Book", author="Author", year=2020)
        self.library.add_book(book)

        self.assertTrue(self.library.is_id_exist(1))
        self.assertFalse(self.library.is_id_exist(2))

    def test_find_books_by_title(self):
        book1 = Book(book_id=1, title="Test Book 1", author="Author A", year=2020)
        book2 = Book(book_id=2, title="Test Book 2", author="Author B", year=2021)
        self.library.add_book(book1)
        self.library.add_book(book2)

        found_books = self.library.find_books_by_title("Test Book 1")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, "Test Book 1")

    def test_find_books_by_author(self):
        book1 = Book(book_id=1, title="Test Book 1", author="Author A", year=2020)
        book2 = Book(book_id=2, title="Test Book 2", author="Author A", year=2021)
        self.library.add_book(book1)
        self.library.add_book(book2)

        found_books = self.library.find_books_by_author("Author A")
        self.assertEqual(len(found_books), 2)

    def test_find_books_by_year(self):
        book1 = Book(book_id=1, title="Test Book 1", author="Author A", year=2020)
        book2 = Book(book_id=2, title="Test Book 2", author="Author B", year=2021)
        self.library.add_book(book1)
        self.library.add_book(book2)

        found_books = self.library.find_books_by_year(2020)
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].year, 2020)

    def test_get_all_books(self):
        book1 = Book(book_id=1, title="Test Book 1", author="Author A", year=2020)
        book2 = Book(book_id=2, title="Test Book 2", author="Author B", year=2021)
        self.library.add_book(book1)
        self.library.add_book(book2)

        all_books = self.library.get_all_books()
        self.assertEqual(len(all_books), 2)

    def test_generate_id(self):
        book1 = Book(book_id=1, title="Test Book 1", author="Author A", year=2020)
        book2 = Book(book_id=2, title="Test Book 2", author="Author B", year=2021)
        self.library.add_book(book1)
        self.library.add_book(book2)

        new_id = self.library.generate_id()
        self.assertEqual(new_id, 3)

    def test_change_book_status(self):
        book = Book(book_id=1, title="Test Book", author="Author", year=2020, status="in stock")
        self.library.add_book(book)

        self.library.change_book_status_by_id(1, "issued")
        self.assertEqual(self.library.books[0].status, "issued")

    def test_change_status_invalid_book(self):
        with self.assertRaises(ValueError):
            self.library.change_book_status_by_id(99, "issued")


if __name__ == "__main__":
    unittest.main()
