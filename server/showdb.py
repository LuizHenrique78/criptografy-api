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
    with open('encripted.json', "r") as read:
        json_data = json.load(read)
        lista_de_dados = json_data["encripted"]

    return render_template("show_data.html", json_data=json_data, lista_de_dados=lista_de_dados)