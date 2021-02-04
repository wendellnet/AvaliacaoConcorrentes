# api-avaliacao-concorrentes
Este projeto api foi construido com flask e python

[![Build Status](https://travis-ci.com/wendellnet/AvaliacaoConcorrentes.svg?token=2Nz1ALo2tCVY7ZXLxTE3&branch=master)](https://travis-ci.com/wendellnet/AvaliacaoConcorrentes)

![Heroku](https://pyheroku-badge.herokuapp.com/?app=acompanhamento-concorrentes&style=flat)

Introdução
------------
Objetivo desde projeto é implementar uma aplicação que entregue os resultados após analise de eventos que indicam fluxos de pessoas em estabelecimentos comerciais.

Utilizei linguagem Python com Flask e interface swagger.

Este serviço armazena seus dados em banco de dados sqlite.

Instalando Dependências
-----
[Este projeto usa ambiente virtual Pipenv.](https://pipenv.readthedocs.io)

Se você tiver o MacOS, instale as dependências pelo homebrew:

`brew install pipenv`

Rode o comando abaixo para instalar as dependências locais em seu computador:

`pipenv install`


Executando a aplicação
----------------------
Após você ter instalado todas dependências, você deve abrir um terminal de comandos e executar o comando abaixo:
Entre na pasta root deste projeto e digite:
`pipenv run python app.py`

Ou você pode iniciar a aplicação usando a sua IDE preferida, PyCharm, VSCode.


Database
--------
Este projeto usa uma base local SQLITE (database.db) para seu repositório.  

Interface
---------
Este projeto contêm uma inteface(UI) SWAGGER.  

[Para maiores informações sobre swagger. Clique aqui.](https://swagger.io/)

[Para maiores informações sobre connexion. Clique aqui.](https://connexion.readthedocs.io/en/latest/)

Para visualizar esta aplicação api swagger, execute e navegue para endereço [http://localhost:5000/ui/]

Você pode testar esta aplicação entrando no endereço web abaixo. 

Deploy dessa aplicação está sendo realizado no [heroku](https://www.heroku.com/).  
Para visualizar está api, navegue para [https://acompanhamento-concorrentes.herokuapp.com/ui/]

Rest Api 
--------
####  [Avaliação de concorrentes] representação das informações sobre fluxos de pessoas;
GET - get_avaliacao_concorrente: [/avaliacao/v1](http://localhost:5000/avaliacao/v1)

####  [Avaliação por seguimento] representação comparativa das empresas por seguimento de atuação;
GET - get_comparativo_seguimento: [/avaliacao/v1/seguimento](http://localhost:5000/avaliacao/v1/seguimento)

####  [Bairros] representa cadastro de municipios;
GET - get_all_bairros: [/bairros/v1](http://localhost:5000/bairros/v1)
GET - get_by_bairro: [/bairros/v1/{codigo}](http://localhost:5000/bairros/v1/{codigo})
GET - get_by_bairro_uf: [/bairros/v1/uf](http://localhost:5000/bairros/v1/uf)
GET - get_by_bairro_nome: [/bairros/v1/nome](http://localhost:5000/bairros/v1/nome)
GET - get_by_bairro_municipio: [/bairros/v1/municipio](http://localhost:5000/bairros/v1/municipio)

####  [Concorrentes] representa cadastro de empresas;
GET - get_all_concorrentes: [/concorrentes/v1](http://localhost:5000/concorrentes/v1)
GET - get_by_concorrente: [/concorrentes/v1/{codigo}](http://localhost:5000/concorrentes/v1/{codigo})
GET - get_by_concorrente_uf: [/concorrentes/v1/uf](http://localhost:5000/concorrentes/v1/uf)
GET - get_by_concorrente_nome: [/concorrentes/v1/nome](http://localhost:5000/concorrentes/v1/nome)
GET - get_by_concorrente_municipio: [/concorrentes/v1/municipio](http://localhost:5000/concorrentes/v1/municipio)
GET - get_by_concorrente_codigo_bairro: [/concorrentes/v1/codigobairro](http://localhost:5000/concorrentes/v1/codigobairro)

####  [Eventos] representa os logs coletados dos concorrenstes;
GET - get_all_eventos: [/eventos/v1](http://localhost:5000/eventos/v1)
GET - get_by_evento_codigo_concorrente: [/eventos/v1/concorrente](http://localhost:5000/eventos/v1/concorrente)
GET - get_by_evento_diadasemana: [/eventos/v1/diadasemana](http://localhost:5000/eventos/v1/diadasemana)
GET - get_by_evento_periodo: [/eventos/v1/periodo](http://localhost:5000/eventos/v1/periodo)

####  [Preco praticado] representa uma rota para cadastro de preços dos concorrentes;
GET - get_precopraticado: [/precopraticado/v1](http://localhost:5000/precopraticado/v1)
POST - add_precopraticado: [/precopraticado/v1](http://localhost:5000/precopraticado/v1)
GET - get_by_faixa_preco: [/precopraticado/v1/{faixa_preco}](http://localhost:5000/precopraticado/v1/{faixa_preco})
PUT - update_descricao: [/precopraticado/v1/{faixa_preco}](http://localhost:5000/precopraticado/v1/{faixa_preco})
PUT - delete_precopraticado: [/precopraticado/v1/{faixa_preco}](http://localhost:5000/precopraticado/v1/{faixa_preco})

####  [Populacao] representa quantidade da população de cada bairro;
GET - get_all_populacoes: [/populacoes/v1](http://localhost:5000/populacoes/v1)
GET - get_by_populacao: [/populacoes/v1/{codigo}](http://localhost:5000//populacoes/v1/{codigo})

## Rotas publicadas
-------------------
####  [Avaliação de concorrentes] representação das informações sobre fluxos de pessoas;
GET - get_avaliacao_concorrente: [/avaliacao/v1](https://acompanhamento-concorrentes.herokuapp.com/avaliacao/v1)

####  [Avaliação por seguimento] representação comparativa das empresas por seguimento de atuação;
GET - get_comparativo_seguimento: [/avaliacao/v1/seguimento](https://acompanhamento-concorrentes.herokuapp.com/avaliacao/v1/seguimento)

####  [Bairros] representa cadastro de municipios;
GET - get_all_bairros: [/bairros/v1](https://acompanhamento-concorrentes.herokuapp.com/bairros/v1)
GET - get_by_bairro: [/bairros/v1/{codigo}](https://acompanhamento-concorrentes.herokuapp.com/bairros/v1/{codigo})
GET - get_by_bairro_uf: [/bairros/v1/uf](https://acompanhamento-concorrentes.herokuapp.com/bairros/v1/uf)
GET - get_by_bairro_nome: [/bairros/v1/nome](https://acompanhamento-concorrentes.herokuapp.com/bairros/v1/nome)
GET - get_by_bairro_municipio: [/bairros/v1/municipio](https://acompanhamento-concorrentes.herokuapp.com/bairros/v1/municipio)

####  [Concorrentes] representa cadastro de empresas;
GET - get_all_concorrentes: [/concorrentes/v1](https://acompanhamento-concorrentes.herokuapp.com/concorrentes/v1)
GET - get_by_concorrente: [/concorrentes/v1/{codigo}](https://acompanhamento-concorrentes.herokuapp.com/concorrentes/v1/{codigo})
GET - get_by_concorrente_uf: [/concorrentes/v1/uf](https://acompanhamento-concorrentes.herokuapp.com/concorrentes/v1/uf)
GET - get_by_concorrente_nome: [/concorrentes/v1/nome](https://acompanhamento-concorrentes.herokuapp.com/concorrentes/v1/nome)
GET - get_by_concorrente_municipio: [/concorrentes/v1/municipio](https://acompanhamento-concorrentes.herokuapp.com/concorrentes/v1/municipio)
GET - get_by_concorrente_codigo_bairro: [/concorrentes/v1/codigobairro](https://acompanhamento-concorrentes.herokuapp.com/concorrentes/v1/codigobairro)

####  [Eventos] representa os logs coletados dos concorrentes;
GET - get_all_eventos: [/eventos/v1](https://acompanhamento-concorrentes.herokuapp.com/eventos/v1)
GET - get_by_evento_codigo_concorrente: [/eventos/v1/concorrente](https://acompanhamento-concorrentes.herokuapp.com/eventos/v1/concorrente)
GET - get_by_evento_diadasemana: [/eventos/v1/diadasemana](https://acompanhamento-concorrentes.herokuapp.com/eventos/v1/diadasemana)
GET - get_by_evento_periodo: [/eventos/v1/periodo](https://acompanhamento-concorrentes.herokuapp.com/eventos/v1/periodo)

####  [Preco praticado] representa uma rota para cadastro de preços dos concorrentes;
GET - get_precopraticado: [/precopraticado/v1](https://acompanhamento-concorrentes.herokuapp.com/precopraticado/v1)
POST - add_precopraticado: [/precopraticado/v1](https://acompanhamento-concorrentes.herokuapp.com/precopraticado/v1)
GET - get_by_faixa_preco: [/precopraticado/v1/{faixa_preco}](https://acompanhamento-concorrentes.herokuapp.com/precopraticado/v1/{faixa_preco})
PUT - update_descricao: [/precopraticado/v1/{faixa_preco}](https://acompanhamento-concorrentes.herokuapp.com/precopraticado/v1/{faixa_preco})
PUT - delete_precopraticado: [/precopraticado/v1/{faixa_preco}](https://acompanhamento-concorrentes.herokuapp.com/precopraticado/v1/{faixa_preco})

####  [Populacao] representa quantidade da população de cada bairro;
GET - get_all_populacoes: [/populacoes/v1](https://acompanhamento-concorrentes.herokuapp.com/populacoes/v1)
GET - get_by_populacao: [/populacoes/v1/{codigo}](https://acompanhamento-concorrentes.herokuapp.com//populacoes/v1/{codigo})



TDD - Testes Integrados
-----------------------
Esta API é totalmente testada com testes de unidade e testes de integração. Por favor, veja o diretório de testes para exemplos.

Os testes se conectam a test.db para testes de integração.

    
Flask 
-----
Este é um projeto Flask. [Para mais informações clique aqui](http://flask.pocoo.org/)
    
    
Docker
-----
seu aplicativo pode ser executado no Docker. Consulte Dockerfile para configuração de imagem. Passos para criar uma imagem e como executá-la o aplicativo em uma lista de contêineres abaixo. (deve ter docker instalado)

Criando a Imagem Docker: `docker build -t avaliacao-concorrentes-api .`

Executando o container docker: `docker run -it -p 5000:5000 avaliacao-concorrentes-api`

__*** Assim que o aplicativo for iniciado, visualize o swagger ui navegando até [http://localhost:5000/ui/] ***__

Visualizando imagem docker: `docker images`

Visualizando containes docker: `docker ps -a`

Remover imagem docker: `docker rmi $(docker images -q)`

Remover container docker: `docker rm $(docker ps -aq)`

[Clique aqui para obter mais informações sobre o docker](https://docs.docker.com/)

__* Nota: este aplicativo flask por padrão é executado como um servidor de desenvolvimento, não destinado à produção. Docker e gunicorn é usado para produzir este aplicativo. Este contêiner docker funciona como um servidor WSGI de produção, com 4 trabalhadores via [gunicorn](https://gunicorn.org/). *__

   
Integração Continua(CI)
-----------------------
Um web hook foi configurado com o Travis CI para todas as solicitações push e pull.

Um web hook também foi configurado com Github Actions para todas as solicitações Push e Pull. 

Implantação Contínua(CD)
------------------------
Este aplicativo está configurado para implantar via [heroku] (https://www.heroku.com/) após uma CI bem-sucedida.

Para visualizar o deploy [clique aqui](https://acompanhamento-concorrentes.herokuapp.com/ui/)

Contato / Questões / Contribuição
---------------------------------
Sinta-se à vontade para bifurcar este repositório, adicionar a ele e criar uma solicitação pull se desejar contribuir.

Se você tiver alguma dúvida, pode entrar em contato comigo por e-mail: `wendell.lopes.nascimento@gmail.com`
