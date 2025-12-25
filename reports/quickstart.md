## QuickStart

### Часть 1. Предварительная подготовка
0) понадобится системный Python, н.п. 3.11.9

1) устанавливаем pipx
python -m pip install --user pipx
python -m pipx ensurepath

2) устанавливаем необходимые для сетапа пакеты
pipx install poetry

---

### Часть 2. Клонирование репозитория и настройка окружения

0) рекомендую использовать git bash

1) клонируем репозиторий
git clone https://github.com/Orrynth/engineering-practices-in-ml.git

2) переходим в склонированную директорию проекта
cd engineering-practices-in-ml/

3) указываем poetry создавать venv локально
poetry config virtualenvs.in-project true

4) создаем виртуальное окружение и устанавливаем зависимости
poetry install

5) получить команду активации виртуального окружения
poetry env activate

6) выполнить полученную в п.5 команду для активации виртуального окружения

7) просмотр веток
git branch -a

---

### Часть 3. Проверка Работы №2

0) переключение на нужную ветку
git switch hw-2

1) устанавливаем dvc в poetry
poetry add dvc

2) подтягиваем индексы
dvc pull

3) скачиваем heart.csv с https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

4) помещаем его в папку data/raw

5) запускаем предобработку
dvc repro

6) запуск обучения
python src/train.py

7) запуск Mlflow
mlflow ui

8) переходим на http://127.0.0.1:5000/

9) выбираем эксперимент heart_disease

---

### Часть 4. Проверка Работы №3

0) переключение на нужную ветку
git switch hw-3

1) запуск обучения
python src/train.py

2) запуск Mlflow
mlflow ui

3) в эксперименте heart_disease находятся все 15 запусков

---

### Часть 5. Проверка Работы №4

0) удаление всех локальных изменений из hw-2
git reset --hard

1) переключение на нужную ветку
git switch hw-4

2) запуск обучения
python src/train.py model=gb

3) запуск Mlflow
mlflow ui

4) запуски находятся в эксперименте heart_disease_classification

---
