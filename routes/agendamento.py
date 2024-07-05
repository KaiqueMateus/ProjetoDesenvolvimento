from flask import request, jsonify
from database import db
from models import Agendamento
from . import bp
from datetime import datetime, timedelta
from models import Agendamento, Cliente, Funcionario

@bp.route('/agendamentos', methods=['POST'])
def create_agendamento():
    data = request.get_json()
    try:
        # Convertendo a string data_agendamento para um objeto datetime
        data['data_agendamento'] = datetime.strptime(data['data_agendamento'], '%Y-%m-%d %H:%M:%S')
        agendamento = Agendamento(**data)
        db.session.add(agendamento)
        db.session.commit()
        return jsonify(agendamento.id), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@bp.route('/agendamentos/<int:id>', methods=['GET'])
def get_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    return jsonify({
        'id': agendamento.id,
        'cliente_id': agendamento.cliente_id,
        'funcionario_id': agendamento.funcionario_id,
        'data_agendamento': agendamento.data_agendamento.strftime('%Y-%m-%d %H:%M:%S'),
        'servico': agendamento.servico
    })

@bp.route('/agendamentos/<int:id>', methods=['DELETE'])
def delete_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    return '', 204

@bp.route('/agendamentos', methods=['GET'])
def list_agendamentos():
    agendamentos = Agendamento.query.all()
    resultado = []
    for agendamento in agendamentos:
        cliente = Cliente.query.get(agendamento.cliente_id)
        funcionario = Funcionario.query.get(agendamento.funcionario_id)
        resultado.append({
            'id': agendamento.id,
            'cliente_nome': cliente.nome,
            'funcionario_nome': funcionario.nome,
            'data_agendamento': agendamento.data_agendamento.strftime('%Y-%m-%d %H:%M:%S'),
            'servico': agendamento.servico
        })
    return jsonify(resultado)


@bp.route('/agendamentos/search', methods=['GET'])
def search_agendamento():
    cpf_cliente = request.args.get('cpf_cliente')
    data_agendamento = request.args.get('data_agendamento')

    try:
        data_inicio = datetime.strptime(data_agendamento, '%Y-%m-%d')
        data_fim = data_inicio + timedelta(days=1)
    except ValueError:
        return jsonify({"error": "Data inválida"}), 400

    cliente = Cliente.query.filter_by(cpf=cpf_cliente).first()
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404

    agendamento = Agendamento.query.filter(
        Agendamento.cliente_id == cliente.id,
        Agendamento.data_agendamento >= data_inicio,
        Agendamento.data_agendamento < data_fim
    ).first()

    if not agendamento:
        return jsonify({"error": "Agendamento não encontrado"}), 404

    return jsonify({
        'id': agendamento.id,
        'cliente_id': agendamento.cliente_id,
        'funcionario_id': agendamento.funcionario_id,
        'data_agendamento': agendamento.data_agendamento.strftime('%Y-%m-%d %H:%M:%S'),
        'servico': agendamento.servico
    })

@bp.route('/agendamentos/<int:id>', methods=['PUT'])
def update_agendamento(id):
    data = request.get_json()
    agendamento = Agendamento.query.get_or_404(id)
    try:
        # Convertendo a string data_agendamento para um objeto datetime
        if 'data_agendamento' in data:
            data['data_agendamento'] = datetime.strptime(data['data_agendamento'], '%Y-%m-%d %H:%M:%S')
        for key, value in data.items():
            setattr(agendamento, key, value)
        db.session.commit()
        return jsonify({
            'id': agendamento.id,
            'cliente_id': agendamento.cliente_id,
            'funcionario_id': agendamento.funcionario_id,
            'data_agendamento': agendamento.data_agendamento.strftime('%Y-%m-%d %H:%M:%S'),
            'servico': agendamento.servico
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
