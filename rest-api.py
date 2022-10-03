from os import system,environ
from flask import *
import requests
import json,time
from flask_restful import Resource, Api

system("clear")
app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        n1 = request.args.get('num1',type=int)
        n2 = request.args.get('num2',type=int)
        print(n1,n2)
        return {"Number1":n1,"Number2":n2,"Product":n1*n2,
                "time":time.time()
        },200
        
    def post(self):
        n1 = request.json['num1']
        n2 = request.json['num2']
        print(n1,n2)
        return {"num1":n1,"num2":n2,"prod":n1*n2},202 

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True)
