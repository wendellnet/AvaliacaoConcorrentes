add_concorrente_schema = {
    "type": "object",
    "properties": {
        "codigo": {"type": "string"},
        "nome": {"type": "string"},
        "categoria": {"type": "string"},
        "faixa_preco": {"type": "string"},
        "municipio": {"type": "string"},
        "uf": {"type": "string"},
        "codigo_bairro": {"type": "integer"},
        "categoria_json": {"type": "string"}
    },
    "required": ["codigo", "nome"]
}