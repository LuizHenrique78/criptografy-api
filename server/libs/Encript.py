
from ast import Return
from cryptography.fernet import Fernet


class Encript:
    def __init__(self):
        self.atributos()
        
         
    
    def atributos(self):
        self.key = Fernet.generate_key()
    
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

    

# m = CodeRobot()
# m.criar_key("novachave.txt")
# arquivo_encripted = m.encrypt('token.txt')
# print (arquivo_encripted)
# print(m.decrypt('token.txt'))