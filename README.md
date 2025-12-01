# Heart Disease Classification #
Generated using Copier template.

Author: Екатерина С.

## Structure

```
./
├── data/
│   ├── raw/           # Исходные данные
│   └── processed/     # Обработанные данные
├── notebooks/         # Jupyter notebooks
├── src/               # Исходный код
└── tests/			   # Тесты
```

## Setup

- установить необходимые для сетапа пакеты
```
pip install copier poetry
```

- создать проект через copier
```
copier copy ./my_ds_template my_project
cd my_project
```

- (опционально) создавать venv внутри проекта
```
poetry config virtualenvs.in-project true
```

- создать виртуальное окружение и установить зависимости
```
poetry install
```

- активировать виртуальное окружение
```
poetry shell
```

- установить pre-commit hooks
```
pre-commit install
```

## Docker

Чтобы собрать и запустить проект в Docker:

```
docker build -t Heart Disease Classification .
docker run -it --rm Heart Disease Classification
```