from flask import request, jsonify
from database import db
from models import Cliente
from . import bp
from datetime import datetime

@bp.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    try:
        # Convertendo a string data_nascimento para um objeto date
        data['data_nascimento'] = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        cliente = Cliente(**data)
        db.session.add(cliente)
        db.session.commit()
        return jsonify(cliente.id), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@bp.route('/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify({
        'id': cliente.id,
        'nome': cliente.nome,
        'email': cliente.email,
        'telefone': cliente.telefone,
        'sexo': cliente.sexo,
        'cpf': cliente.cpf,
        'data_nascimento': cliente.data_nascimento.strftime('%Y-%m-%d'),
        'cep': cliente.cep,
        'bairro': cliente.bairro,
        'logradouro': cliente.logradouro,
        'numero': cliente.numero
    })

@bp.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    cliente = Cliente.query.get_or_404(id)
    try:
        # Convertendo a string data_nascimento para um objeto date
        if 'data_nascimento' in data:
            data['data_nascimento'] = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        for key, value in data.items():
            setattr(cliente, key, value)
        db.session.commit()
        return jsonify({
            'id': cliente.id,
            'nome': cliente.nome,
            'email': cliente.email,
            'telefone': cliente.telefone,
            'sexo': cliente.sexo,
            'cpf': cliente.cpf,
            'data_nascimento': cliente.data_nascimento.strftime('%Y-%m-%d'),
            'cep': cliente.cep,
            'bairro': cliente.bairro,
            'logradouro': cliente.logradouro,
            'numero': cliente.numero
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@bp.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return '', 204
