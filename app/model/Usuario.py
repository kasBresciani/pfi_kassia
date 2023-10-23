from app import db


class Usuario(db.Model): 
    # cria a classe "usuário" 
    __tablename__ = "usuarios"
    # Indica qual tabela está relacionada com a classe "usuário"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    datadenascimento = db.Column(db.String(50))
    senha = db.Column(db.String(50))
    # indica as colunas do bd que são referentes aos atributos da classe 
    
    def __init__(self, nome, email, datadenascimento, senha):
        self.nome = nome
        self.email = email
        self.datadenascimento = datadenascimento
        self.senha = senha
        
    def toJson(self): # pega os paraêtros e retorna como dicionário
        return {"id":self.id, "nome":self.nome, "email":self.email, "Data de Nascimento":self.datadenascimento, "senha":self.senha}