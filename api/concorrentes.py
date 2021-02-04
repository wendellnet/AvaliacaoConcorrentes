import jsonschema

from schemas.concorrente_schema import *
from flask import jsonify, Response, request, json
from models.concorrente_model import Concorrentes
from messages.error_messages import *


def get_all_concorrentes():
    return_value = jsonify({'concorrentes': Concorrentes.get_all_concorrentes()})
    return return_value

def get_by_concorrente(codigo):
    response = Response(str(Concorrentes.get_concorrente(codigo)), 200, mimetype="application/json")
    return response

def get_by_concorrente_nome(nome):
    response = Response(str(Concorrentes.get_concorrente_by_name(nome)), 200, mimetype="application/json")
    return response

def get_by_concorrente_municipio(municipio):
    response = Response(str(Concorrentes.get_concorrente_by_municipio(municipio)), 200, mimetype="application/json")
    return response

def get_by_concorrente_uf(uf):
    response = Response(str(Concorrentes.get_concorrente_by_uf(uf)), 200, mimetype="application/json")
    return response

def get_by_concorrente_codigo_bairro(codigo_bairro):
    response = Response(str(Concorrentes.get_concorrente_by_codigo_bairro(codigo_bairro)), 200, mimetype="application/json")
    return response

