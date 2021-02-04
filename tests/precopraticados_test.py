import json
import os
import connexion
import pytest

from config import my_app
from db_config import db

ac_api = connexion.FlaskApp(__name__)
# setting in memory database for testing
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(my_app.root_path, 'database/test.db')
ac_api.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
ac_api.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(ac_api.app)
ac_api.add_api('../swagger/swagger.yml')


@pytest.fixture(scope='module')
def client():
    with ac_api.app.test_client() as c:
        yield c


@pytest.fixture(scope='module')
def helper(json_info):
    for info in json_info:
        first_row = info.decode("utf-8")
        return str(json.loads(first_row))


def test_precopraticados_tc0001_get(client):
    td_faixa_preco = 'Abaixo de R$40,00'
    response = client.get('/precopraticado/v1')
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert location is found on response json
    if td_faixa_preco not in json_info:
        print("FAIL: Not able to find td " + td_faixa_preco)
        assert False


def test_precopraticados_tc0002_get_by_faixa_preco(client):
    td_faixa_preco = '2'
    response = client.get('/precopraticado/v1/' + td_faixa_preco)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert location is found on response json
    if td_faixa_preco not in json_info:
        print("FAIL: Not able to find td " + td_faixa_preco)
        assert False


def test_precopraticados_tc0003_post(client):
    td_faixa_preco = 'wi'
    td_descricao = 'madison'

    response = client.post('/precopraticado/v1', data=json.dumps(dict(
        faixa_preco=td_faixa_preco,
        descricao=td_descricao
    )), mimetype='application/json')

    json_info = helper(response.response)

    if td_faixa_preco not in json_info and td_descricao not in json_info:
        print("FAIL: Not able to find td " + td_faixa_preco + ' ' + td_descricao)
        assert False


def test_precopraticados_tc0004_put(client):
    td_faixa_preco = '2'
    td_descricao = 'R$41,00 à R$80,00'

    response = client.put('/precopraticado/v1/' + td_faixa_preco, data=json.dumps(dict(descricao=td_descricao)),
                          mimetype='application/json')
    # assert proper status code returned
    assert response.status_code == 204
    # making a get call to retrieve record to verify email updated
    response = client.get('/precopraticado/v1/' + td_faixa_preco)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert email is found on response json
    if td_descricao not in json_info:
        print("FAIL: Not able to find td " + td_descricao)
        assert False


def test_precopraticados_tc0005_delete(client):
    td_faixa_preco = 10
    td_descricao = 'madison'

    test = client.post('/precopraticado/v1', data=json.dumps(dict(
        faixa_preco=td_faixa_preco,
        descricao=td_descricao
    )), mimetype='application/json')

    response = client.delete('/precopraticado/v1/' + str(td_faixa_preco))
    assert response.status_code == 204

def test_precopraticados_tc0006_bad_post(client):
    td_faixa_preco = 'wi'
    td_descricao = 'madison'
    td_error_msg = '{\'error\': "\'faixa_preco\' is a required property."}'

    response = client.post('/precopraticado/v1', data=json.dumps(dict(
        faixa_precoz=td_faixa_preco,
        descricao=td_descricao
    )), mimetype='application/json')

    assert response.status_code == 400

    json_info = str(helper(response.response))

    if td_error_msg not in json_info:
        print("FAIL: Error message not found: " + td_error_msg)
        assert False


def test_precopraticados_tc0007_bad_put(client):
    td_faixa_preco = '1'
    td_descricao = 'R&40,00 à R$80,00'
    td_error_msg = '{\'error\': "\'descricao\' is a required property."}'

    response = client.put('/precopraticado/v1/' + td_faixa_preco, data=json.dumps(dict(descricaoz=td_descricao)),
                          mimetype='application/json')
    # assert proper status code returned
    assert response.status_code == 400

    json_info = helper(response.response)
    # assert descricao is not found on response json
    if td_error_msg not in json_info:
        print("Error message not found: " + td_error_msg)
        assert False


def test_precopraticados_tc0008_bad_delete(client):
    td_faixa_preco = '22'
    td_error_msg = '{\'error\': \'Preco praticado não encontrado, indisponivel para excluir.\'}'

    response = client.delete('/precopraticado/v1/' + td_faixa_preco)

    # assert proper status code returned
    assert response.status_code == 404
    json_info = helper(response.response)

    print(json_info)
    print(td_error_msg)

    # assert email is not found on response json
    if td_error_msg not in json_info:
        print("Error message not found: " + td_error_msg)
        assert False
