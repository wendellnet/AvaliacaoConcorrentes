import jsonschema

from schemas.concorrente_schema import *
from flask import jsonify, Response, request, json
from models.concorrente_model import Concorrentes
from messages.error_messages import *


def get_all_concorrentes(offset, limit):
    try:
        return_value = Response(str(Concorrentes.get_all_concorrentes(offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        return_value = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return return_value

    #return_value = jsonify({'concorrentes': Concorrentes.get_all_concorrentes()})
    #return return_value

def get_by_concorrente(codigo):
    response = Response(str(Concorrentes.get_concorrente(codigo)), 200, mimetype="application/json")
    return response

def get_by_concorrente_nome(nome, offset, limit):
    try:
        response = Response(str(Concorrentes.get_concorrente_by_name(nome, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

def get_by_concorrente_municipio(municipio, offset, limit):
    try:
        response = Response(str(Concorrentes.get_concorrente_by_municipio(municipio, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

def get_by_concorrente_uf(uf, offset, limit):
    try:
        response = Response(str(Concorrentes.get_concorrente_by_uf(uf, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

def get_by_concorrente_codigo_bairro(codigo_bairro, offset, limit):
    try:
        response = Response(str(Concorrentes.get_concorrente_by_codigo_bairro(codigo_bairro, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response
