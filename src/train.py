from pathlib import Path

import hydra
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"
MLFLOW_EXPERIMENT_NAME = "heart_disease_classification"


@hydra.main(config_path="../configs", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
    # MLflow setup
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

    with mlflow.start_run():
        # Логируем ВСЮ конфигурацию Hydra
        mlflow.log_params(OmegaConf.to_container(cfg, resolve=True))

        data_cfg = cfg.data
        train_cfg = cfg.training

        df = pd.read_csv(data_cfg.processed_path)

        X = df.drop(data_cfg.target_col, axis=1)
        y = df[data_cfg.target_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=train_cfg.test_size,
            random_state=train_cfg.random_state,
        )

        model = instantiate(cfg.model)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        # Логируем метрики
        mlflow.log_metric("accuracy", acc)

        # Логируем модель
        mlflow.sklearn.log_model(model, name="model")

        # Сохраняем модель локально (для DVC)
        Path(train_cfg.model_dir).mkdir(exist_ok=True)
        joblib.dump(model, f"{train_cfg.model_dir}/model.pkl")


if __name__ == "__main__":
    main()
