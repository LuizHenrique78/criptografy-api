from http import client
import string
from uuid import uuid4
from xmlrpc.client import boolean
from pyrsistent import b
from flask import Blueprint, render_template, request, redirect, url_for
from server.libs.Encript import Encript 
import json

choice = Blueprint('choice', __name__)

@choice.route('/', methods=['GET'])
def escolha():
    return render_template("base.html")