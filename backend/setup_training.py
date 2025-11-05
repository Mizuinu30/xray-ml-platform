#!/usr/bin/env python3
"""
Complete training environment setup script
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Run a shell command with error handling"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Success")
            return True
        else:
            print(f"❌ {description} - Failed")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False


def main():
    """Main setup function"""
    print("🚀 Complete X-Ray ML Training Environment Setup")
    print("=" * 60)
    
    # Check Python version
    print(f"🐍 Python version: {sys.version}")
    
    # Install dependencies
    dependencies = [
        "tensorflow>=2.8.0",
        "scikit-learn>=1.0.0", 
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "numpy>=1.21.0",
        "Pillow>=8.3.0",
        "opencv-python>=4.5.0",
        "pandas>=1.3.0",
        "kaggle>=1.5.0"
    ]
    
    print("\n📦 Installing dependencies...")
    for package in dependencies:
        run_command(f"pip install {package}", f"Installing {package}")
    
    # Setup Kaggle
    print("\n🔐 Setting up Kaggle API...")
    kaggle_dir = Path.home() / ".kaggle"
    kaggle_dir.mkdir(exist_ok=True)
    
    print("Please ensure you have kaggle.json in ~/.kaggle/")
    print("Download from: https://www.kaggle.com/settings/account")
    
    # Test Kaggle API
    if run_command("kaggle datasets list -s \"chest xray\" --max-size 1", "Testing Kaggle API"):
        print("✅ Kaggle API is working!")
    else:
        print("❌ Kaggle API test failed")
        print("Please check your kaggle.json configuration")
    
    # Create directory structure
    print("\n📁 Creating directory structure...")
    directories = [
        "data/raw",
        "data/processed",
        "data/splits", 
        "models/pneumonia",
        "logs",
        "training"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✅ {directory}")
    
    print("\n✅ Setup completed!")
    print("\n🎯 Next steps:")
    print("1. Run: python training/train_pneumonia.py")
    print("2. This will automatically download the dataset and start training")
    print("3. Monitor training in the logs/ directory")


if __name__ == "__main__":
    main()
