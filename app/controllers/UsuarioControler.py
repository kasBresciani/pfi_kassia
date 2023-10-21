from flask import request, redirect, render_template, session, url_for
from app import app, db

from app.model.Usuario import Usuario 


def get_user():
    user = Usuario.query.all()
    list_of_users = []

    for i in user:
        list_of_users.append(i.toJson())

    return list_of_users

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

    
    db.session.add(user) # aqui ele pega a classe "usuario" e faz um "insert" no BD
    db.session.commit() # ele inicializa o comando escrito anteriormente
  
    session["nome"] = user.toJson()["nome"]
    session["email"] = user.toJson()["email"]
    session["logged_in"] = True
    return render_template("home.html")  
    # o render_template irá renderizar o template com base no arquivo que foi add e 
    # por isso não é feito com rota e sim com o endereço do arquivo

@app.route("/usuarios/auth", methods=["POST"])
def auth():
    usr_data = {
        "email":request.form["email"],
        "senha":request.form["senha"]
    }

    users = get_user()
   
    email = usr_data["email"]
    senha = usr_data["senha"]

    #return render_template("mostrarusuario.html", lista = users)
    if len(users) > 0:
        for user in users:
            if user["email"] == email and user["senha"] == senha:
                session["nome"] = user["nome"]
                session["email"] = user["email"]
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
        
        
        return redirect(url_for("perfil", id=id))

@app.route("/usuarios/sair")
def user_logout():
    
    session["nome"] = ''
    session["email"] = ''
    session["logged_in"] = False  

    return redirect(url_for("home"))

