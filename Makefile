.PHONY: run test lint format typecheck check

run:
	uv run uvicorn app.main:app --reload

test:
	uv run pytest -v

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check . --fix
	uv run ruff format .

typecheck:
	uv run mypy app tests

check: lint typecheck test