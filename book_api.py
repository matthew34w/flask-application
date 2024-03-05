from flask import Blueprint, request, jsonify
from app import db
from models import Book

book_api = Blueprint('book_api', __name__)

@book_api.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(
        isbn=data['isbn'],
        author_name=data['author_name'],
        title=data['title'],
        length=data['length'],
        cover_type=data['cover_type']
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(book.id), 201

@book_api.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': book.id,
        'isbn': book.isbn,
        'author_name': book.author_name,
        'title': book.title,
        'length': book.length,
        'cover_type': book.cover_type
    } for book in books]), 200

@book_api.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'isbn': book.isbn,
        'author_name': book.author_name,
        'title': book.title,
        'length': book.length,
        'cover_type': book.cover_type
    }), 200

@book_api.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.isbn = data.get('isbn', book.isbn)
    book.author_name = data.get('author_name', book.author_name)
    book.title = data.get('title', book.title)
    book.length = data.get('length', book.length)
    book.cover_type = data.get('cover_type', book.cover_type)
    db.session.commit()
    return jsonify({
        'id': book.id,
        'isbn': book.isbn,
        'author_name': book.author_name,
        'title': book.title,
        'length': book.length,
        'cover_type': book.cover_type
    }), 200

@book_api.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 200
