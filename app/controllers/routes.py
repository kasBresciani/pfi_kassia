from app import app
from flask import render_template, request, session


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/perfil')
def perfil():
    email = session.get("email")
    users = usr.get_user()
    user_logged = []
    if len(users) > 0:
        for user in users:
            if user["email"] == email: 
                user_logged.append(user)   

    return render_template("perfil.html", user = user_logged)

from app.controllers import UsuarioControler as usr

# o texto deste arquivo poderia estar dentro "app.controllers" 
# mas por uma questão de organização é melhor manter separado
