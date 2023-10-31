from app import app
from flask import render_template, request, session


@app.route('/')
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

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/recup_senha')
def recup_senha():
    return render_template("recup_senha.html")

@app.route('/hist_cdc')
def hist_cdc():
    return render_template("historia_cdc.html")

@app.route('/home')
def pag_inicial():
    return render_template("home.html")

@app.route('/perfil')
def perfil():
    return render_template("perfil.html")

from app.controllers import UsuarioControler

# o texto deste arquivo poderia estar dentro "app.controllers" 
# mas por uma questão de organização é melhor manter separado
