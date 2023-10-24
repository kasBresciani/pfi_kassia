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
        "datadeNascimento":request.form["DT_Nasc"],
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

    user = Usuario( usuario["nome"], usuario["email"], usuario["datadeNascimento"], usuario["senha"])
    # instacia a classe usuário usando como paramêtro as infos fornecidas do dicionário 

    # db.session.add(user) # aqui ele pega a classe "usuario" e faz um "insert" no BD
    # db.session.commit() # ele inicializa o comando escrito anteriormente
        
    # session["nome"] = user.toJson()["nome"]
    # session["email"] = user.toJson()["email"]
    return render_template("home.html")  
    # o render_template irá renderizar o template com base no arquivo que foi add e 
    # por isso não é feito com rota e sim com o endereço do arquivo

@app.route("/usuarios/read" )
def read():
    user = Usuario.query.all() # "busque todos dentro da tabela usuários"
    lista = []
    
    for i in user:
        lista.append(i.toJson()) # Transforme o objeto retornado em uma condição {chave : valor} que pode ser lida pelo backend
        
        
        return redirect(url_for("perfil", id=id))

@app.route("/usuarios/sair")
def user_logout():
    
    session["nome"] = ''
    session["email"] = ''
    session["logged_in"] = False  

# @app.route("/usuarios/rec_senha")
# def read():
#     user = Usuario.query.all() # "busque todos dentro da tabela usuários"
#     lista = []
    
    # for i in user:
#         lista.append(i.toJson()) # Transforme o objeto retornado em uma condição {chave : valor} que pode ser lida pelo backend
        
#     print(lista)  
    
#     return render_template("mostrarUsuario.html", lista = lista )
