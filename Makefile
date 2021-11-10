default: qas

build-qas:
	@docker build -f Dockerfile -t recursive-dict-docker .

run-tests: build-qas
	@docker-compose up tests

run-notebook: build-qas
	@docker-compose up jupyterlab

black-linter: build-qas
	@docker-compose up black-linter

qas: black-linter run-tests
