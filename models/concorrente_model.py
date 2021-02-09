import json
import pandas as pd

from db_config import db

class Concorrentes(db.Model):
    __tablename__ = 'concorrentes'
    codigo = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(120))
    faixa_preco = db.Column(db.Integer())
    endereco = db.Column(db.String(300))
    municipio = db.Column(db.String(80))
    uf = db.Column(db.String(2))
    codigo_bairro = db.Column(db.Integer())
    categoria_json = db.Column(db.JSON)
    
    def json(self):
        return{'codigo': self.codigo, 'nome': self.nome, 'categoria': self.categoria, 'faixa_preco': self.faixa_preco, 'endereco': self.endereco,
        'municipio': self.municipio, 'uf': self.uf, 'codigo_bairro': self.codigo_bairro}

    @staticmethod
    def get_all_concorrentes(offset, limit):
        #return [Concorrentes.json(concorrente) for concorrente in Concorrentes.query.all()]
        query = Concorrentes.query.paginate(offset,limit,error_out=False)
        #print(query.items)
        return query.items


    @staticmethod
    def get_concorrente(_codigo):
        query = Concorrentes.query.filter_by(codigo=_codigo).first()
        return query
    
    @staticmethod
    def get_concorrente_by_name(_nome, offset, limit):
        query = Concorrentes.query.filter(Concorrentes.nome.like('%' + str(_nome) + '%')).paginate(offset,limit,error_out=False)
        #q = session.query(Bairros).filter(Bairros.nome.like('e%')).\
        #        limit(5).from_self().\
        #        join(User.addresses).filter(Address.email.like('q%'))

        return query.items
    
    @staticmethod
    def get_concorrente_by_uf(_uf, offset, limit):
        query = Concorrentes.query.filter_by(uf=_uf).paginate(offset,limit,error_out=False)
        return query.items
    
    @staticmethod
    def get_concorrente_by_codigo_bairro(_codigo_bairro, offset, limit):
        query = Concorrentes.query.filter_by(codigo_bairro=_codigo_bairro).paginate(offset,limit,error_out=False)
        return query.items

    @staticmethod
    def get_concorrente_by_municipio(_municipio, offset, limit):
        query = Concorrentes.query.filter_by(municipio=_municipio).paginate(offset,limit,error_out=False)
        return query.items

    @staticmethod
    def add_concorrentes_td(conn):
        # load the data into a Pandas DataFrame
        concorrentes = pd.read_csv('data/concorrentes.csv',encoding='utf-8',delimiter=",")
        # write the data to a sqlite table
        def str_txt_array(x):
            y = "[\""
            z = "\"]"
            x2 = x.replace(" ","").replace(",","\",\"")
    
            return (y+"" + x2 +"" + z).lower()
        concorrentes['categoria_json'] = concorrentes['categoria'].apply(str_txt_array)

        concorrentes.to_sql('concorrentes', conn, if_exists='append', index = False)
        
    def __repr__(self):
        concorrente_object = {
            'codigo': self.codigo, 
            'nome': self.nome, 
            'categoria': self.categoria, 
            'faixa_preco': self.faixa_preco, 
            'endereco': self.endereco,
            'municipio': self.municipio, 
            'uf': self.uf, 
            'codigo_bairro': self.codigo_bairro,
            'categoria_json': self.categoria_json

        }
        return json.dumps(concorrente_object)
