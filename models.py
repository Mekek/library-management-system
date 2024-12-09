import json
from datetime import datetime

class Book:
    """
    Класс для представления книги в библиотеке.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги (по умолчанию "in stock").
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "in stock"):
        """
        Инициализирует объект книги.

        Параметры:
            book_id (int): Уникальный идентификатор книги.
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            status (str, опционально): Статус книги. По умолчанию 'in stock'.
        """
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library:
    """
    Класс для управления библиотекой книг.

    Атрибуты:
        storage_path (str): Путь к файлу, в котором хранится информация о книгах.
        books (list[Book]): Список объектов книг, загруженных из файла хранения.
    """
    def __init__(self, storage_path: str):
        """
        Инициализирует библиотеку.

        Параметры:
            storage_path (str): Путь к файлу для хранения данных о книгах.
        """
        self.storage_path = storage_path
        self.books = self.load_books_from_storage()

    def load_books_from_storage(self) -> list[Book]:
        """
        Загружает список книг из файла хранилища.

        Возвращает:
            list[Book]: Список книг, загруженных из файла.

        Исключения:
            FileNotFoundError: Если файл хранения не существует.
            json.JSONDecodeError: Если файл хранения поврежден или имеет некорректный формат.
        """
        try:
            with open(self.storage_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                books = [Book(book["id"], book["title"], book["author"], book["year"], book["status"]) for book in data]
                return books
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
            return []

    def save_books_to_storage(self):
        """
        Сохраняет список книг в файл хранения.

        Возвращает:
            None
        """
        with open(self.storage_path, "w", encoding="utf-8") as file:
            data = [{
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "status": book.status
            } for book in self.books]
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_book(self, book: Book):
        """
        Добавляет новую книгу в библиотеку.

        Параметры:
            book (Book): Объект книги для добавления.

        Исключения:
            ValueError: Если книга с таким ID уже существует в библиотеке.
        """
        if self.is_id_exist(book.id):
            raise ValueError(f"Книга с ID {book.id} уже существует в библиотеке.")
        
        self.books.append(book)
        self.save_books_to_storage()
        print(f"Книга '{book.title}' добавлена с ID {book.id}")

    def delete_book(self, book_id: int):
        """
        Удаляет книгу из библиотеки по ее ID.

        Параметры:
            book_id (int): ID книги, которую необходимо удалить.

        Возвращает:
            None

        Печатает:
            Сообщение о результате (удалена книга или не найдена).
        """
        book_to_delete = None
        for book in self.books:
            if int(book.id) == book_id:
                book_to_delete = book
                break
        if book_to_delete:
            self.books.remove(book_to_delete)
            self.save_books_to_storage()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def is_id_exist(self, book_id: int) -> bool:
        """
        Проверяет, существует ли книга с указанным ID.

        Параметры:
            book_id (int): ID книги для проверки.

        Возвращает:
            bool: True, если книга с таким ID существует, иначе False.
        """
        return any(book.id == book_id for book in self.books)

    def find_book_by_id(self, book_id: int) -> Book:
        """
        Ищет книгу по ID.

        Параметры:
            book_id (int): ID книги для поиска.

        Возвращает:
            Book: Объект книги, если найдена, иначе None.
        """
        for book in self.books:
            if book.id == int(book_id):
                return book
        return None

    def find_books_by_title(self, title: str) -> list[Book]:
        """
        Ищет книги по названию.

        Параметры:
            title (str): Название книги для поиска.

        Возвращает:
            list[Book]: Список книг, которые содержат указанное название.
        """
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author: str) -> list[Book]:
        """
        Ищет книги по автору.

        Параметры:
            author (str): Имя или фамилия автора для поиска.

        Возвращает:
            list[Book]: Список книг указанного автора.
        """
        return [book for book in self.books if author.lower() in book.author.lower()]

    def find_books_by_year(self, year: int) -> list[Book]:
        """
        Ищет книги по году издания.

        Параметры:
            year (int): Год издания книги для поиска.

        Возвращает:
            list[Book]: Список книг, выпущенных в указанный год.
        """
        return [book for book in self.books if book.year == year]

    def get_all_books(self) -> list[Book]:
        """
        Возвращает все книги в библиотеке.

        Возвращает:
            list[Book]: Список всех книг в библиотеке.
        """
        return self.books

    def change_book_status_by_id(self, book_id: int, new_status: str):
        """
        Изменяет статус книги по ее ID.

        Параметры:
            book_id (int): ID книги для изменения статуса.
            new_status (str): Новый статус книги ('in stock' или 'issued').

        Исключения:
            ValueError: Если новый статус некорректен или книга с таким ID не найдена.
        """
        if new_status not in {"in stock", "issued"} or not self.is_id_valid(book_id):
            raise ValueError(f"Некорректный статус: '{new_status}'. Допустимые значения: 'in stock', 'issued'.")
        
        book = self.find_book_by_id(book_id)
        if book:
            book.status = new_status
            self.save_books_to_storage()
            print(f"Статус книги с ID {book_id} изменен на {new_status}.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def generate_id(self) -> int:
        """
        Генерирует уникальный ID для новой книги.

        Возвращает:
            int: Новый уникальный ID.
        """
        used_ids = [book.id for book in self.books]
        acceptable_id = 1
        while acceptable_id in used_ids:
            acceptable_id += 1
        return acceptable_id

    def is_year_valid(self, year):
        """
        Проверяет, является ли год издания корректным.

        Параметры:
            year (int): Год издания книги.

        Возвращает:
            bool: True, если год корректен, иначе False.
        
        Печатает:
            Сообщение об ошибке, если год больше текущего.
        """
        try:
            year = int(year)
            if year <= datetime.now().year:
                return True
            else:
                raise ValueError
        except ValueError:
            print(f"Некорректный год. Год не должен быть больше, чем {datetime.now().year}.")
            return False

    def is_id_valid(self, id):
        """
        Проверяет, является ли ID книги корректным.

        Параметры:
            id (int): ID книги.

        Возвращает:
            bool: True, если ID корректен, иначе False.

        Печатает:
            Сообщение об ошибке, если ID некорректен.
        """
        try:
            id = int(id)
            if id <= 0:
                print("ID должен быть больше 0.")
                raise ValueError
            if self.is_id_exist(id):
                return True
            else:
                print("Книги с таким ID нет в библиотеке.")
                raise ValueError
        except ValueError:
            print("Некорректный ID.")
            return False
