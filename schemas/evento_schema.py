add_evento_schema = {
    "type": "object",
    "properties": {
        "codigo": {"type": "string"},
        "data": {"type": "string"},
        "codigo_concorrente": {"type": "string"},
        "diadasemana": {"type": "string"},
        "hora": {"type": "integer"},
        "periodo": {"type": "string"}
    },
    "required": ["codigo", "data", "codigo_concorrente"]
}