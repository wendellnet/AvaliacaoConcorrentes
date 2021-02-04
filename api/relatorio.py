import jsonschema

from flask import jsonify, Response, request, json
from models.relatorio_model import Relatorio
from messages.error_messages import *


def get_avaliacao_concorrente(codigo_concorrente):
    response = Response(str(Relatorio.get_relatorio(codigo_concorrente)), 200, mimetype="application/json")
    return response

def get_comparativo_seguimento(categoria):
    try:
        response = Response(str(Relatorio.get_comparativoseguimento(categoria)), 200, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response