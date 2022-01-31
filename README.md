# SISTEMA DE GERENCIAMENTO E LOCAÇÃO DE LIVROS
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

Change `/frontend/.env.production` to your machine ip with port 8000

Build and run the docker-compose in root folder:
```sh
docker-compose up --build -d
```

The system will be available at "yourip:9000"

To change password run the command below in the api container :

```sh
flask change-password mynewpassword
```
