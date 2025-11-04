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

## 🤝 Contributing

This is a research project and contributions are welcome. Please ensure any additions maintain the research-only nature of the platform.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.