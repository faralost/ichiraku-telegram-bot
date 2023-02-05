lint:
		flake8 . --max-line-length=127
		mypy bot.py

test: lint
		pytest --cov-report term-missing --cov
