default: lint

build-tests:
	@docker build . --target=recursive-dict-tests -t recursive-dict-tests

run-unit-test:
	@docker-compose run recursive-dict-tests tests

lint:
	@flake8 . --ignore=W503
