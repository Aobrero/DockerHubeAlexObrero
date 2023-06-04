from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bienvenidos a Puesta en Producción Segura'
