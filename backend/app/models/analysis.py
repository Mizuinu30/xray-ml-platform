from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from enum import Enum

class AnalysisStatus(str, Enum):
    PROCESSING = "processing"
    SUCCESS = "success"
    ERROR = "error"

class Condition(BaseModel):
    name: str
    confidence: float

class AnalysisResults(BaseModel):
    conditions: List[Condition]
    findings: List[str]
    confidence_score: float
    model_version: str

class AnalysisResponse(BaseModel):
    analysis_id: str
    status: AnalysisStatus
    progress: int
    results: Optional[AnalysisResults]
    timestamp: datetime
