from datetime import datetime
from database import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    funcao = db.Column(db.String(50), nullable=False)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    data_agendamento = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    servico = db.Column(db.String(50), nullable=False)

    cliente = db.relationship('Cliente', backref=db.backref('agendamentos', lazy=True))
    funcionario = db.relationship('Funcionario', backref=db.backref('agendamentos', lazy=True))
