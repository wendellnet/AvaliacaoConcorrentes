add_bairro_schema = {
    "type": "object",
    "properties": {
        "codigo": {"type": "string"},
        "nome": {"type": "string"},
        "municipio": {"type": "string"},
        "uf": {"type": "string"},
        "area": {"type": "string"},
    },
    "required": ["codigo", "nome", "uf"]
}