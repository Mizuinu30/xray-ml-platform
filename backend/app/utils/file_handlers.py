import aiofiles
import os
from fastapi import UploadFile

async def save_upload_file(file: UploadFile, analysis_id: str) -> str:
    file_extension = os.path.splitext(file.filename)[1]
    filename = f"{analysis_id}{file_extension}"
    file_path = os.path.join("uploads", filename)
    
    async with aiofiles.open(file_path, 'wb') as f:
        content = await file.read()
        await f.write(content)
    
    return file_path

def validate_file(file: UploadFile):
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.dcm']
    file_extension = os.path.splitext(file.filename)[1].lower()
    
    if file_extension not in allowed_extensions:
        return {
            "valid": False,
            "message": f"File type not supported. Allowed types: {', '.join(allowed_extensions)}"
        }
    
    max_size = 10 * 1024 * 1024  # 10MB
    if file.size > max_size:
        return {
            "valid": False,
            "message": f"File size exceeds {max_size // (1024*1024)}MB limit"
        }
    
    return {"valid": True, "message": "File validation successful"}
