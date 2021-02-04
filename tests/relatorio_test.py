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


def test_avaliacao_tc0007_get_avaliacao_concorrente(client):
    td_codigo_concorrente = '650509405109544'
    response = client.get('/avaliacao/v1?codigo_concorrente='+td_codigo_concorrente)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_codigo_concorrente not in json_info:
        print("FAIL: Not able to find td " + td_codigo_concorrente)
        assert False  

def test_avaliacao_tc0008_get_comparativo_seguimento(client):
    td_categoria = 'gelatoshop'
    response = client.get('/avaliacao/v1/seguimento?categoria='+td_categoria)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_categoria not in json_info:
        print("FAIL: Not able to find td " + td_categoria)
        assert False