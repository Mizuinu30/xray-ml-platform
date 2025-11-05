#!/usr/bin/env python3
"""
Quick smoke test script to verify the pneumonia training skeleton works.

The production project is expected to replace the placeholder components in
``pneumonia_data_loader`` and ``pneumonia_trainer``. Until then, this script
exercises the lightweight scaffolding so contributors can confirm their Python
environment is wired correctly.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Iterable, Mapping, Tuple

# Ensure the training package directory is importable when the script is run
# from the repository root or the ``backend`` folder.
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))


def _import_data_loader():
    try:
        from pneumonia_data_loader import PneumoniaDataLoader  # type: ignore
    except ImportError:  # pragma: no cover - fallback for alternate invocations
        from backend.training.pneumonia_data_loader import PneumoniaDataLoader  # type: ignore
    return PneumoniaDataLoader


def _import_trainer():
    try:
        from pneumonia_trainer import PneumoniaModelTrainer  # type: ignore
    except ImportError:  # pragma: no cover - fallback for alternate invocations
        from backend.training.pneumonia_trainer import PneumoniaModelTrainer  # type: ignore
    return PneumoniaModelTrainer


def _describe_batch_value(value: Any) -> str:
    if value is None:
        return "placeholder None"
    shape = getattr(value, "shape", None)
    if shape is not None:
        return f"shape={shape}"
    return f"type={type(value).__name__}"


def test_data_loading() -> bool:
    """Exercise the placeholder data loader."""
    print("🧪 Testing Data Pipeline...")
    print("=" * 50)

    try:
        PneumoniaDataLoader = _import_data_loader()
        data_loader = PneumoniaDataLoader()

        print("📊 Loading metadata...")
        metadata = data_loader.load_metadata()
        if not isinstance(metadata, Mapping):
            print("❌ FAIL: Expected metadata mapping, got", type(metadata))
            return False

        splits = metadata.get("splits", {})
        total_images = 0
        if isinstance(splits, Mapping):
            for split_name, class_counts in splits.items():
                if isinstance(class_counts, Mapping):
                    split_total = sum(class_counts.values())
                    total_images += split_total
                    print(f"  {split_name}: total={split_total}, breakdown={class_counts}")
        print(f"✅ SUCCESS: Loaded placeholder metadata (total images reported: {total_images})")

        print("\n📈 Testing dataset analysis...")
        data_loader.analyze_dataset_balance(metadata)

        print("\n🔄 Testing data generators...")
        generators = data_loader.create_data_generators(
            metadata,
            batch_size=4,
            target_size=(128, 128),
        )
        if not isinstance(generators, Mapping):
            print("❌ FAIL: Expected generators mapping, got", type(generators))
            return False

        required_generators = ["train", "val", "test"]
        for name in required_generators:
            if name not in generators:
                print(f"❌ MISSING: {name} generator")
                return False
            gen = generators[name]
            length = len(gen) if hasattr(gen, "__len__") else "unknown"
            print(f"✅ {name} generator available (length: {length})")

        print("\n🔥 Inspecting first batch from each generator...")
        for name, generator in generators.items():
            try:
                iterator: Iterable[Any]
                if isinstance(generator, Iterable):
                    iterator = generator
                else:
                    raise TypeError("Generator is not iterable")
                first_batch = next(iter(iterator))
            except StopIteration:
                print(f"❌ {name} generator yielded no data")
                return False
            except Exception as exc:
                print(f"❌ {name} batch retrieval failed: {exc}")
                return False

            if isinstance(first_batch, Tuple) and len(first_batch) == 2:
                batch_x, batch_y = first_batch
                x_desc = _describe_batch_value(batch_x)
                y_desc = _describe_batch_value(batch_y)
                print(f"✅ {name} batch placeholder -> X: {x_desc}, y: {y_desc}")
            else:
                print(f"❌ {name} batch has unexpected structure: {first_batch}")
                return False

        print("\n🎉 DATA PIPELINE TEST PASSED!")
        return True

    except Exception as exc:  # pragma: no cover - diagnostic aid
        print(f"❌ DATA PIPELINE TEST FAILED: {exc}")
        import traceback

        traceback.print_exc()
        return False


def test_trainer_placeholder() -> bool:
    """Exercise the placeholder trainer."""
    print("\n🧠 Testing Trainer Skeleton...")
    print("=" * 50)

    try:
        PneumoniaModelTrainer = _import_trainer()
        trainer = PneumoniaModelTrainer(model_dir="models/test")

        print("📐 Running placeholder training loop...")
        model, history = trainer.train([], [], epochs=1)
        if model is None:
            print("❌ FAIL: Trainer returned no model")
            return False
        if not isinstance(history, Mapping):
            print("❌ FAIL: Trainer returned unexpected history type", type(history))
            return False
        print(f"✅ Training stub completed with history keys: {list(history.keys())}")

        print("\n🗂️ Verifying saved model artifacts...")
        expected_files = [
            Path(trainer.model_dir) / "pneumonia_best_model.h5",
            Path(trainer.model_dir) / "pneumonia_final_model.h5",
        ]
        for artifact in expected_files:
            if artifact.exists():
                print(f"✅ Found placeholder artifact: {artifact}")
            else:
                print(f"❌ Missing expected artifact: {artifact}")
                return False

        print("\n📊 Evaluating placeholder model...")
        results = trainer.evaluate_model([])
        if not isinstance(results, Mapping):
            print("❌ FAIL: Expected evaluation results mapping, got", type(results))
            return False
        print(f"✅ Evaluation stub returned metrics: {results}")

        print("\n🎉 TRAINER TEST PASSED!")
        return True

    except Exception as exc:  # pragma: no cover - diagnostic aid
        print(f"❌ TRAINER TEST FAILED: {exc}")
        import traceback

        traceback.print_exc()
        return False


def main() -> bool:
    """Run the quick validation suite."""
    print("🚀 COMPREHENSIVE PIPELINE TEST SUITE")
    print("=" * 60)

    tests = [
        ("Data loader", test_data_loading),
        ("Trainer", test_trainer_placeholder),
    ]

    passed = 0
    for name, test_func in tests:
        if test_func():
            passed += 1
        print("-" * 60)

    print("\n" + "=" * 60)
    print("📊 TEST RESULTS")
    print("=" * 60)
    print(f"Tests Passed: {passed}/{len(tests)}")

    if passed == len(tests):
        print("🎉 ALL TESTS PASSED! You're ready for full training.")
        print("\n💡 Next: python training/train_pneumonia.py")
        return True

    print("❌ SOME TESTS FAILED. Please check the errors above.")
    return False


if __name__ == "__main__":
    success = main()
    raise SystemExit(0 if success else 1)
