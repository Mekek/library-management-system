from datetime import datetime

from config import STORAGE_PATH
from models import Book, Library


def main():
    while True:
        library = Library(storage_path=STORAGE_PATH)
        print()
        print("Введите номер желаемого действия:")
        print("1. Добавить книгу в библиотеку")
        print("2. Удалить книгу из библиотеки")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Завершить работу")
        print()

        while True:
            command = input("Введите номер желаемого действия: ")

            try:
                command = int(command)
                if 1 <= command <= 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Некорректный ввод. Введите число от 1 до 6.")

        if command == 1:
            id = library.generate_id()
            title = input("Введите название книги: ")
            author = input("Введите инициалы автора книги: ")
            
            while True:
                year = input("Введите год написания книги: ")

                if library.is_year_valid(year):
                    break

            new_book = Book(id, title, author, int(year))
            library.add_book(new_book)
            print("Книга добвалена в бибилиотеку.")

        if command == 2:
            while True:
                id = input("Введите ID книги для удаления: ")

                if library.is_id_valid(id):
                    break
                
            library.delete_book(int(id))

        if command == 3:
            print("Приступим к поиску книги. Выберите, что вы знаете о книге:")
            print("1. Название")
            print("2. Автор")
            print("3. Год написания")

            while True:
                param = input("Введите номер известного вам параметра книги: ")
                try:
                    param = int(param)
                    if 1 <= param <= 3:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Некорректный ввод. Введите число от 1 до 3.")

            if param == 1:
                title = input("Введите название книги: ")
                found_books = library.find_books_by_title(title)
            elif param == 2:
                author = input("Введите автора: ")
                found_books = library.find_books_by_author(author)
            else:
                while True:
                    year = input("Введите год написания книги: ")

                    if library.is_year_valid(year):
                        break
                found_books = library.find_books_by_year(int(year))

            print("Найденные книги:")
            print()
            for found_book in found_books:
                print("ID: ", found_book.id)
                print("Название: ", found_book.title)
                print("Автор: ", found_book.author)
                print("Год: ", found_book.year)
                print()

        if command == 4:
            print("Все книги:")
            print()
            books = library.get_all_books()
            for book in books:
                print("ID: ", book.id)
                print("Название: ", book.title)
                print("Автор: ", book.author)
                print("Год: ", book.year)
                print("Статус: ", book.status)
                print()
            
        if command == 5:
            while True:
                id = input("Введите ID книги, статус которой вы бы хотели изменить: ")
                if library.is_id_valid(id):
                    break

            book = library.find_book_by_id(id)
            old_status = book.status
            if old_status == "in stock":
                new_status = "issued"
            else:
                new_status = "in stock"

            print(f"Текущий статус книги - {old_status}, если вы хотите изменить его на {new_status}, введите 'yes'. При другом ответе статус не будет изменен.")
            answer = input("Ваш ответ: ")
            if answer == "yes":
                library.change_book_status_by_id(id, new_status)
                print("Статус изменен.")
            else:
                print("Статус не был изменен.")

        if command == 6:
            print("Завершение работы.")
            return


if __name__ == "__main__":
    main()