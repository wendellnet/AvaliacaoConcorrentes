from flask import Response
from models.bairro_model import *
from models.concorrente_model import *
from models.populacao_model import *
from models.evento_model import *
from models.precopraticado_model import *

import sqlite3

conn = sqlite3.connect('database/database.db', check_same_thread=False)

def create_db():
    db.drop_all()
    db.create_all()

    Bairros.add_bairros_td(conn)
    Concorrentes.add_concorrentes_td(conn)
    Populacoes.add_populacoes_td(conn)
    Eventos.add_eventos_td(conn)
    PrecoPraticado.add_precopraticado_td()
    
    response_text = '{ "message": "Database criado." }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


def welcome():
    response_text = '{ "message": "Olá, seja bem vindo a API de Avaliação de Concorrentes" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


def health():
    response_text = '{ "status": "OK" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response
