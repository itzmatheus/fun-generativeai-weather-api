
# Fun Weather Assistant API

Generate fun text about weather city from input input using Generative AI.

## Author

- [@Matheus Leite](https://www.github.com/itzmatheus)


## API Reference

#### Generate text
##### Request
```http
POST /city/question_generate
```
```json
{
    "entrada": "Joao Pessoa"
}
```

| Field     | Type     | Description                  |
| :-------- | :------- | :--------------------------- |
| `entrada` | `string` | Name of a city. **Required** |

###### Response
```json
{
  "saida": "Parece que em Joao Pessoa o sol resolveu fazer um intervalo entre as nuvens, deixando o clima parcialmente nublado. Será que ele está preparando uma surpresa? Só o tempo dirá!"
}
```

## Installation/Running

> **Info**: Access Makefile to see all executables.

 1) Run with python locally
 2) Run with docker
 3) Tests

-----

#### 1) Install project and run it with Python (Using Bash Terminal)

Previously you have to installed:
- [Python3.10>=](https://www.python.org/downloads/)
- [Python3-pip](https://pip.pypa.io/en/stable/installation/)
- [Python3-virtualenv](https://docs.python.org/3/library/venv.html)

###### Installation

```bash
~ git clone ... api
~ virtualenv env
~ source env/bin/activate
~ cd api
~ pip install -r requirements.txt
```
###### Configuration

Run locally
```bash
make run
# or
fastapi run
```
Run tests
```bash
make test
# or
pytest -v
```

#### 2) Running with docker

Required [docker](https://docs.docker.com/engine/install/) with [compose](https://docs.docker.com/compose/) already installed

```bash
make docker-up
# or
docker compose --file docker-compose.development.yml up --build
```

#### 3) Run tests

```bash
make test
# or
pytest -v
```

## Tech Stack

**API Back End:** [FastAPI](https://fastapi.tiangolo.com/)

**GenerativeAI:** [OpenAPI - Chat GPT](https://platform.openai.com/docs/guides/text-generation)

**Weather API:** [WTTR](https://github.com/chubin/wttr.in)
