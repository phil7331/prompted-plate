from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List
import os
import tempfile
from ..models.food import FoodAnalysis, ChartDataItem, FoodImageRequest
from ..services.food_analysis_service import FoodAnalysisService
from ..services.chart_data_service import ChartDataService

router = APIRouter(prefix="/food", tags=["food"])

# Initialize services
food_service = FoodAnalysisService()
chart_service = ChartDataService()

@router.get("/", response_model=dict)
async def get_food_root():
    """Root endpoint for food API"""
    return {"message": "Food Analysis API"}

@router.post("/analyze", response_model=FoodAnalysis)
async def analyze_food_image(request: FoodImageRequest):
    """
    Analyze a food image and return nutritional information
    
    Args:
        request: FoodImageRequest containing image path and optional prompt
        
    Returns:
        FoodAnalysis object with nutritional data
    """
    try:
        result = food_service.analyze_food_image(request.image_path, request.prompt)
        
        if isinstance(result, str):
            raise HTTPException(status_code=400, detail=result)
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@router.post("/analyze-upload", response_model=FoodAnalysis)
async def analyze_uploaded_food_image(
    file: UploadFile = File(...),
    prompt: str = None
):
    """
    Analyze an uploaded food image
    
    Args:
        file: Uploaded image file
        prompt: Optional custom prompt
        
    Returns:
        FoodAnalysis object with nutritional data
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            # Analyze the image
            result = food_service.analyze_food_image(temp_file_path, prompt)
            
            if isinstance(result, str):
                raise HTTPException(status_code=400, detail=result)
            
            return result
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
                
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@router.get("/chart-data", response_model=List[ChartDataItem])
async def get_chart_data():
    """Get dummy chart data"""
    return chart_service.get_dummy_chart_data()

@router.get("/nutrition-chart", response_model=List[ChartDataItem])
async def get_nutrition_chart_data():
    """Get nutrition chart data"""
    return chart_service.get_nutrition_chart_data() 