import json
import pandas as pd

from db_config import db
#import sqlite3 as sqlite3

#connN = sqlite3.connect('database/database.db')

#load precompiled json1 extension
#connN.enable_load_extension(True)
#connN.load_extension("./json1")


import json

class modelo_json:
	def json(self):
		return dict({ "cod_concorrente":"", "nome_concorrente":"", "seguimento":"", "endereco":"", "preco_praticado":"",
				"fluxo_medio":{ "segunda-feira":{	"manhã":0,	"tarde":0,	"noite":0 }, 
										"terça-feira":{	"manhã":0, "tarde":0, "noite":0 },
										"quarta-feira":{ "manhã":0, "tarde":0, "noite":0},
										"quinta-feira":{ "manhã":0, "tarde":0, "noite":0},
										"sexta-feira":{ "manhã":0, "tarde":0, "noite":0},
										"sábado":{ "manhã":0, "tarde":0, "noite":0 },
										"domingo":{ "manhã":0, "tarde":0, "noite":0}    
									},
				"bairro":"", "populacao":0,	"densidade":0 })

class Relatorio():
	@staticmethod
	def get_relatorio(_codigo_concorrente):
		query = ("SELECT \
			c.codigo as cod_concorrente, \
			c.nome as nome_concorrente, \
			c.categoria_json as seguimento,\
			c.endereco as endereco, \
			pp.descricao as preco_praticado,  \
			b.nome as bairro, \
			b.municipio,  \
			b.uf, \
			b.area, \
			p.populacao, \
			ROUND(CAST (p.populacao AS FLOAT) / CAST(b.area AS FLOAT),1) as densidade, \
			e.diadasemana,  \
			e.periodo,  \
			count(*)qtd, \
			z.dtq_semana, \
			ROUND(count(*)/CAST(z.dtq_semana AS FLOAT),2)fluxo_pessoas_periodo \
			from concorrentes c \
			inner join eventos e on e.codigo_concorrente = c.codigo \
			inner join bairros b on b.codigo = c.codigo_bairro \
			inner join populacoes p on p.codigo = b.codigo \
			left join precopraticados pp on pp.faixa_preco = c.faixa_preco  \
			inner join (\
		  select codigo codigo_concorrente, diadasemana, periodo, count(distinct dia) dtq_semana from (\
		  select c1.codigo, c1.nome , e1.diadasemana, e1.periodo, strftime('%d%m%Y', `data`)  dia\
		  from concorrentes c1\
		  inner join eventos e1 on e1.codigo_concorrente = c1.codigo\
		  where c1.codigo='{0}' ) group by codigo, diadasemana,periodo\
	    ) z on z.codigo_concorrente = c.codigo and z.diadasemana = e.diadasemana and z.periodo = e.periodo\
			where c.codigo='{0}'\
			group by  \
			c.codigo, c.nome , b.nome, b.municipio, b.uf, b.area, p.populacao,ROUND(CAST (p.populacao AS FLOAT) / CAST(b.area AS FLOAT),1), \
			e.diadasemana,  e.periodo, z.dtq_semana").format(_codigo_concorrente)

		cursor = db.session.execute(query)
		cursor = cursor.fetchall()
	
		json_object = modelo_json().json()

		for item in cursor:
			json_object.update({"cod_concorrente": item["cod_concorrente"]})
			json_object.update({"nome_concorrente": item["nome_concorrente"]})
			json_object.update({"seguimento": item["seguimento"]})
			json_object.update({"endereco": item["endereco"]})
			json_object.update({"preco_praticado": item["preco_praticado"]})
			json_object.update({"bairro": item["bairro"]})
			json_object.update({"populacao": item["populacao"]})
			json_object.update({"densidade": item["densidade"]})

			if item["diadasemana"] == "segunda-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["segunda-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["segunda-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["segunda-feira"]["noite"]=item["fluxo_pessoas_periodo"]
			
			elif item["diadasemana"] == "terça-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["terça-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["terça-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["terça-feira"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "quarta-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["quarta-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["quarta-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["quarta-feira"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "quinta-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["quinta-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["quinta-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["quinta-feira"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "sexta-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["sexta-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["sexta-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["sexta-feira"]["noite"]=item["fluxo_pessoas_periodo"]
				
			elif item["diadasemana"] == "sábado":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["sábado"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["sábado"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["sábado"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "domingo":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["domingo"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["domingo"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["domingo"]["noite"]=item["fluxo_pessoas_periodo"]
		
		if not cursor:
			return json.dumps({"status":"dados não encontrado"})
		else:
			return json.dumps(json_object)
	
	@staticmethod
	def get_comparativoseguimento(_categoria):
		aux_where = "" 
		for i, x in enumerate(_categoria.split(',')):
			if i==0:
				aux_where +="c.categoria_json LIKE '%{0}%' ".format(x) 
			else:
				aux_where +=" or c.categoria_json LIKE '%{0}%' ".format(x) 
			#if i==0:
			#	aux_where +="json_each.value LIKE '{0}' ".format(x) 
			#else:
			#	aux_where +=" or json_each.value LIKE '{0}' ".format(x) 	

		query = "SELECT \
			c.codigo as cod_concorrente, \
			c.nome as nome_concorrente, \
			c.categoria_json as seguimento,\
			c.endereco as endereco, \
			pp.descricao as preco_praticado,  \
			b.nome as bairro, \
			b.municipio,  \
			b.uf, \
			b.area, \
			p.populacao, \
			ROUND(CAST (p.populacao AS FLOAT) / CAST(b.area AS FLOAT),1) as densidade, \
			e.diadasemana,  \
			e.periodo,  \
			count(*)qtd, \
			z.dtq_semana, \
			ROUND(count(*)/CAST(z.dtq_semana AS FLOAT),2)fluxo_pessoas_periodo \
			from concorrentes c \
			inner join eventos e on e.codigo_concorrente = c.codigo \
			inner join bairros b on b.codigo = c.codigo_bairro \
			inner join populacoes p on p.codigo = b.codigo \
			left join precopraticados pp on pp.faixa_preco = c.faixa_preco  \
			inner join ( \
		  select codigo codigo_concorrente, diadasemana, periodo, count(distinct dia) dtq_semana from ( \
		  select c1.codigo, c1.nome , e1.diadasemana, e1.periodo, strftime('%d%m%Y', `data`)  dia \
		  from concorrentes c1 \
		  inner join eventos e1 on e1.codigo_concorrente = c1.codigo \
		  ) group by codigo, diadasemana,periodo \
	    ) z on z.codigo_concorrente = c.codigo and z.diadasemana = e.diadasemana and z.periodo = e.periodo \
			where {0} group by  \
			c.codigo, c.nome , b.nome, b.municipio, b.uf, b.area, p.populacao,ROUND(CAST (p.populacao AS FLOAT) / CAST(b.area AS FLOAT),1), \
			e.diadasemana,  e.periodo, z.dtq_semana order by c.codigo".format(aux_where)
		
		#clausula retirda devido problemas na configuração do json1 do sqlite3
		#serve para pesquisa nas categorias
		#where (SELECT DISTINCT concorrentes.codigo FROM concorrentes,json_each(concorrentes.categoria_json) 
		#			WHERE json_valid(concorrentes.categoria_json)	AND ({0})) 

		cursor = db.session.execute(query)
		cursor = cursor.fetchall()
		
		json_object_default = []
		
		cod_concorrente=""
		tamMaximo = len(cursor)

		json_object = modelo_json().json()

		for index, item in enumerate(cursor):
			if index == 0:
				cod_concorrente = item['cod_concorrente']
			
			if cod_concorrente != item['cod_concorrente']:
				json_object_default.append(json_object)
				cod_concorrente = item['cod_concorrente']
				
				json_object = modelo_json().json()

			json_object.update({"cod_concorrente": item["cod_concorrente"]})
			json_object.update({"nome_concorrente": item["nome_concorrente"]})
			json_object.update({"seguimento": item["seguimento"]})
			json_object.update({"endereco": item["endereco"]})
			json_object.update({"preco_praticado": item["preco_praticado"]})
			json_object.update({"bairro": item["bairro"]})
			json_object.update({"populacao": item["populacao"]})
			json_object.update({"densidade": item["densidade"]})

			if item["diadasemana"] == "segunda-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["segunda-feira"]["manhã"]=item["fluxo_pessoas_periodo"] 
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["segunda-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["segunda-feira"]["noite"]=item["fluxo_pessoas_periodo"]
			
			elif item["diadasemana"] == "terça-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["terça-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["terça-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["terça-feira"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "quarta-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["quarta-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["quarta-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["quarta-feira"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "quinta-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["quinta-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["quinta-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["quinta-feira"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "sexta-feira":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["sexta-feira"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["sexta-feira"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["sexta-feira"]["noite"]=item["fluxo_pessoas_periodo"]
				
			elif item["diadasemana"] == "sábado":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["sábado"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["sábado"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["sábado"]["noite"]=item["fluxo_pessoas_periodo"]

			elif item["diadasemana"] == "domingo":
				if item["periodo"] == "manhã":
					json_object["fluxo_medio"]["domingo"]["manhã"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "tarde":
					json_object["fluxo_medio"]["domingo"]["tarde"]=item["fluxo_pessoas_periodo"]
				elif item["periodo"] == "noite":
					json_object["fluxo_medio"]["domingo"]["noite"]=item["fluxo_pessoas_periodo"]
			
			cod_concorrente = item['cod_concorrente']	
			
			if index == tamMaximo-1:
				json_object_default.insert(index, json_object)
		
		if not cursor:
			return json.dumps({"status":"dados não encontrado"})
		else:
			return json.dumps(json_object_default)