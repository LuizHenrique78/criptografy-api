
from http import client
import string
from uuid import uuid4
from xmlrpc.client import boolean
from pyrsistent import b
from flask import Blueprint, render_template, request, redirect, url_for
from server.libs.Encript import Encript 
from server.libs.Manipulation import Manipulation as lib_manipulation
import json

code = Blueprint('code', __name__)
client = Encript()


@code.route('/code', methods=['POST', 'GET'])
def encode():
    if request.method == "POST":
        user_string = request.form["String"]
        status = lib_manipulation.verifica_vazio(request.form["String"])
        if status == False:
            return "Nao envie o formulario vazio", 400
        else:
            dict, key, encripted  = client.gera_dict(user_string, client)
            client.insiro_no_json(dict)
            results = client.verifico_json("server/database/encripted.json", user_string )
            if results == True:

                return render_template("code.html", user_key=key.decode('utf-8'), user_encripted=encripted.decode('utf-8'))
            else:
                return "Erro generico ao enviar a task, problema na lib manipulation.py", 400
    else:
        return  render_template("code.html")
  
@code.route("/<results>")
def results(results):
    return  f"<h1>Dados1</h1><h1>{results}</h1>"