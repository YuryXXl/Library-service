from db import books, next_id
from models.book_model import Book

def get_all_books():
    return [book.to_dict() for book in books]

def get_book_by_id(book_id):
    for book in books:
        if book.book_id == book_id:
            return book.to_dict()
    return None

def add_book(data):
    global next_id
    new_book = Book(
        book_id=next_id,
        title=data.get("title"),
        author=data.get("author"),
        year=data.get("year"),
        genre=data.get("genre"),
        status=data.get("status"),
        rating=data.get("rating"),
        notes=data.get("notes")
    )
    books.append(new_book)
    next_id += 1
    return new_book.to_dict()

def delete_book(book_id):
    global books
    books = [book for book in books if book.book_id != book_id]
