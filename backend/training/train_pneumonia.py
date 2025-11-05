#!/usr/bin/env python3
"""
Main training script for Chest X-Ray Pneumonia dataset
With automatic Kaggle dataset download
"""

import os
import sys
from pathlib import Path

# Add the training directory to Python path
sys.path.append(os.path.dirname(__file__))

from pneumonia_data_loader import PneumoniaDataLoader
from pneumonia_trainer import PneumoniaModelTrainer

def setup_environment():
    """Setup the training environment"""
    print("🔧 Setting up training environment...")
    
    # Create necessary directories
    directories = [
        "data/raw",
        "data/processed", 
        "models/pneumonia",
        "logs",
        "training"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✅ Created: {directory}")

def check_dataset():
    """Check if dataset exists, download if missing"""
    dataset_path = Path("data/raw/chest_xray")
    
    if dataset_path.exists():
        print("✅ Dataset found locally")
        return True
    else:
        print("📥 Dataset not found, downloading...")
        try:
            from download_dataset import download_pneumonia_dataset
            # call with download=True to attempt download; download_dataset has safeguards
            download_pneumonia_dataset(download=True)
            return True
        except Exception as e:
            print(f"❌ Failed to download dataset: {e}")
            return False

def main():
    """Main training function for pneumonia dataset"""
    print("🚀 Chest X-Ray Pneumonia Model Training Pipeline")
    print("=" * 60)
    
    # Setup environment
    setup_environment()
    
    # Check and download dataset
    if not check_dataset():
        print("❌ Cannot proceed without dataset. Please download manually:")
        print("   kaggle datasets download -d paultimothymooney/chest-xray-pneumonia")
        print("   unzip chest-xray-pneumonia.zip -d data/raw/")
        return
    
    # Initialize data loader
    data_loader = PneumoniaDataLoader()
    
    # Load metadata
    print("\n📊 Loading dataset metadata...")
    metadata_df = data_loader.load_metadata()
    
    # Analyze dataset balance
    data_loader.analyze_dataset_balance(metadata_df)
    
    # Create data generators
    print("\n🔄 Creating data generators...")
    generators = data_loader.create_data_generators(
        metadata_df, 
        batch_size=32, 
        target_size=(224, 224)
    )
    
    if 'train' not in generators or 'val' not in generators:
        print("❌ Error: Could not create data generators.")
        print("Please check your dataset structure.")
        return
    
    # Initialize trainer
    trainer = PneumoniaModelTrainer()
    
    # Train model
    print("\n🎯 Starting model training...")
    try:
        model, history = trainer.train(
            generators['train'],
            generators['val'],
            epochs=50,
            use_class_weights=True  # Important for imbalanced dataset
        )
        
        # Evaluate on test set
        if 'test' in generators:
            print("\n📈 Evaluating on test set...")
            eval_results = trainer.evaluate_model(generators['test'])
        else:
            print("⚠️  No test generator found, skipping evaluation.")
            eval_results = None
        
        print("\n" + "="*60)
        print("🎉 TRAINING COMPLETED SUCCESSFULLY!")
        print("="*60)
        print(f"📁 Model saved to: {trainer.model_dir}")
        print(f"🏆 Best model: {trainer.model_dir}/pneumonia_best_model.h5")
        print(f"📦 Final model: {trainer.model_dir}/pneumonia_final_model.h5")
        
        if eval_results:
            print(f"📊 Test Accuracy: {eval_results['test_accuracy']:.4f}")
            print(f"📊 Test AUC: {eval_results['test_auc']:.4f}")
            print(f"📊 Test Precision: {eval_results['test_precision']:.4f}")
            print(f"📊 Test Recall: {eval_results['test_recall']:.4f}")
        
        return model, history, eval_results
        
    except Exception as e:
        print(f"❌ Training failed: {e}")
        raise

if __name__ == "__main__":
    main()
