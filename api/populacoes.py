import jsonschema

from schemas.concorrente_schema import *
from flask import jsonify, Response, request, json
from models.populacao_model import Populacoes
from messages.error_messages import *


def get_all_populacoes():
    return_value = jsonify({'populacoes': Populacoes.get_all_populacoes()})
    return return_value

def get_by_populacao(codigo):
    response = Response(str(Populacoes.get_populacao(codigo)), 200, mimetype="application/json")
    return response

