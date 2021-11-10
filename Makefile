default: lint

build-tests:
	@docker build . --target=recursive-dict-tests -t recursive-dict-tests

run-tests: build-tests
	@docker-compose run recursive-dict-tests tests

lint:
	@flake8 . --ignore=W503
