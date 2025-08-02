import os
from typing import List
from ..config.settings import settings

def validate_image_file(file_path: str) -> bool:
    """
    Validate if a file is a valid image
    
    Args:
        file_path: Path to the file
        
    Returns:
        True if valid, False otherwise
    """
    if not os.path.exists(file_path):
        return False
    
    # Check file size
    file_size = os.path.getsize(file_path)
    if file_size > settings.MAX_FILE_SIZE:
        return False
    
    # Check file extension
    allowed_extensions = ['.jpg', '.jpeg', '.png']
    file_extension = os.path.splitext(file_path)[1].lower()
    
    return file_extension in allowed_extensions

def validate_uploaded_file(file_content_type: str, file_size: int) -> bool:
    """
    Validate uploaded file
    
    Args:
        file_content_type: MIME type of the file
        file_size: Size of the file in bytes
        
    Returns:
        True if valid, False otherwise
    """
    # Check content type
    if file_content_type not in settings.ALLOWED_IMAGE_TYPES:
        return False
    
    # Check file size
    if file_size > settings.MAX_FILE_SIZE:
        return False
    
    return True

def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for security
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove path separators and other dangerous characters
    dangerous_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in dangerous_chars:
        filename = filename.replace(char, '_')
    
    return filename 