from app import app
from flask import render_template, request


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/perfil/<id>')
def perfil(id):
    user = usr.get_user(id)
    return render_template("perfil.html", user = user)

from app.controllers import UsuarioControler as usr

# o texto deste arquivo poderia estar dentro "app.controllers" 
# mas por uma questão de organização é melhor manter separado
