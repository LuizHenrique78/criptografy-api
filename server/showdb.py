from http import client
import string
from uuid import uuid4
from xmlrpc.client import boolean
from pyrsistent import b
from flask import Blueprint, render_template, request, redirect, url_for
from server.libs.Encript import Encript 
import json

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
    try:
        with open('server/database/encripted.json', "r") as read:
            json_data = json.load(read)
            list = json_data["encripted"]
            contador = 0 
            contador_iguais = 0
        for dict in list:
            for keys in dict:
                value = dict.get(keys)
                dici = list[contador]
                print(value)
                if value == reference:
                    ref = value
                    list_dict = []
                    dici = list[contador]
                    list_dict.append(dici)
                    contador_iguais += 1
                    print(contador_iguais)
                    if reference == ref:
                        return render_template("filter.html", lista_de_dados=dici)
            contador += 1
        
        
                       
    except: 
        return "nao rolou"