
import json


class Manipulation:
    def __init__(self):
        self.atributos()
        
        
    def atributos(self):
        pass

    
    def get_queue(self):
        return open('queue.txt', "r").read()

    def get_json(self):
        with open("encripted.json", "r") as file:
            data_json = json.load(file)
            return data_json

    def write_queue(self, string):
        
    



obj = Manipulation()
print(obj.get_queue())
            
