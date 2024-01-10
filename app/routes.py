from app import app
from flask import render_template, request, jsonify
from app.models import User
from app.database import session
import uuid


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register-user', methods=['POST'])
def create_user():
    user = User(
        id=str(uuid.uuid4()),
        name=request.form.get('name'),
        email=request.form.get('email'),
        password=request.form.get('password')
    )

    session.add(user)
    session.commit()

    return render_template('dashboard.html'), 200


@app.route('/auth', methods=['POST'])
def authenticate():
    email = request.form.get('email')
    password = request.form.get('password')

    user = session.query(User).filter_by(
        email=email, password=password).first()

    if user:
        return render_template('dashboard.html'), 200
    else:
        return render_template('error.html'), 401
