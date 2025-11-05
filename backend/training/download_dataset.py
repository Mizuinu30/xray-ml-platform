#!/usr/bin/env python3
"""
Automated dataset download script for Chest X-Ray Pneumonia

This script is safe by default: it will not download the dataset unless
you pass the `--download` flag. Use this to explore or verify an already
downloaded dataset structure.
"""

import argparse
import os
import zipfile
from pathlib import Path

try:
    import kaggle
except Exception:  # pragma: no cover - Kaggle may not be installed in CI
    kaggle = None


def download_pneumonia_dataset(download=True):
    """Download and extract the Chest X-Ray Pneumonia dataset.

    If `download` is False, the function will skip downloading and only
    report on an existing dataset under `data/raw`.
    """

    dataset_name = "paultimothymooney/chest-xray-pneumonia"
    download_dir = Path("data/raw")
    zip_path = download_dir / "chest-xray-pneumonia.zip"

    # Create directory
    download_dir.mkdir(parents=True, exist_ok=True)

    if not download:
        print("ℹ️  Download skipped (run with --download to fetch files).")
        if not download_dir.exists():
            print(f"ℹ️  No data found at {download_dir}. Nothing to explore.")
            return
        explore_dataset_structure(download_dir)
        return

    print("🔍 Downloading Chest X-Ray Pneumonia dataset...")

    if kaggle is None:
        raise RuntimeError("The kaggle package is not installed. Run `pip install kaggle`.")

    try:
        # Download dataset (this will create a zip file in download_dir)
        kaggle.api.dataset_download_files(
            dataset_name,
            path=download_dir,
            quiet=False
        )

        print("✅ Download completed!")

        # Try to find the downloaded zip file (the name can vary)
        # If the expected name exists use that, otherwise search for any zip
        if not zip_path.exists():
            zips = list(download_dir.glob("*.zip"))
            if zips:
                zip_path = zips[0]

        if zip_path.exists():
            # Extract dataset
            print("📦 Extracting dataset...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)

            print("✅ Extraction completed!")

            # Explore the extracted structure
            explore_dataset_structure(download_dir)

            # Clean up zip file
            try:
                zip_path.unlink()
                print("🧹 Cleaned up zip file")
            except Exception:
                print("⚠️  Could not remove zip file; please remove it manually if desired.")
        else:
            print("⚠️  Download finished but no zip file was found to extract.")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please ensure:")
        print("1. kaggle.json is in ~/.kaggle/")
        print("2. Kaggle API is installed: pip install kaggle")
        print("3. You've accepted any dataset rules on Kaggle")
        raise


def explore_dataset_structure(download_dir: Path):
    """Explore and verify the dataset structure"""
    print("\n📁 Dataset Structure:")
    print("=" * 50)

    if not download_dir.exists():
        print(f"No dataset directory found at {download_dir}")
        return

    for root, dirs, files in os.walk(download_dir):
        # Skip the root directory itself
        if root == str(download_dir):
            continue

        level = root.replace(str(download_dir), '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")

        subindent = ' ' * 2 * (level + 1)
        for file in files[:5]:  # Show first 5 files
            print(f"{subindent}{file}")
        if len(files) > 5:
            print(f"{subindent}... and {len(files) - 5} more files")

    # Count images
    count_images(download_dir)


def count_images(download_dir: Path):
    """Count total images in dataset"""
    image_extensions = {'.jpeg', '.jpg', '.png'}
    total_count = 0
    split_counts = {}

    for split in ['train', 'test', 'val']:
        split_path = download_dir / "chest_xray" / split
        if split_path.exists():
            split_count = 0
            for class_dir in ['NORMAL', 'PNEUMONIA']:
                class_path = split_path / class_dir
                if class_path.exists():
                    count = sum(1 for f in class_path.iterdir()
                                if f.suffix.lower() in image_extensions)
                    split_count += count
                    print(f"  {split}/{class_dir}: {count} images")

            split_counts[split] = split_count
            total_count += split_count

    print(f"\n📊 Total Images: {total_count}")
    for split, count in split_counts.items():
        print(f"  {split.upper()}: {count} images")


def verify_dataset_integrity(download_dir: Path):
    """Verify the dataset is complete and properly structured"""
    print("\n🔍 Verifying dataset integrity...")

    required_structure = {
        "chest_xray/train/NORMAL": "*.jpeg",
        "chest_xray/train/PNEUMONIA": "*.jpeg",
        "chest_xray/test/NORMAL": "*.jpeg",
        "chest_xray/test/PNEUMONIA": "*.jpeg",
        "chest_xray/val/NORMAL": "*.jpeg",
        "chest_xray/val/PNEUMONIA": "*.jpeg"
    }

    all_good = True
    for path_pattern, file_pattern in required_structure.items():
        full_path = download_dir / path_pattern
        if not full_path.exists():
            print(f"❌ Missing directory: {path_pattern}")
            all_good = False
            continue

        files = list(full_path.glob(file_pattern))
        if not files:
            print(f"❌ No images found in: {path_pattern}")
            all_good = False
        else:
            print(f"✅ {path_pattern}: {len(files)} images")

    if all_good:
        print("\n🎉 Dataset integrity verified!")
    else:
        print("\n⚠️  Dataset has missing components!")

    return all_good


def main():
    parser = argparse.ArgumentParser(description="Chest X-Ray Pneumonia dataset helper")
    parser.add_argument("--download", action="store_true", help="Download the dataset (off by default)")
    args = parser.parse_args()

    print("🚀 Chest X-Ray Pneumonia Dataset Setup")
    print("=" * 50)

    download_pneumonia_dataset(download=args.download)

    # Verify integrity
    download_dir = Path("data/raw")
    verify_dataset_integrity(download_dir)

    print("\n✅ Setup completed! You can now run the training pipeline.")
    print("💡 Next step: python training/train_pneumonia.py")


if __name__ == "__main__":
    main()
