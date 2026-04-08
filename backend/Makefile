.PHONY: run lint check-models

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

lint:
	python -m py_compile $(shell rg --files . -g '*.py')

check-models:
	python test_models_import.py
