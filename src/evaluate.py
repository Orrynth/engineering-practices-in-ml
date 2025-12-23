import json
import pickle  # nosec B403

import pandas as pd
from sklearn.metrics import accuracy_score

DATA_PATH = "data/processed/heart_processed.csv"
MODEL_PATH = "models/model.pkl"
METRICS_PATH = "reports/metrics.json"


def main():
    df = pd.read_csv(DATA_PATH)

    X = df.drop("target", axis=1)
    y = df["target"]

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)  # nosec B301

    preds = model.predict(X)
    acc = accuracy_score(y, preds)

    metrics = {
        "accuracy": acc,
    }

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)


if __name__ == "__main__":
    main()
