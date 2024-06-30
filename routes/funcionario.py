from flask import request, jsonify
from database import db
from models import Funcionario
from . import bp
from datetime import datetime

@bp.route('/funcionarios', methods=['POST'])
def create_funcionario():
    data = request.get_json()
    try:
        # Convertendo as strings de data para objetos date
        data['data_nascimento'] = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        data['data_admissao'] = datetime.strptime(data['data_admissao'], '%Y-%m-%d').date()
        funcionario = Funcionario(**data)
        db.session.add(funcionario)
        db.session.commit()
        return jsonify(funcionario.id), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@bp.route('/funcionarios/<int:id>', methods=['GET'])
def get_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    return jsonify({
        'id': funcionario.id,
        'nome': funcionario.nome,
        'email': funcionario.email,
        'telefone': funcionario.telefone,
        'sexo': funcionario.sexo,
        'cpf': funcionario.cpf,
        'data_nascimento': funcionario.data_nascimento.strftime('%Y-%m-%d'),
        'cep': funcionario.cep,
        'bairro': funcionario.bairro,
        'logradouro': funcionario.logradouro,
        'numero': funcionario.numero,
        'data_admissao': funcionario.data_admissao.strftime('%Y-%m-%d'),
        'funcao': funcionario.funcao
    })

@bp.route('/funcionarios/<int:id>', methods=['PUT'])
def update_funcionario(id):
    data = request.get_json()
    funcionario = Funcionario.query.get_or_404(id)
    try:
        # Convertendo as strings de data para objetos date
        if 'data_nascimento' in data:
            data['data_nascimento'] = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        if 'data_admissao' in data:
            data['data_admissao'] = datetime.strptime(data['data_admissao'], '%Y-%m-%d').date()
        for key, value in data.items():
            setattr(funcionario, key, value)
        db.session.commit()
        return jsonify({
            'id': funcionario.id,
            'nome': funcionario.nome,
            'email': funcionario.email,
            'telefone': funcionario.telefone,
            'sexo': funcionario.sexo,
            'cpf': funcionario.cpf,
            'data_nascimento': funcionario.data_nascimento.strftime('%Y-%m-%d'),
            'cep': funcionario.cep,
            'bairro': funcionario.bairro,
            'logradouro': funcionario.logradouro,
            'numero': funcionario.numero,
            'data_admissao': funcionario.data_admissao.strftime('%Y-%m-%d'),
            'funcao': funcionario.funcao
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@bp.route('/funcionarios/<int:id>', methods=['DELETE'])
def delete_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    db.session.delete(funcionario)
    db.session.commit()
    return '', 204
