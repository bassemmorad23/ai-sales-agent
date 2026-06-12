from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATION_SUCCESS = 'file_validation_success'    
    FILE_TYPE_NOT_SUPPORTED = 'file_type_not_supported'
    FILE_SIZE_EXCEEDS = 'file_size_exceeds'
    FILE_UPLOAD_SUCCESS = 'file_upload_success'
    FILE_UPLOAD_FAILED = 'file_upload_failed'   
    PROCESSING_SUCCESS = 'processing_success'
    PROCESSING_FAILED = 'file_processing_failed'