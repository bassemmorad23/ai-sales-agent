from src.helpers.config import get_settings , Settings
import os



class BaseController:
    def __init__(self):
        
        self.app_settings = get_settings()
        
        
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.src_dir = os.path.abspath(os.path.join(self.base_dir, ".."))
        self.files_dir=os.path.join(self.src_dir,"assets", "files")
            