.PHONY: install venv activate run_tests start build

# Створення віртуального середовища
venv:
    python -m venv .venv

# Активація середовища (для PowerShell)
activate:
    . .venv/Scripts/Activate.ps1
deactivate:
	deactivate

# Запуск тестів
run_tests:
    pytest

# Запуск програми
start:
    python main.py

# Створення проекту
build:
    python setup.py install
