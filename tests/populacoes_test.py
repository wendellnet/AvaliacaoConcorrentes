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

def test_populacoes_tc0001_get_all_populacoes(client):
    td_codigo = '355620110'
    response = client.get('/populacoes/v1')
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_codigo not in json_info:
        print("FAIL: Not able to find td " + td_codigo)
        assert False

def test_populacoes_tc0002_get_by_populacao(client):
    td_codigo = '355620110'
    response = client.get('/populacoes/v1/' + td_codigo)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_codigo not in json_info:
        print("FAIL: Not able to find td " + td_codigo)
        assert False