from flask_cors import cross_origin
from app import app
from flask import render_template, request, jsonify
from app.models import User
from app.database import session
import uuid


@app.route('/')
def home():
    return render_template('index.html'), 200


@app.route('/register')
def register():
    return render_template('register.html'), 200


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

    return render_template('/'), 200


@app.route('/auth', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type'])
def authenticate():
    try:
        req_auth = request.json
        email = req_auth.get('email')
        password = req_auth.get('password')

        user = session.query(User).filter_by(
            email=email, password=password).first()

        print(req_auth)
        # return True

        if user:
            return jsonify({'authenticated': True, 'user_id': user.id})
        else:
            return jsonify({'authenticated': False}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/dashboard', methods=['GET'])
def dashboard():
    users = session.query(User).all()
    return render_template('dashboard.html', users=users)
