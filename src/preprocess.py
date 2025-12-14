from pathlib import Path

import pandas as pd

df = pd.read_csv("data/raw/heart.csv")
df = df.drop_duplicates()

Path("data/processed").mkdir(exist_ok=True)
df.to_csv("data/processed/heart_processed.csv", index=False)
