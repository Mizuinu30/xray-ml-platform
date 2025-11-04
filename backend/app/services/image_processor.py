# Image processing service (simplified for now)
class ImageProcessor:
    def __init__(self):
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.dcm']
    
    async def process_image(self, file_path: str):
        # For now, return mock image info
        # In a real implementation, this would process the image
        return {
            "width": 512,
            "height": 512,
            "format": "JPEG",
            "file_size": 1024000,
            "color_mode": "L"
        }
