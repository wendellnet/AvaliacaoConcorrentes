import jsonschema

from schemas.bairro_schema import *
from flask import jsonify, Response, request, json
from models.bairro_model import Bairros
from messages.error_messages import *


def get_all_bairros(offset, limit):
    try:
        return_value = Response(str(Bairros.get_all_bairros(offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        return_value = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return return_value

def get_by_bairro(codigo):
    response = Response(str(Bairros.get_bairro(codigo)), 200, mimetype="application/json")
    return response

def get_by_bairro_nome(nome, offset, limit):
    try:
        response = Response(str(Bairros.get_bairro_by_name(nome, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

def get_by_bairro_municipio(municipio, offset, limit):
    try:
        response = Response(str(Bairros.get_bairro_by_municipio(municipio, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

def get_by_bairro_uf(uf, offset, limit):
    try:
        response = Response(str(Bairros.get_bairro_by_uf(uf, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response
