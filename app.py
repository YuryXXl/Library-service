from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

books = []
next_id = 1

@app.route("/")
def homepage():
    return render_template("index.html")

# GET /api/books
@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

# GET /api/books/<book_id>
@app.route("/api/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["book_id"] == book_id:
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# POST /api/books
@app.route("/api/books", methods=["POST"])
def add_book():
    global next_id
    data = request.get_json()
    if not data.get("title") or not data.get("author"):
        return jsonify({"error": "Title and author required"}), 400

    new_book = {
        "book_id": next_id,
        "title": data["title"],
        "author": data["author"],
        "year": data.get("year", None),
        "genre": data.get("genre", ""),
        "status": data.get("status", "to read"),
        "rating": data.get("rating", 0),
        "notes": data.get("notes", "")
    }
    books.append(new_book)
    next_id += 1
    return jsonify(new_book), 201

# PUT /api/books/<book_id>
@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book["book_id"] == book_id:
            book.update({
                "title": data.get("title", book["title"]),
                "author": data.get("author", book["author"]),
                "year": data.get("year", book.get("year")),
                "genre": data.get("genre", book.get("genre")),
                "status": data.get("status", book.get("status")),
                "rating": data.get("rating", book.get("rating")),
                "notes": data.get("notes", book.get("notes")),
            })
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# DELETE /api/books/<book_id>
@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"}), 200
    return jsonify({"error": "Book not found"}), 404

# GET /api/books/stats
@app.route("/api/books/stats", methods=["GET"])
def get_stats():
    total_books = len(books)
    status_counts = {"read": 0, "reading": 0, "to read": 0}
    genre_counts = {}
    rating_sum = 0
    rated_books = 0

    for book in books:
        status = book.get("status", "to read")
        if status in status_counts:
            status_counts[status] += 1

        genre = book.get("genre", "")
        if genre:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

        if isinstance(book.get("rating"), int) or isinstance(book.get("rating"), float):
            rating_sum += book["rating"]
            rated_books += 1

    avg_rating = round(rating_sum / rated_books, 2) if rated_books > 0 else 0

    return jsonify({
        "total_books": total_books,
        "books_by_status": status_counts,
        "average_rating": avg_rating,
        "books_by_genre": genre_counts
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
