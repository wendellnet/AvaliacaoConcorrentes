import jsonschema

from schemas.evento_schema import *
from flask import jsonify, Response, request, json
from models.evento_model import Eventos
from messages.error_messages import *

def get_all_eventos(offset, limit):
    try:
        return_value = Response(str(Eventos.get_all_eventos(offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        return_value = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return return_value

def get_by_evento_codigo_concorrente(codigo_concorrente, offset, limit):
    try:
        response = Response(str(Eventos.get_evento_by_codigo_concorrente(codigo_concorrente, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

def get_by_evento_periodo(periodo, offset, limit):
    try:
        response = Response(str(Eventos.get_evento_by_periodo(periodo, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

def get_by_evento_diadasemana(diadasemana, offset, limit):
    try:
        response = Response(str(Eventos.get_evento_by_diadasemana(diadasemana, offset, limit)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response

