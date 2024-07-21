run:
	fastapi run

test:
	pytest -v

docker-up:
	docker compose --file docker-compose.development.yml up --build

docker-downm:
	docker compose --file docker-compose.development.yml down

docker-build:
	docker build -t generative-api . -f Dockerfile

docker-run:
	docker run --rm -it -p 8000:8000 generative-api

docker-clean:
	docker rmi generative-api