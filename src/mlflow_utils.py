from contextlib import contextmanager
from functools import wraps
from typing import Callable, Dict, Optional

import mlflow


@contextmanager
def mlflow_run(
    run_name: Optional[str] = None,
    tags: Optional[Dict[str, str]] = None,
):
    """
    Контекстный менеджер для MLflow run
    """
    with mlflow.start_run(run_name=run_name):
        if tags:
            mlflow.set_tags(tags)
        yield


def mlflow_experiment(
    run_name: str,
    tags: Optional[Dict[str, str]] = None,
):
    """
    Декоратор для автоматического логирования MLflow run
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with mlflow_run(run_name=run_name, tags=tags):
                return func(*args, **kwargs)

        return wrapper

    return decorator


def log_common_params(params: Dict):
    """
    Логирование стандартных параметров эксперимента
    """
    for key, value in params.items():
        mlflow.log_param(key, value)
