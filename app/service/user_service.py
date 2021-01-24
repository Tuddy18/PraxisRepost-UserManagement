from app import app, PROFILE_SERVICE_URL
from flask import request, render_template, flash, redirect, url_for, session, jsonify
from passlib.hash import sha256_crypt
from sqlalchemy.orm import with_polymorphic
import requests

from app.domain.user import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        email = request.form['email']
        password_candidate = request.form['password']

        entities = with_polymorphic(User, '*')
        user = db.session().query(entities).filter_by(email=email).first()

        # use this for non polymorphic query
        # user = User.query.filter_by(email=email).first()

        # Compare passwords
        # if sha256_crypt.verify(password_candidate, user.password):
        if user.password == password_candidate:
            # Passed
            flash('You are now logged in', 'success')
            resp = jsonify(user.json_dict())
            return resp
        else:
            error = 'Invalid login'
            resp = jsonify(message=error, success=False)
            resp.status_code = 401
            return resp
    else:
        error = 'Username not found'
        resp = jsonify(success=False)
        resp.status_code = 401
        return resp

@app.route('/register', methods=['POST'])
def register():
    user_json = request.get_json()
    user = User(email=user_json['email'], password=user_json['password'])

    db.session().add(user)
    db.session().commit()

    profile_json = {'email': user_json['email'], 'name': user_json['name'], 'type': user_json['type']}
    url = PROFILE_SERVICE_URL + 'profile/create'
    response = requests.post(url, json=profile_json)

    if response.status_code == 200:
        resp = jsonify(response.json())
        return resp
    else:
        db.session().delete(user)
        db.session().commit()
        resp = jsonify(success=False, message="profile creation failed")
        resp.status_code = 500
        return resp

