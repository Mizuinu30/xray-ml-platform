#!/usr/bin/env python3
"""
Quick test script to verify the data pipeline works
"""

import os
import sys
from pathlib import Path

def test_data_loading():
    """Test if data loads correctly"""
    print("🧪 Testing Data Pipeline...")
    print("=" * 50)
    
    try:
        from pneumonia_data_loader import PneumoniaDataLoader
        
        # Initialize loader
        data_loader = PneumoniaDataLoader()
        
        # Test metadata loading
        print("📊 Loading metadata...")
        metadata_df = data_loader.load_metadata()
        
        if metadata_df is None or len(metadata_df) == 0:
            print("❌ FAIL: No metadata loaded")
            return False
        
        print(f"✅ SUCCESS: Loaded {len(metadata_df)} images")
        
        # Test dataset balance analysis
        print("\n📈 Testing dataset analysis...")
        data_loader.analyze_dataset_balance(metadata_df)
        
        # Test data generators
        print("\n🔄 Testing data generators...")
        generators = data_loader.create_data_generators(
            metadata_df, 
            batch_size=4,  # Small batch for testing
            target_size=(128, 128)  # Smaller images for quick test
        )
        
        required_generators = ['train', 'val', 'test']
        for gen_name in required_generators:
            if gen_name in generators:
                print(f"✅ {gen_name} generator: {generators[gen_name].samples} samples")
            else:
                print(f"❌ MISSING: {gen_name} generator")
                return False
        
        # Test one batch from each generator
        print("\n🔥 Testing batch generation...")
        for gen_name, generator in generators.items():
            try:
                batch_x, batch_y = next(generator)
                print(f"✅ {gen_name} batch: {batch_x.shape}, labels: {batch_y.shape}")
            except Exception as e:
                print(f"❌ {gen_name} batch failed: {e}")
                return False
        
        print("\n🎉 DATA PIPELINE TEST PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ DATA PIPELINE TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_model_creation():
    """Test if model can be created"""
    print("\n🧠 Testing Model Creation...")
    print("=" * 50)
    
    try:
        from pneumonia_trainer import PneumoniaModelTrainer
        
        trainer = PneumoniaModelTrainer(model_dir="models/test")
        
        # Test basic model
        print("📐 Creating basic model...")
        basic_model = trainer.create_pneumonia_model(input_shape=(128, 128, 1))
        print(f"✅ Basic model: {basic_model.count_params()} parameters")
        
        # Test transfer learning model
        print("🔄 Creating transfer learning model...")
        tl_model = trainer.create_transfer_learning_model(input_shape=(128, 128, 1))
        print(f"✅ Transfer learning model: {tl_model.count_params()} parameters")
        
        # Test model compilation
        print("⚡ Testing model compilation...")
        try:
            tl_model.compile(
                optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy']
            )
            print("✅ Model compilation successful")
        except Exception as e:
            print(f"❌ Model compilation failed: {e}")
            return False
        
        print("\n🎉 MODEL CREATION TEST PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ MODEL CREATION TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("🚀 COMPREHENSIVE PIPELINE TEST SUITE")
    print("=" * 60)
    
    tests_passed = 0
    tests_total = 2
    
    # Test data pipeline
    if test_data_loading():
        tests_passed += 1
    
    # Test model creation  
    if test_model_creation():
        tests_passed += 1
    
    # Final results
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS")
    print("=" * 60)
    print(f"Tests Passed: {tests_passed}/{tests_total}")
    
    if tests_passed == tests_total:
        print("🎉 ALL TESTS PASSED! You're ready for full training.")
        print("\n💡 Next: python training/train_pneumonia.py")
        return True
    else:
        print("❌ SOME TESTS FAILED. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
