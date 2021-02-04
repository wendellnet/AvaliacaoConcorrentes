import jsonschema

from schemas.bairro_schema import *
from flask import jsonify, Response, request, json
from models.bairro_model import Bairros
from messages.error_messages import *


def get_all_bairros():
    return_value = jsonify({'bairros': Bairros.get_all_bairros()})
    #return_value = Response(str(Bairros.get_all_bairros()), 200, mimetype="application/json")
    return return_value

def get_by_bairro(codigo):
    response = Response(str(Bairros.get_bairro(codigo)), 200, mimetype="application/json")
    return response

def get_by_bairro_nome(nome):
    response = Response(str(Bairros.get_bairro_by_name(nome)), 200, mimetype="application/json")
    return response

def get_by_bairro_municipio(municipio):
    response = Response(str(Bairros.get_bairro_by_municipio(municipio)), 200, mimetype="application/json")
    return response

def get_by_bairro_uf(uf):
    response = Response(str(Bairros.get_bairro_by_uf(uf)), 200, mimetype="application/json")
    return response
