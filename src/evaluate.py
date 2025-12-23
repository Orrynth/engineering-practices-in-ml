import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

DATA_PATH = "data/processed/heart_processed.csv"
MODEL_PATH = "models/model.pkl"


def main():
    df = pd.read_csv(DATA_PATH)

    X = df.drop("target", axis=1)
    y = df["target"]

    model = joblib.load(MODEL_PATH)

    preds = model.predict(X)
    acc = accuracy_score(y, preds)

    metrics = {"accuracy": acc}

    Path("reports").mkdir(exist_ok=True)
    with open("reports/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)


if __name__ == "__main__":
    main()
