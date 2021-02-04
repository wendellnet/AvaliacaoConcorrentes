import json
import pandas as pd

from db_config import db

class Populacoes(db.Model):
    __tablename__ = 'populacoes'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False)
    populacao = db.Column(db.Float())
    
    def json(self):
        return{'codigo': self.codigo, 'populacao': self.populacao}

    @staticmethod
    def get_all_populacoes():
        return [Populacoes.json(populacao) for populacao in Populacoes.query.all()]

    @staticmethod
    def get_populacao(_codigo):
        query = Populacoes.query.filter_by(codigo=_codigo).first()
        return query
    

    @staticmethod
    def add_populacoes_td(conn):
        # load the data into a Pandas DataFrame
        populacao = pd.read_json('data/populacao.json', lines=False)
        # write the data to a sqlite table
        totalNull = populacao.isnull().sum().sum()
        if totalNull>0:
            populacao['populacao']=populacao['populacao'].fillna(0)

        populacao.to_sql('populacoes', conn, if_exists='append', index = False)
        
    def __repr__(self):
        populacao_object = {
            'codigo': self.codigo, 
            'populacao': self.populacao
        }
        return json.dumps(populacao_object)
