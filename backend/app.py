from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLAlchemy Database to point to PostgreSQL db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'