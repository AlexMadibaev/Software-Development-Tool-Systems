# GitHub Actions Workflow: Run Python Tests

Этот workflow автоматически запускает модульные тесты Python при каждом push в ветку `main`.

## Описание

Этот workflow используется для автоматического запуска модульных тестов Python вашего проекта на платформе GitHub Actions. Он клонирует репозиторий, устанавливает необходимые зависимости из файла `requirements.txt` и запускает модульные тесты с помощью команды `python -m unittest discover -v`.

## Как это работает

1. **Checkout repository**: Действие `actions/checkout@v2` используется для клонирования репозитория в окружение GitHub Actions.

2. **Set up Python**: Действие `actions/setup-python@v2` используется для настройки версии Python.

3. **Install dependencies**: С помощью команды `pip install -r requirements.txt` устанавливаются необходимые зависимости из файла `requirements.txt`.

4. **Run unit tests**: Действие запускает модульные тесты Python с помощью команды `python -m unittest discover -v`.

## Как использовать

Чтобы включить этот workflow в ваш проект, добавьте файл `main.yml` в директорию `.github/workflows/` вашего репозитория с содержимым, аналогичным приведенному ниже:

```yaml
name: Run Python Tests

on:
  push:
    branches:
      - master

jobs:
  test:
    name: Run Python Tests
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run unit tests
      run: python -m unittest discover -v
```
