from app import app
from flask import render_template

@app.route('/') # o nome da rota pode ser qualquer um
def home():
    return render_template("index.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

from app.controllers import UsuarioControler

# o texto deste arquivo poderia estar dentro "app.controllers" 
# mas por uma questão de organização é melhor manter separado
