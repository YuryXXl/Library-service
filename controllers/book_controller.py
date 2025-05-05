from flask import Blueprint, jsonify, request
from services.book_service import get_all_books, get_book_by_id, add_book, delete_book
from utils.validation import validate_book_data

book_bp = Blueprint("books", __name__, url_prefix="/v2")

@book_bp.route("/books", methods=["GET"])
def list_books():
    return jsonify(get_all_books()), 200

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@book_bp.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    if not validate_book_data(data):
        return jsonify({"error": "Missing required fields"}), 400
    return jsonify(add_book(data)), 201

@book_bp.route("/books/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):
    delete_book(book_id)
    return '', 204