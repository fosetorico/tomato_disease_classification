from dataclasses import dataclass
from pathlib import Path

# @dataclass is a simple way to create classes that are primarily used for storing data
# frozen=True makes the dataclass immutable, meaning you cannot modify its attributes after the object is created
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
