from models.book_model import Book

book1 = Book(
    book_id=1,
    title="Clean Code",
    author="Robert C. Martin",
    year=2008,
    genre="Computer Science",
    status="read",
    rating=5,
    notes="A book about how to write clean code."
)

book2 = Book(
    book_id=2,
    title="The Pragmatic Programmer",
    author="Andrew Hunt",
    year=1999,
    genre="Computer Science",
    status="reading",
    rating=4,
    notes="A book about how to be a good programmer."
)

books = [book1, book2]
next_id = 3