import re
from flask import request, jsonify, url_for
from app import db
from app.api import bp
# from app.api.auth import token_auth
from app.api.erros import bad_request
from app.models import User


@bp.route('/users',methods = ['POST'])
def create_user():
    data =request.get_json()
    if not data:
        return bad_request("need json data")
    message = {}
    if 'username' not in data or not data.get('username', None):
        message['username'] = 'Please provide a valid username.'
    if User.query.filter_by(username=data.get('username', None)).first():
        message['username'] = 'Please use a different username.'
    if message:
        return bad_request(message)
    
    user =User()
    user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    # response.status_code = 201
    # response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users/<int:id>',methods = ['GET'])
def get_users(id):
    return jsonify(User.query.get_or_404(id).to_dict())