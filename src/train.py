from pathlib import Path

import hydra
import joblib
import pandas as pd
from hydra.utils import instantiate
from omegaconf import DictConfig
from sklearn.model_selection import train_test_split


@hydra.main(config_path="../configs", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
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

    Path(train_cfg.model_dir).mkdir(exist_ok=True)
    joblib.dump(model, f"{train_cfg.model_dir}/model.pkl")


if __name__ == "__main__":
    main()
