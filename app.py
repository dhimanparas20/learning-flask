from os import system,environ
from flask import *
from time import sleep
import requests
import json,time

app = Flask(__name__)
system("clear")

@app.route('/<name>', methods=['GET', 'POST'])
def home(name):
    if request.method == 'GET':
      res = requests.get(f"https://api.agify.io?name={name}")
      x = res.json()
      y = x['age']
      print(f"Hello {name}, you look.{y} years old")
      return (f"Hello {name}, you look.{y} years old")
      #return "hello"
      
@app.route('/ok/<game>', methods=['GET', 'POST'])      
def ok(game):
  return jsonify({"key":69,"value":f"{game}","TIME":time.time()}),200
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
      res = requests.get(f"https://dog.ceo/api/breeds/image/random")
      x = res.json()
      y = x['message']
      system(f"curl {y} -o out.jpg")
      return send_file("out.jpg", mimetype='image/gif')
  
if __name__ == "__main__":
  app.run(debug=True)
