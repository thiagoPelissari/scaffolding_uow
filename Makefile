export PYTHONPATH=$(shell pwd)/src/
export API_PORT=5000

.PHONY: migrations


run-api:
	poetry run uvicorn my_project_uow.entrypoints.http_api.main:app --host 0.0.0.0 --port $(API_PORT) --reload

migrations:
	poetry run alembic -c ./migrations/alembic.ini revision --autogenerate -m "$(MESSAGE)"

migrate:
	poetry run alembic -c ./migrations/alembic.ini upgrade head