
from ast import Return
from tokenize import String
from cryptography.fernet import Fernet
from uuid import uuid4
import json


class Encript:
    def __init__(self):
        self.atributos()
        
    def atributos(self):
        self.key = Fernet.generate_key()
        self.contador = 0
    
    def gerar_key(self):
        key = self.key
        return key
    def encrypt(self, key , content):
        #content = self.senha
        bytescontent = bytes(content, "ASCII")
        self.atributos()
        obj = Fernet(key)
        token = obj.encrypt(bytescontent)
        return  token

    def decrypts(self, key, token):
        f = Fernet(key)
        conteudo = f.decrypt(token)
        print(conteudo)
        decode = conteudo.decode()
        return decode

    def gera_dict(self,user_string, client=object):
        key = client.gerar_key()
        encripted = client.encrypt(key, user_string)
        generate = uuid4()
        dict = {
            "id": generate.hex,
            "string": user_string , 
            "key": key.decode("utf-8"),
            "encripted":encripted.decode("utf-8")
        }
        return dict, key, encripted  
    
    def insiro_no_json(self, dict):
        self.write_json(dict, "server/database/encripted.json")
            
    
    def write_json(self, dict, filename):
        with open(filename,"r+") as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["encripted"].append(dict)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

    def verifico_json(self, filename, user_string):
        self.atributos()
        with open(filename,"r+") as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            for self.contador in range(10000):
                try:
                    for keys in file_data["encripted"][self.contador]:
                        value = file_data["encripted"][self.contador].get(keys)
                        if value == user_string:
                            return True
                    self.contador += 1
                except:
                    return False
                
