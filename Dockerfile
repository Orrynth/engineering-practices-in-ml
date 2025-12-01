# Dockerfile
FROM python:3.11-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Копируем pyproject.toml и poetry.lock
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем poetry
RUN pip install --no-cache-dir poetry

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Копируем весь проект
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Опционально: задаём команду по умолчанию
CMD ["python"]
