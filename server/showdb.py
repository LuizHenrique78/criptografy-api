from http import client
from pydoc import cli
import string
from uuid import uuid4
from wsgiref.util import request_uri
from xmlrpc.client import boolean
from pyrsistent import b
from flask import Blueprint, render_template, request, redirect, url_for
from server.libs.Encript import Encript 
import json
lib_encript = Encript()
db = Blueprint('database', __name__)

@db.route('/database', methods=['GET'])
def data():
    with open('server/database/encripted.json', "r") as read:
        json_data = json.load(read)
        lista_de_dados = json_data["encripted"]

    return render_template("show_data.html", json_data=json_data, lista_de_dados=lista_de_dados)

@db.route('/search')
def search():
    args = request.args
    reference = args.get('ref')
    retorno, lista_de_conteudo = lib_encript.pesquisa_no_json(ref=reference)
    if retorno == True:
        return render_template("filter.html", lista_de_dados=lista_de_conteudo)
    else:
        return "sorry an error occured", 400        