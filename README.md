﻿# SISTEMA DE GERENCIAMENTO E LOCAÇÃO DE LIVROS
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
<img src="https://img.shields.io/badge/vue-2.6.11-brightgreen.svg" alt="vue">

<h4 align="center"> 
	🚧   Under development...  🚧
</h4>

### Requirements

You need to have the following tools installed on your machine:
[Git](https://git-scm.com), [Docker](https://www.docker.com/), 
and [Docker-Compose](https://docs.docker.com/compose/install/)

## Get Start
```sh
git clone https://github.com/MDoreto/Biblioteca.git
```

Change `/frontend/.env.production` value according to your api address with the same port in the next step

Build and run the docker-compose in root folder:
```sh
docker-compose up --build -d
```

For Defaults the api will run on the port 8000, and the ui on the port 9000

In the first deploy:

And to create tables:

```sh
docker exec -it odin flask seed
```

### API_DOCS 

The swagger apidocs is avaliable in `/apidocs` endpoint in api
