from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from .model import User
from .serealizer import UserSchema


bp_users = Blueprint('users', __name__)


@bp_users.route('/mostrar', methods=['GET'])
@jwt_required
def mostrar():
    result = User.query.all()
    return UserSchema(many=True).jsonify(result), 200


@bp_users.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    User.query.filter(Book.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_users.route('/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = UserSchema()
    query = User.query.filter(Book.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_users.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = UserSchema()
    user, error = bs.load(request.json)

    if error:
        return jsonify(error), 401

    current_app.db.session.add(user)
    current_app.db.session.commit()
    return bs.jsonify(user), 201