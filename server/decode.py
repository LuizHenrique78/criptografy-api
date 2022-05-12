
from http import client
import string
from uuid import uuid4
from xmlrpc.client import boolean
from pyrsistent import b
from flask import Blueprint, render_template, request, redirect, url_for
from server.libs.Encript import Encript
import json

decode = Blueprint('decode', __name__)
client = Encript()


@decode.route('/decode', methods=['POST', 'GET'])
def decodes():
    if request.method == "POST":
        user_encoded = request.form["encoded"]
        #print(user_encoded)
        #print(type(user_encoded))
        
        try:
            with open('encripted.json', "r") as read:
                json_data = json.load(read)
                list = json_data["encripted"]
            determined_index = list.index(next(filter(lambda n: n.get("encripted") == str(user_encoded), list)))
            key = list[determined_index]["key"]
            encripted = list[determined_index]["encripted"]
            print(len(str(encripted)))
        except:
            return "<p>String nao encontrada</p>"
        if len(encripted) == 100:
                print(len(encripted))
                bytestoken = bytes(encripted, "ASCII")
                variable = client.decrypts(key, bytestoken)
                lista = []
                lista.append(variable)
                #print(variable)
                #print(variable)
                print("passou aq")
        else:
            return "<p>Passe uma string encriptada.</p>"
        
                

                
                
                
        
        return  render_template("decode.html", string=string, decript=lista)
    else:
        return  render_template("decode.html")


# @code.route("/<dados>")
# def dado(data):
#     return  f"<h1>Dados</h1><p>{data}</p>"
    
# @decode.route("/<results>")
# def results(results):
      
#     with open('encripted.json', "r+") as file: 
#         results = json.load(file)
#     return  f"<h1>Dados1</h1><h1>{results}</h1>"