from flask import request, redirect, render_template, session, url_for
from app import app, db

from app.model.Usuario import Usuario 

@app.route("/usuarios/create", methods=["POST"]) 
def create():

    usuario = {
        "nome":request.form["nome"],
        "email":request.form["email"],
        "senha":request.form["senha"],
        "confsenha":request.form["confirmasenha"],
    }
    #usa as infos fornecidas no forms e coloca elas dentro de um dicionário
    
    if usuario["senha"] == usuario["confsenha"]:
        user = Usuario(usuario["nome"], usuario["email"], usuario["senha"])
    else:
        return render_template("home.html")
    # instacia a classe usuário usando como paramêtro as infos fornecidas do dicionário 

    
    #db.session.add(user) # aqui ele pega a classe "usuario" e faz um "insert" no BD
    #db.session.commit() # ele inicializa o comando escrito anteriormente
    session["id"] = user.toJson()["id"]    
    session["nome"] = user.toJson()["nome"]
    session["email"] = user.toJson()["email"]
    session["logged_in"] = True
    return render_template("home.html")  
    # o render_template irá renderizar o template com base no arquivo que foi add e 
    # por isso não é feito com rota e sim com o endereço do arquivo

@app.route("/usuarios/auth", methods=["POST"])
def auth():
    usr = {
        "email":request.form["email"],
        "senha":request.form["senha"]
    }

    user = Usuario.query.filter_by(email=usr["email"], senha = usr["senha"])
    if user.count() != 0:
        #print(user)
        for usuario in user:
            session["id"] = usuario.toJson()["id"]    
            session["nome"] = usuario.toJson()["nome"]
            session["email"] = usuario.toJson()["email"]
        session["logged_in"] = True

        return redirect(url_for("home"))
    else:
         return redirect(url_for("login"))

@app.route("/usuarios/validacao")
def validation():
    print(session.get("logged_in"))
    if session.get("logged_in") == False:
        return redirect(url_for("login"))
    else:
        id = session.get("id")
        
        return redirect(url_for("perfil", id=id))

def get_user(id):
    user = Usuario.query.filter_by(id = id)
    print(user)

    return user
@app.route("/usuarios/sair")
def user_logout():
    session["id"] = ''
    session["nome"] = ''
    session["email"] = ''
    session["logged_in"] = False  

    return redirect(url_for("home"))

