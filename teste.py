#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

user = [
    {
        'id': 0,

    },
    {
        'id':1,
    }
]
user.
# Como invocar na linha de comando
#
# curl -i http://localhost:5000/login
#
@app.route('/login', methods=['GET'])
def obtem_login():
    return jsonify({'login': login})


# Como invocar na linha de comando
#
# curl -i http://localhost:5000/login/user/senha/senha
#
@app.route('/login/<string:user>/<string:senha>', methods=['GET'])
def detalhe_user(user,senha):
    resultado = [resultado for resultado in login if resultado['user'] == user]and [resultado for resultado in login if resultado['senha'] == senha]
    if len(resultado) == 0:
        abort(404)
    return jsonify({'login': resultado[0]})

# Como invocar na linha de comando
#
# curl -i -X DELETE http://localhost:5000/livros/2
#
@app.route('/login/<string:user>', methods=['DELETE'])
def excluir_login(user):
    resultado = [resultado for resultado in login if resultado['id'] == user]
    if len(resultado) == 0:
        abort(404)
    login.remove(resultado[0])
    return jsonify({'resultado': True})


#### Autenticacao simples ####
# Como invocar na linha de comando
#
# curl -u aluno:senha123 -i http://localhost:5000/livrosautenticado
#
@app.route('/livrosautenticado', methods=['GET'])
@auth.login_required
def obtem_users_autenticados():
    return jsonify({'login': login})

# Autenticacao simples
@auth.get_password
def get_password(username):
    if username == 'aluno':
        return 'senha123'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'erro': 'Acesso Negado'}), 403)
##############################

# Para apresentar erro 404 HTTP se tentar acessar um recurso que nao existe
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'erro': 'Recurso Nao encontrado'}), 404)


if __name__ == "__main__":
    print("Servidor no ar!")
    app.run(host='0.0.0.0', debug=True)