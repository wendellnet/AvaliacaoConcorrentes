import json
from db_config import db

class PrecoPraticado(db.Model):
    __tablename__ = 'precopraticados'
    faixa_preco = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80), unique=True, nullable=False)
    
    def json(self):
        return {'faixa_preco': self.faixa_preco,'descricao': self.descricao}

    @staticmethod
    def get_all_precopraticado():
        return [PrecoPraticado.json(precopraticado) for precopraticado in PrecoPraticado.query.all()]

    @staticmethod
    def get_precopraticado(_faixa_preco):
        query = PrecoPraticado.query.filter_by(faixa_preco=_faixa_preco).first()
        return query

    @staticmethod
    def add_precopraticado(_faixa_preco, _descricao):
        new_precopraticado = PrecoPraticado(faixa_preco=_faixa_preco, descricao=_descricao)
        db.session.add(new_precopraticado)
        db.session.commit()

    @staticmethod
    def update_descricao(_faixa_preco, _descricao):
        precopraticado_to_update = PrecoPraticado.query.filter_by(faixa_preco=_faixa_preco).first()
        precopraticado_to_update.descricao = _descricao
        db.session.commit()

    @staticmethod
    def delete_precopraticado(_faixa_preco):
        is_successful = PrecoPraticado.query.filter_by(faixa_preco=_faixa_preco).delete()
        db.session.commit()
        return bool(is_successful)

    @staticmethod
    def add_precopraticado_td():
        PrecoPraticado.add_precopraticado(0, "Abaixo de R$40,00")
        PrecoPraticado.add_precopraticado(1, "R$40,00 à R$80,00")
        PrecoPraticado.add_precopraticado(2, "R$80,00 à R$200,00")
        PrecoPraticado.add_precopraticado(3, "R$200,00 à R$500,00")
        PrecoPraticado.add_precopraticado(4, "Acima de R$500,00")

    def __repr__(self):
        precopraticado_object = {
            'faixa_preco': self.faixa_preco,
            'descricao': self.descricao
        }
        return json.dumps(precopraticado_object)