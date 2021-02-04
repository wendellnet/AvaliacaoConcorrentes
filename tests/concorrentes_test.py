import json
import os
import connexion
import pytest

from config import my_app
from db_config import db

ac_app = connexion.FlaskApp(__name__)
# setting in memory database for testing
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(my_app.root_path, 'database/test.db')
ac_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
ac_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(ac_app.app)
ac_app.add_api('../swagger/swagger.yml')


@pytest.fixture(scope='module')
def client():
    with ac_app.app.test_client() as c:
        yield c


@pytest.fixture(scope='module')
def helper(json_info):
    for info in json_info:
        first_row = info.decode("utf-8")
        return str(json.loads(first_row))

def test_concorrente_tc0001_get_all_concorrentes(client):
    td_codigo_concorrente = '431962533652067'
    response = client.get('/concorrentes/v1')
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_codigo_concorrente not in json_info:
        print("FAIL: Not able to find td " + td_codigo_concorrente)
        assert False 

def test_concorrente_tc0002_get_by_concorrente(client):
    td_codigo = '431962533652067'
    response = client.get('/concorrentes/v1/' + td_codigo)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_codigo not in json_info:
        print("FAIL: Not able to find td " + td_codigo)
        assert False

def test_concorrente_tc0003_get_by_concorrente_uf(client):
    td_uf = 'SP'
    response = client.get('concorrentes/v1/uf?uf='+td_uf)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_uf not in json_info:
        print("FAIL: Not able to find td " + td_uf)
        assert False  

def test_concorrente_tc0004_get_by_concorrente_nome(client):
    td_nome = 'Boiz'
    response = client.get('/concorrentes/v1/nome?nome=' + td_nome)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_nome not in json_info:
        print("FAIL: Not able to find td " + td_nome)
        assert False     

def test_concorrente_tc0005_get_by_concorrente_municipio(client):
    td_municipio = 'Monte Mor'
    response = client.get('/concorrentes/v1/municipio?municipio='+td_municipio)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_municipio not in json_info:
        print("FAIL: Not able to find td " + td_municipio)
        assert False   

def test_concorrente_tc0006_get_by_concorrente_codigo_bairro(client):
    td_codigo_bairro = '3519071005'
    response = client.get('/concorrentes/v1/codigobairro?codigo_bairro='+ td_codigo_bairro)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_codigo_bairro not in json_info:
        print("FAIL: Not able to find td " + td_codigo_bairro)
        assert False   