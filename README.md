
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

## Packages

- docs/
    - info about deploy this api in cloud.
    - a proposal for architecture in cloud for this api.
- src/
    - city/
        - API Route for question generation.
    - config/
        - Project global information used in code.
    - generativeai/
        - Integration with external Generative AI Apis.
        - Class integrated with OpenAI Chat GPT do generate text.
        - Class integrated with Dolphin in LM Studio Server to generate text.
    - weather/
        - Integration with external Weather api.
        - Class integrated with WTTR Api for get info about weather of a city.

## Installation/Running

> **Info**: Access Makefile to see all executables.

 1) Install project
 2) Run with python
 3) Run with docker
 4) Tests

-----

#### 1) Installation

Previous you have to installed:
- [Python3.10>=](https://www.python.org/downloads/)
- [Python3-pip](https://pip.pypa.io/en/stable/installation/)
- [Python3-virtualenv](https://docs.python.org/3/library/venv.html)

###### Installation

Clone the project

```bash
  git https://github.com/itzmatheus/fun-generativeai-weather-api api
```
Go to project directory

```bash
  cd api
```

Create .env file

```bash
  cp .env.sample .env
```

> **Info**: Access **.env** and add your informations.

#### 2) Run with python

Create virtualenv and activate it

```bash
  virtualenv env
```

```bash
  source env/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run locally
```bash
make run
# or
fastapi run
```

#### 3) Running with docker

Required [docker](https://docs.docker.com/engine/install/) with [compose](https://docs.docker.com/compose/) already installed

```bash
make docker-up
# or
docker compose --file docker-compose.development.yml up --build
```

#### 4) Run tests (required installation locally with python. Step 2)

```bash
make test
# or
pytest -v
```

## Environment Variables

To run this project, you will need to configure the following environment variables to your .env file

`OPENAI_API_KEY` - https://platform.openai.com/docs/quickstart
`LM_STUDIO_API_KEY`
`LM_STUDIO_BASE_URL`
`LM_STUDIO_MODEL`

> **Warning**: If you set LM_STUDIO_API_KEY, LM_STUDIO_BASE_URL and LM_STUDIO_MODEL values, the project not Open AI Implementation.


## Integrated locally with LM Studio Local Inference Server

This project have a class `src/generativeai/lmstudio/DolphinGenerativeAIText` that implement dolphin model (TheBloke/dolphin-2.2.1-mistral-7B-GGUF/dolphin-2.2.1-mistral-7b.Q5_K_M.gguf), so basically you have to configure the enviroments LM_STUDIO in .env, and the project adjust itsel to connect. Make sure you have started the server in LM Studio.

You can also create another interface to Gen AI Text implementing `src/src/generativeai/GenerativeAIText` model and configuring the factory `src/generativeai/GenerativeAITextFactory.py`.

[This tutorial](https://www.youtube.com/watch?v=m7PvtNHsUa8) will help you to how run locally LM Studio with a model.

## Tech Stack

**API Back End:** [FastAPI](https://fastapi.tiangolo.com/)

**GenerativeAI:** [OpenAPI - Chat GPT](https://platform.openai.com/docs/guides/text-generation)

**Weather API:** [WTTR](https://github.com/chubin/wttr.in)
