import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.mlflow_utils import log_common_params, mlflow_experiment

# ======================
# Константы конфигурации
# ======================
EXPERIMENT_NAME = "heart_disease"
TRACKING_URI = "sqlite:///mlflow.db"
RANDOM_STATE = 42
DATA_PATH = "data/processed/heart_processed.csv"


def load_data(path: str):
    """Загрузка и разделение данных на признаки и целевую переменную"""
    df = pd.read_csv(path)
    X = df.drop("target", axis=1)
    y = df["target"]
    return X, y


@mlflow_experiment(
    run_name="training_run",
    tags={"project": "heart_disease", "task": "classification"},
)
def train_and_log(
    model_name: str,
    model_cls,
    params: dict,
    X_train,
    X_test,
    y_train,
    y_test,
):
    """Обучение модели и логирование результатов в MLflow"""

    model = model_cls(**params)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Логирование параметров и метрик
    log_common_params(
        {
            "model_name": model_name,
            **params,
        }
    )

    mlflow.log_metric("accuracy", acc)

    # Логирование модели как артефакта
    mlflow.sklearn.log_model(model, name="model")


def main():
    # Настройка MLflow
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)

    # Загрузка данных
    X, y = load_data(DATA_PATH)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
    )

    # План экспериментов (15 запусков)
    experiments = (
        [
            (
                "rf",
                RandomForestClassifier,
                {"n_estimators": n, "random_state": RANDOM_STATE},
            )
            for n in [50, 100, 200, 300, 500]
        ]
        + [
            ("lr", LogisticRegression, {"C": c, "max_iter": 1000})
            for c in [0.01, 0.1, 1, 10, 100]
        ]
        + [
            (
                "gb",
                GradientBoostingClassifier,
                {"n_estimators": n, "random_state": RANDOM_STATE},
            )
            for n in [50, 100, 200, 300, 500]
        ]
    )

    # Запуск экспериментов
    for model_name, model_cls, params in experiments:
        train_and_log(
            model_name=model_name,
            model_cls=model_cls,
            params=params,
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
            y_test=y_test,
        )


if __name__ == "__main__":
    main()
