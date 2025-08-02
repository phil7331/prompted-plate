from pydantic import BaseModel
from typing import Optional

class FoodAnalysis(BaseModel):
    """Model for food analysis results from AI"""
    calories: Optional[str] = None
    protein: Optional[str] = None
    carbohydrates: Optional[str] = None
    fat: Optional[str] = None
    
class ChartDataItem(BaseModel):
    """Model for chart data items"""
    label: str
    value: int

class FoodImageRequest(BaseModel):
    """Model for food image analysis request"""
    image_path: str
    prompt: Optional[str] = None 