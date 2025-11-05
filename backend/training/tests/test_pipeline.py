import unittest
import os
from pathlib import Path

from backend.training.pneumonia_data_loader import PneumoniaDataLoader
from backend.training.pneumonia_trainer import PneumoniaModelTrainer


class PipelineSkeletonTests(unittest.TestCase):
    def setUp(self):
        # Ensure model dir is in a temp area under repo
        self.repo_root = Path.cwd()
        self.model_dir = Path("models/pneumonia")
        if self.model_dir.exists():
            # clean up any leftover placeholder files
            for p in self.model_dir.iterdir():
                try:
                    p.unlink()
                except Exception:
                    pass

    def test_data_loader_returns_metadata_and_generators(self):
        loader = PneumoniaDataLoader(raw_dir="data/raw")
        meta = loader.load_metadata()
        self.assertIsInstance(meta, dict)
        loader.analyze_dataset_balance(meta)  # should not raise
        gens = loader.create_data_generators(meta, batch_size=2)
        self.assertIsInstance(gens, dict)
        self.assertIn('train', gens)
        self.assertIn('val', gens)

    def test_trainer_train_and_evaluate(self):
        trainer = PneumoniaModelTrainer(model_dir=str(self.model_dir))
        model, history = trainer.train([], [], epochs=1)
        self.assertIsNotNone(model)
        self.assertIsInstance(history, dict)
        # check model files exist
        self.assertTrue((self.model_dir / "pneumonia_best_model.h5").exists())
        self.assertTrue((self.model_dir / "pneumonia_final_model.h5").exists())
        results = trainer.evaluate_model([])
        self.assertIsInstance(results, dict)
        self.assertIn('test_accuracy', results)


if __name__ == '__main__':
    unittest.main()
