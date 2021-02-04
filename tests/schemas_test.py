import json
import jsonschema

from schemas.bairro_schema import add_bairro_schema
from schemas.concorrente_schema import add_concorrente_schema
from schemas.evento_schema import add_evento_schema
from schemas.populacao_schema import add_populacao_schema
from schemas.precopraticado_schema import add_precopraticado_schema,update_descricao_schema


def test_schema_tc0001_add_bairro_schema():
    td_post_body = '{ "codigo": "string", "nome": "string", "municipio": "string", "uf": "string", "area": "string" }'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), add_bairro_schema)

def test_schema_tc0002_add_concorrente_schema():
    td_post_body = '{"codigo": "string","nome": "string", "categoria": "string", "faixa_preco": "string", "municipio": "string", "uf": "string", "codigo_bairro": 1, "categoria_json": "string"}'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), add_concorrente_schema)   

def test_schema_tc0003_add_evento_schema():
    td_post_body = '{"codigo": "string", "data": "string",  "codigo_concorrente": "string",  "diadasemana": "string",  "hora": 1,  "periodo": "string"}'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), add_evento_schema)
def test_schema_tc0004_add_populacao_schema():
    td_post_body = '{"codigo":"string","populacao": "string"}'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), add_populacao_schema)    
def test_schema_tc0005_add_precopraticado_schema():
    td_post_body = '{"faixa_preco": 1, "descricao": "string"}'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), add_precopraticado_schema)
def test_schema_tc0006_update_descricao_schema():
    td_post_body = '{"descricao": "string"}'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), update_descricao_schema)

