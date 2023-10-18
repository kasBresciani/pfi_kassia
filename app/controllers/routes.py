from app import app
from flask import render_template

@app.route('/') # o nome da rota pode ser qualquer um
def home():
    return render_template("home.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/forum')
def forum():
    return render_template("forum.html")

# @app.route('/home')
# def home():
#     return render_template("home.html")

from app.controllers import UsuarioControler

# o texto deste arquivo poderia estar dentro "app.controllers" 
# mas por uma questão de organização é melhor manter separado
