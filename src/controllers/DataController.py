from fastapi import UploadFile
from .BaseController import BaseController
from src.models import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        

    
    def validate_uploaded_file(self, file: UploadFile):
        # Implement file validation logic here
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * 1024 * 1024:
            return False , ResponseSignal.FILE_SIZE_EXCEEDS.value
        
        return True , ResponseSignal.FILE_UPLOAD_SUCCESS.value
    

   