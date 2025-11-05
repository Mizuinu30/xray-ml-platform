"""Simple skeleton data loader for the Chest X-Ray Pneumonia pipeline.

This file provides a minimal implementation to allow end-to-end
dry-runs and unit tests. Replace with production-ready data loading
and augmentation later.
"""
from pathlib import Path
from typing import Dict, Any


class PneumoniaDataLoader:
    def __init__(self, raw_dir: str = "data/raw"):
        self.raw_dir = Path(raw_dir)

    def load_metadata(self) -> Dict[str, Any]:
        """Return a minimal metadata structure describing the dataset.

        For the skeleton we return a dict with counts per split/class. In
        a full implementation this would return a pandas.DataFrame.
        """
        # basic, safe representation
        meta = {
            "splits": {
                "train": {"NORMAL": 0, "PNEUMONIA": 0},
                "val": {"NORMAL": 0, "PNEUMONIA": 0},
                "test": {"NORMAL": 0, "PNEUMONIA": 0},
            },
            "raw_dir": str(self.raw_dir)
        }
        return meta

    def analyze_dataset_balance(self, metadata: Dict[str, Any]) -> None:
        """Print a short summary of class balance (skeleton)."""
        print("Dataset metadata summary:")
        splits = metadata.get("splits", {})
        for split, classes in splits.items():
            total = sum(classes.values())
            print(f"  {split}: total={total}, breakdown={classes}")

    def create_data_generators(self, metadata: Dict[str, Any], batch_size: int = 32, target_size=(224, 224)) -> Dict[str, Any]:
        """Return simple placeholder generators/datasets.

        The real project should return Keras/TensorFlow generators or PyTorch
        Datasets. For testing we return small lists that act like iterables.
        """
        # Create small placeholder lists for train/val/test
        generators = {
            "train": [(None, None)] * 2,
            "val": [(None, None)] * 1,
            "test": [(None, None)] * 1,
        }
        return generators


if __name__ == "__main__":
    loader = PneumoniaDataLoader()
    meta = loader.load_metadata()
    loader.analyze_dataset_balance(meta)
    gens = loader.create_data_generators(meta)
    print("Generators keys:", list(gens.keys()))
