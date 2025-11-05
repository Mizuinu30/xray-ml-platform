# X-ray ML Research Platform

![Research Use Only](https://img.shields.io/badge/Purpose-Research%20Only-red)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688)
![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB)

## 🚨 Research & Development Only

**IMPORTANT: This platform is for RESEARCH AND DEVELOPMENT purposes only. NOT FOR CLINICAL USE.**

This platform provides a research environment for experimenting with X-ray image analysis using machine learning. It is designed to facilitate academic research and technology development in medical imaging.

## 🚀 Features

- Web-based interface for X-ray image upload and analysis
- Support for multiple image formats (JPEG, PNG, DICOM)
- Real-time analysis progress tracking
- Research-focused result presentation
- Clear research-only disclaimers and warnings

## 🛠 Technical Stack

### Backend
- FastAPI (Python)
- Uvicorn ASGI server
- Python image processing libraries
- Async file handling

### Frontend
- React 18
- Modern JavaScript (ES6+)
- CSS3 with modern features
- Responsive design

## 🔧 Setup & Installation

### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

The frontend will be available at `http://localhost:3000` and the backend API at `http://localhost:8000`.

## 📚 API Documentation

Once the backend is running, visit:
- API Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

## 🔬 Development

This project uses a VS Code workspace configuration for easy development. Open `xray-platform.code-workspace` in VS Code to get started.

### Project Structure
```
xray-ml-platform/
├── backend/                # Python FastAPI backend
│   ├── app/               # Main application code
│   │   ├── models/       # Data models
│   │   ├── services/     # Business logic
│   │   └── utils/        # Utility functions
│   └── uploads/          # Upload directory
├── frontend/             # React frontend
│   ├── public/          # Static files
│   └── src/             # React source code
└── docs/                # Documentation
```

## ⚠️ Disclaimers

1. This platform is strictly for research and development purposes.
2. Not for clinical use or diagnosis.
3. All results are experimental and should not be used for medical decisions.

## 👤 Author

- **Juan Silva**
- Email: juansilva.dvm@gmail.com
- GitHub: [@Mizuinu30](https://github.com/Mizuinu30)
- LinkedIn: [@juan-silva-rubio](https://linkedin.com/in/juan-silva-rubio)

## 🔐 Secrets & Kaggle API

This project uses the Kaggle API for dataset access. Keep credentials out of source control.

To create a local environment file for development:

1. Create `backend/.env` in the project root (this file is already ignored by `.gitignore`):

```bash
mkdir -p backend
cat > backend/.env <<'ENV'
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_key
ENV
```

2. Secure the file permissions (optional but recommended):

```bash
chmod 600 backend/.env
```

3. Access the variables in Python with `os.getenv("KAGGLE_USERNAME")` and `os.getenv("KAGGLE_KEY")`.

Production / CI recommendations

- GitHub Actions / CI: Use GitHub Secrets to store `KAGGLE_USERNAME` and `KAGGLE_KEY` and expose them to workflows as environment variables. Do not store secrets in the repository.
- GitHub Secrets example (in your workflow):

```yaml
env:
	KAGGLE_USERNAME: ${{ secrets.KAGGLE_USERNAME }}
	KAGGLE_KEY: ${{ secrets.KAGGLE_KEY }}
```

- Vault / Secrets Manager: For more secure production deployments, use a dedicated secrets manager (HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager) and fetch credentials at runtime instead of shipping them in files.

Security reminder: Do not commit `backend/.env`, `~/.kaggle/kaggle.json`, or any other secret files to Git. Rotate your Kaggle API key if it is ever exposed.

## ⚙️ CI & Running Training Locally

We include a lightweight GitHub Actions CI workflow that runs unit tests and the dataset explorer without downloading large datasets. This keeps CI fast while validating core project logic.

Quick CI notes
- Workflow path: `.github/workflows/ci.yml`  
- What it runs: unit tests (`backend/training/tests`) and the safe dataset explorer (`backend/training/download_dataset.py`)  
- It intentionally does NOT install heavy ML packages (TensorFlow, etc.) — those are kept in a separate requirements file.

Run CI locally (recommended)
1. Run the unit tests in your venv:

```bash
source backend/venv/bin/activate
python -m unittest discover -v backend/training/tests
```

2. Run the dataset explorer (safe — it will not download unless you pass --download):

```bash
# explores any files under backend/data/raw
python backend/training/download_dataset.py
```

Install full training dependencies (optional)

If you want to run training locally (this will install heavier packages like TensorFlow), use the dedicated training requirements file:

```bash
source backend/venv/bin/activate
pip install -r backend/requirements-training.txt
```

Then run the full setup helper (installs packages and creates directories):

```bash
python backend/setup_training.py
```

Start training

Once dependencies are installed and the dataset is available (either downloaded via Kaggle or placed into `backend/data/raw`), start training:

```bash
python backend/training/train_pneumonia.py
```

Notes and safety
- If you run the training script on a machine without a GPU, training may be slow. Consider running on Colab or a cloud instance with GPU.  
- The training requirements are intentionally separated from CI/test requirements to keep CI fast and low-cost.

## 🤝 Contributing

This is a research project and contributions are welcome. Please ensure any additions maintain the research-only nature of the platform.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.