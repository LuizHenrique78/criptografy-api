
from http import client
import string
from uuid import uuid4
from xmlrpc.client import boolean
from pyrsistent import b
from flask import Blueprint, render_template, request, redirect, url_for
from server.libs.Encript import Encript 
import json

code = Blueprint('code', __name__)
client = Encript()


@code.route('/code', methods=['POST', 'GET'])
def encode():
    if request.method == "POST":
        
        user_string = request.form["String"]
        key = client.gerar_key()
        encripted = client.encrypt(key, user_string)
        generate = uuid4()
        print(generate)
        dict = {"id": generate.hex,
                "string": user_string , 
                "key": key.decode("utf-8"),
                "encripted":encripted.decode("utf-8")
                }
        try:
            with open('encripted.json', "r+") as file: 
                data = json.load(file)
                print(type(data))
                data["encripted"].append(dict)
                file.seek(0)
                json.dump(data, file)

            with open('encripted.json', "r") as read:
                json_data = json.load(read)

    
            return redirect(url_for("code.results", results=json_data)) 
        except:
            return  'Erro ao enviar a task'
        
    else:
        return  render_template("code.html")

@code.route('/secret', methods =['GET'])
def basejson():
    boolean
    user_string = request.form["Dados"]
    print(user_string  + 123)
    with open('encripted.json', "r") as read:
        
            json_data = json.load(read)
    return  f"<p>{json_data}</p>"

    
@code.route("/<results>")
def results(results):
      
    with open('encripted.json', "r+") as file: 
        results = json.load(file)
    return  f"<h1>Dados1</h1><h1>{results}</h1>"