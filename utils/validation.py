def validate_book_data(data):
    required_fields = ["title", "author", "year", "genre", "status", "rating", "notes"]
    return all(field in data for field in required_fields)
