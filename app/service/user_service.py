from app import app
from flask import request, render_template, flash, redirect, url_for, session, jsonify
from passlib.hash import sha256_crypt
from sqlalchemy.orm import with_polymorphic

from app.domain.student import *


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
