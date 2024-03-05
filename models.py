from app import db,app


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    cover_type = db.Column(db.String(50), nullable=False)  # Hardcover or Paperback




new_book = Book(title="Example Book", author_name="Author Name", id='39',isbn ='aaaee',length = '150', cover_type='hard copy')
db.session.add(new_book)
db.session.commit()

