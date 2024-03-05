from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ytxdurpb:8SeN2cjLygPzwgcvs2aY5NaNs5-xHTCS@ruby.db.elephantsql.com/ytxdurpb'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

#DataBase

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128)) 


def initialize():
    db.create_all()

# Routes

@app.route('/')
def index():
    return render_template('index.html')

from auth import auth_bp


app.register_blueprint(auth_bp, url_prefix='/auth') 


if __name__ == '__main__':
    app.run(debug=True)


# Currently there is a bug that maintains the application is working out of context
# this bug will run an error if you do not change 'Isbn' and 'id' for variable 'new_book' in models.py
# each time before running the application.
# i have install the code below to keep the application running 

with app.app_context():
    from book_api import book_api

    app.register_blueprint(book_api, url_prefix='/api')


