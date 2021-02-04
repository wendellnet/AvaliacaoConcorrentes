add_precopraticado_schema = {
    "type": "object",
    "properties": {
        "faixa_preco": {"type": "integer"},
        "descricao": {"type": "string"}
    },
    "required": ["faixa_preco", "descricao"]
}

update_descricao_schema = {
    "type": "object",
    "properties": {
        "descricao": {"type": "string"}
    },
    "required": ["descricao"]
}
