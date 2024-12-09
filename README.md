# Library Management System

## Описание проекта

Этот проект представляет собой систему управления библиотекой книг. Приложение позволяет добавлять, удалять, искать книги, а также изменять их статус (например, доступна в библиотеке или выдана). Приложение работает с данными о книгах, которые сохраняются в формате JSON на локальном диске.

## Основной функционал

Приложение предоставляет следующие функции:

### 1. **Добавление книги**
   - Вы можете добавить новую книгу в библиотеку, указав её уникальный ID, название, автора, год издания и статус (по умолчанию "in stock").
   - Система автоматически сгенерирует уникальный ID, если указанный уже существует в базе.

### 2. **Удаление книги**
   - Книгу можно удалить по её уникальному ID.
   - Если книга с таким ID не найдена, будет выведено соответствующее сообщение.

### 3. **Поиск книг**
   Приложение позволяет искать книги по следующим параметрам:
   - **ID**: Поиск по уникальному идентификатору.
   - **Название**: Поиск книг, содержащих заданную подстроку в названии.
   - **Автор**: Поиск книг, написанных автором, чье имя или фамилия содержат заданную подстроку.
   - **Год издания**: Поиск книг, выпущенных в указанный год.

### 4. **Изменение статуса книги**
   - Статус книги можно изменить на `in stock` (книга доступна) или `issued` (книга выдана).
   - При изменении статуса система проверяет корректность данных (например, книга с указанным ID должна существовать).

### 5. **Валидация данных**
   - Все входные данные проходят валидацию. Приложение проверяет:
     - Корректность ID (он должен быть больше нуля и уникальным).
     - Корректность года (год не должен быть больше текущего).
   
### 6. **Хранение данных**
   - Все данные о книгах хранятся в локальном файле в формате JSON.
   - При добавлении, удалении или изменении книги данные автоматически сохраняются в файл.

### 7. **Генерация уникальных ID**
   - Для каждой новой книги система генерирует уникальный ID, который не повторяется в базе данных.

## Структура данных

Каждая книга представлена объектом с такими атрибутами:
- `id` (int): Уникальный идентификатор книги.
- `title` (str): Название книги.
- `author` (str): Автор книги.
- `year` (int): Год издания книги.
- `status` (str): Статус книги (по умолчанию "in stock").

## Инструкции по установке и запуску

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

### 2. Запуск приложения

```bash
python main.py
```

## Тестирование
Для запуска тестов запустите команду:
```bash
python -m unittest discover tests
```
