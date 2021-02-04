def validate_bairro_object(bairro_object):
    if "nome" in bairro_object and "codigo" in bairro_object:
        return True
    else:
        return False


def validate_put_request_object(bairro_object):
    if "codigo" in bairro_object:
        return True
    else:
        return False
