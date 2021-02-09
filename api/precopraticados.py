import jsonschema

from schemas.precopraticado_schema import *
from flask import jsonify, Response, request, json
from models.precopraticado_model import PrecoPraticado
from messages.error_messages import *


def get_precopraticado():
    return_value = jsonify({'precopraticado': PrecoPraticado.get_all_precopraticado()})
    return return_value


def get_by_faixa_preco(faixa_preco):
    response = Response(str(PrecoPraticado.get_precopraticado(faixa_preco)), 200, mimetype="application/json")
    return response


def add_precopraticado():
    request_data = request.get_json()
    try:
        jsonschema.validate(request_data, add_precopraticado_schema)
        PrecoPraticado.add_precopraticado(request_data['faixa_preco'], request_data['descricao'])
        response = Response(json.dumps(request_data), 201, mimetype="application/json")
        response.headers['PrecoPraticado'] = "precopraticado/v1/" + str(request_data['faixa_preco'])
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response


def update_descricao(faixa_preco):
    request_data = request.get_json()
    try:
        jsonschema.validate(request_data, update_descricao_schema)
        PrecoPraticado.update_descricao(faixa_preco, request_data['descricao'])
        response = Response('', 204, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response


def delete_precopraticado(faixa_preco):
    if PrecoPraticado.delete_precopraticado(faixa_preco):
        response = Response('', 204)
    else:
        response = Response(json.dumps(invalid_delete_error_msg_precopraticado), 404, mimetype="application/json")
    return response
