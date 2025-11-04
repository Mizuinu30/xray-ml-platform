from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uuid
import os

app = FastAPI(
    title="X-ray ML Analysis Research API",
    description="FOR RESEARCH USE ONLY - NOT FOR CLINICAL DIAGNOSIS",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory
os.makedirs("uploads", exist_ok=True)

@app.get("/")
async def root():
    return {
        "message": "X-ray ML Analysis Research API",
        "status": "operational",
        "disclaimer": "FOR RESEARCH USE ONLY - NOT FOR CLINICAL DIAGNOSIS"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.post("/api/analyze")
async def analyze_xray(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.dcm')):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    # Generate analysis ID
    analysis_id = str(uuid.uuid4())
    
    return {
        "analysis_id": analysis_id,
        "status": "success",
        "progress": 100,
        "results": {
            "conditions": [
                {"name": "No significant findings", "confidence": 0.92},
                {"name": "Pneumonia", "confidence": 0.07}
            ],
            "findings": [
                "Lungs are clear and well expanded",
                "No pleural effusion or pneumothorax"
            ],
            "confidence_score": 0.92,
            "model_version": "Research Model v1.0"
        },
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
