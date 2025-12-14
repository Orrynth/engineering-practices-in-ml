# Heart Disease Classification #
**Проект**: Heart Disease Classification

**Цель**: разработать и оценить модель машинного обучения, которая предсказывает наличие сердечного заболевания у пациента на основе клинических данных.

**Автор**: Екатерина С.

## Structure

```
./
├── data/
│   ├── raw/           # Исходные данные
│   └── processed/     # Обработанные данные
├── notebooks/         # Jupyter notebooks
├── reports/ 		   # Отчеты
├── src/               # Исходный код
├── tests/			   # Тесты
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Setup

- установить pipx (рекомендуется)
```
python -m pip install --user pipx
python -m pipx ensurepath
```

- установить необходимые для сетапа пакеты
```
pipx install poetry
pipx install copier
pipx install pre-commit

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
poetry env activate
```

- установить pre-commit hooks
```
pre-commit install
```

## Docker

Чтобы собрать и запустить проект в Docker:

```
docker build -t {{ project_name }} .
docker run -it --rm {{ project_name }}
```
