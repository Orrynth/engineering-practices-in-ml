from dataclasses import dataclass


@dataclass
class DataConfig:
    raw_path: str
    processed_path: str
    target_col: str


@dataclass
class TrainingConfig:
    test_size: float
    random_state: int
    model_dir: str
