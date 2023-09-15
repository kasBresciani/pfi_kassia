from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# <Nome do SGBD>://<Usuário>:<Senha>@<Endereço>/<Nome do banco>
# este é o endereço do BD em toda conexão que for diferente deve ser substituido os dados

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@127.0.0.1/lillac"
app.secret_key = "q4t7w!z%C*F-JaNd"

db = SQLAlchemy(app)

from app.controllers import routes
