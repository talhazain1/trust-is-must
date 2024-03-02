from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define a route for the root URL
@app.route('/')
def home():
    return jsonify(message="Welcome to Trust Is Must API"), 200

if __name__ == '__main__':
    app.run(debug=True)
