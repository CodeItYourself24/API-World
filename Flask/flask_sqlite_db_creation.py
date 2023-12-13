
# ******** creating and connecting to sqlite db in flask **************

# 1. install flask and flask-sqlalchemy

'''
    - "pip install flask"
    - "pip install Flask Flask-SQLAlchemy"
'''

# 2.setup flask app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)          # creating instance of flask and initializes web app

# Configure the SQLite database. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Replace 'app.db' with your desired database file.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Suppresses warning

db = SQLAlchemy(app)    # creates a SQLAlchemy object that is linked to the application.

# 3.create database models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# 4. create database tables

    # Run this command in your terminal to create the tables
'''
    flask db.create_all()
'''

    # OR can db tables can also be created like below (IFF your db is defined in seperate python file)

'''
    def create_db():
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")

    if __name__ == '__main__':
    create_db()
'''
    # and run the database.py file

# check if an instance with db is created

# 5. create your API's

# Create a route to add users via POST request
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request
        new_user = User(
            id=data.get('id'),
            username=data.get('username'),
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added successfully!'}), 201
    else:
        return jsonify({'error': 'Invalid request method'}), 405

# 6.Test your API using postman with endpoints

'''
{
  "id": "unique_id_here",
  "username": "john_doe"
}

'''