import json
import pandas as pd

from db_config import db

class Bairros(db.Model):
    __tablename__ = 'bairros'
    codigo = db.Column(db.String(10), primary_key=True)
    nome = db.Column(db.String(100))
    municipio = db.Column(db.String(80))
    uf = db.Column(db.String(2))
    area = db.Column(db.Float())
    
    
    def json(self):
        return{'codigo': self.codigo, 'nome': self.nome, 'municipio': self.municipio, 'uf': self.uf, 'area': self.area}

    @staticmethod
    def get_all_bairros(offset, limit):
        #return [Concorrentes.json(concorrente) for concorrente in Concorrentes.query.all()]
        query = Bairros.query.paginate(offset,limit,error_out=False)
        #print(query.items)
        return query.items

        #return [Bairros.json(bairro) for bairro in Bairros.query.all()]

    @staticmethod
    def get_bairro(_codigo):
        query = Bairros.query.filter_by(codigo=_codigo).first()
        return query
    
    @staticmethod
    def get_bairro_by_name(_nome, offset, limit):
        query = Bairros.query.filter(Bairros.nome.like('%' + str(_nome) + '%')).paginate(offset,limit,error_out=False)
        return query.items
    
    @staticmethod
    def get_bairro_by_municipio(_municipio, offset, limit):
        query = Bairros.query.filter(Bairros.municipio.like('%' + str(_municipio) + '%')).paginate(offset,limit,error_out=False)
        return query.items
    
    @staticmethod
    def get_bairro_by_uf(_uf, offset, limit):
        query = Bairros.query.filter_by(uf=_uf).paginate(offset,limit,error_out=False)
        return query.items

    @staticmethod
    def add_bairros(_codigo, _nome, _municipio, _uf, _area):
        new_bairros = Bairros(codigo=_codigo, nome=_nome, municipio=_municipio,
        uf=_uf, area=_area)
        db.session.add(new_bairros)
        db.session.commit()
        

    @staticmethod
    def add_bairros_td(conn):
        # load the data into a Pandas DataFrame
        bairros = pd.read_csv('data/bairros.csv',encoding='utf-8',delimiter=",")
        # write the data to a sqlite table
        bairros.to_sql('bairros', conn, if_exists='append', index = False)
        



    def __repr__(self):
        bairro_object = {
            'codigo': self.codigo,
            'nome': self.nome,
            'municipio': self.municipio,
            'uf': self.uf,
            'area': self.area
        }

        return json.dumps(bairro_object)
