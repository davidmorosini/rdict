default: lint test

lint:
	@flake8 . --ignore=W503

test:
	@tox
