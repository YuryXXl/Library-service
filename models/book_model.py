from uuid import uuid4
from datetime import datetime

class Book:
    def __init__(self, book_id, title, author, year, genre, status, rating, notes):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.status = status
        self.rating = rating
        self.notes = notes
        self.uuid = str(uuid4())
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "status": self.status,
            "rating": self.rating,
            "notes": self.notes,
            "uuid": self.uuid,
            "created_at": self.created_at.isoformat()
        }
