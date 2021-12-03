default: qas

build-qas:
	@docker build -f Dockerfile -t qas .

run-tests: build-qas
	@docker-compose up tests

black-linter: build-qas
	@docker-compose up black-linter

qas: black-linter run-tests
