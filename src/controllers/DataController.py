from fastapi import UploadFile
from .BaseController import BaseController
from src.models import ResponseSignal
from .ProjectController import ProjectController
import random
import string
import re
import os


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
    
    
    def generate_unique_filepath(self, org_file_name: str, project_id: str, length=8):
        random_key=self.get_random_string(length=length)
        project_path=ProjectController().get_project_path(project_id=project_id)
        
        
        cleaned_file_name = self.clean_file_name(org_file_name=org_file_name)
        
        new_file_path=os.path.join(project_path,
                                   random_key+"_"+cleaned_file_name)
        
        while os.path.exists(new_file_path):
            random_key=self.get_random_string(length=length)
            new_file_path=os.path.join(project_path,
                                       random_key+"_"+cleaned_file_name)
        return new_file_path , random_key+"_"+cleaned_file_name
    
    
    def clean_file_name(self,org_file_name: str):
        
        cleaned_file_name =re.sub(r'[^\w\-_\. ]', '_', org_file_name)
        
        cleaned_file_name=cleaned_file_name.replace(" ","_")
        
        return cleaned_file_name
    

   