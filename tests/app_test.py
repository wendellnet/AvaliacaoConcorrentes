import json
import connexion
import pytest

from config import my_app

ac_app = connexion.FlaskApp(__name__)
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

def test_app_tc0001_welcome(client):
    td_message = 'Olá, seja bem vindo a API de Avaliação de Concorrentes'
    response = client.get('/')
    json_info = helper(response.response)
    # validate response code
    assert response.status_code == 200
    # validate return message
    if td_message not in json_info:
        print('FAIL: Not able to find td ' + td_message)
        assert False

def test_app_tc0002_health(client):
    td_message = 'OK'
    response = client.get("/health", content_type='application/json')
    json_info = helper(response.response)
    # validate response code
    assert response.status_code == 200
    # validate return message
    if td_message not in json_info:
        print('FAIL: Not able to find td ' + td_message)
        assert False
