from fastapi import FastAPI , APIRouter , Depends ,UploadFile ,status ,File
from fastapi.responses import JSONResponse
    
from src.helpers.config import get_settings , Settings
from src.controllers import DataController ,ProjectController
import aiofiles
import os
from src.models import ResponseSignal

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1_data",'data']
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str,file:UploadFile=File(), app_settings: Settings = Depends(get_settings)):
    
    
    
    # Validate the uploaded properties
    is_valid , result_signal = DataController().validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"signal": result_signal})

    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = os.path.join(project_dir_path, file.filename)
    
    
    


    async with aiofiles.open(file_path, 'wb') as out_file:
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):  # Read the uploaded file content
            await out_file.write(chunk)  # Write the content to the destination file

    return JSONResponse(content={"signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value})


    