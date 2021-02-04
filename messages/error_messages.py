invalid_post_error_msg_precopraticado = {
    "error": "Invalid request",
    "helpString": "Example: {'faixa_preco': '1', 'descricao': 'R&40,00 à R$80,00'}"
}

invalid_put_error_msg_precopraticado = {
    "error": "Invalid request",
    "helpString": "Example: {'faixa_preco': '1', 'descricao': 'R&40,00 à R$80,00'}"
}

invalid_delete_error_msg_precopraticado = {
    "error": "Preco praticado não encontrado, indisponivel para excluir."
}

def error_message_helper(msg):
    return '{ "error": "' + msg + '."}'

class ErrorMessages:
    pass
