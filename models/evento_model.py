import json
import pandas as pd
import os
from db_config import db
import config as conf

class Eventos(db.Model):
    __tablename__ = 'eventos'
    codigo = db.Column(db.String(20), primary_key=True)
    data = db.Column(db.DateTime, primary_key=True)
    codigo_concorrente = db.Column(db.String(20),primary_key=True)
    diadasemana = db.Column(db.String(20),index=True)
    hora = db.Column(db.Integer())
    periodo = db.Column(db.String(15),index=True)
    
    def json(self):
        return{'codigo': self.codigo, 'data': self.data, 'codigo_concorrente': self.codigo_concorrente, 'diadasemana': self.diadasemana, 'hora': self.hora,'periodo': self.periodo}
    
    @staticmethod
    def get_all_eventos(offset, limit):
        #return [Eventos.json(evento) for evento in Eventos.query.paginate(offset,limit,error_out=False)]
        query = Eventos.query.paginate(offset,limit,error_out=False)
        #print(query.items)
        return query.items

    @staticmethod
    def get_evento_by_codigo_concorrente(_codigo_concorrente, offset, limit):
        query = Eventos.query.filter_by(codigo_concorrente=_codigo_concorrente).paginate(offset,limit,error_out=False)
        return query.items
    
    @staticmethod
    def get_evento_by_periodo(_periodo, offset, limit):
        query = Eventos.query.filter_by(periodo=_periodo).paginate(offset,limit,error_out=False)
        return query.items
    
    @staticmethod
    def get_evento_by_diadasemana(_diadasemana, offset, limit):
        query = Eventos.query.filter_by(diadasemana=_diadasemana).paginate(offset,limit,error_out=False)
        return query.items

    @staticmethod
    def add_eventos_td(conn):
        # load the data into a Pandas DataFrame
        # Lista de missing values:
        missing_values = ['n/a','na','--','.']
        #Lendo a base e passando a lista com os missing values:
        try:
            df = pd.read_csv('data/eventos_de_fluxo.csv', encoding='utf-8',delimiter=",", na_values=missing_values)
        except:
            df = pd.read_csv('data/eventos_de_fluxo.csv.gz', compression='gzip', encoding='utf-8',delimiter=",", na_values=missing_values)

        df.columns = ['codigo', 'data', 'codigo_concorrente']
        #removendo duplicados
        df = df.drop_duplicates(['codigo','data','codigo_concorrente'],keep= 'last')
        
        # convert the 'Date' column to datetime format
        df['data']= pd.to_datetime(df['data'], format='%Y-%m-%d %H:%M:%S.%f')

        #dia da semana
        dayOfWeek={0:'segunda-feira', 1:'terça-feira', 2:'quarta-feira', 3:'quinta-feira', 4:'sexta-feira', 5:'sábado', 6:'domingo'}
        df['diadasemana'] = df['data'].dt.dayofweek.map(dayOfWeek)
        
        #df['hora'] = df['data'].dt.strftime('%H').astype(int)
        df['hora'] = pd.to_datetime(df['data'], format='%H').dt.strftime('%H').astype(int)
        

        def fperiodo(x):
            x = int(x)
            if (x >= 0) and (x < 12):
                return 'manhã'
            elif (x >= 12) and (x < 18):
                return'tarde'
            elif (x >= 18) and (x < 24):
                return'noite'

        df['periodo'] = df['hora'].apply(fperiodo)

        df.to_sql('eventos', conn, if_exists='append', index = False, chunksize = 500000)
  
    def __repr__(self):
        evento_object = {
            'codigo': self.codigo,
            'data': str(self.data), 
            'codigo_concorrente': self.codigo_concorrente,
            'diadasemana': self.diadasemana,
            'hora': self.hora,
            'periodo': self.periodo
        }
        return json.dumps(evento_object)
