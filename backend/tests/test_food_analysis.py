import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.food import FoodAnalysis

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_food_root():
    """Test the food API root endpoint"""
    response = client.get("/api/v1/food/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Food Analysis API"

def test_chart_data():
    """Test the chart data endpoint"""
    response = client.get("/api/v1/food/chart-data")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "label" in data[0]
    assert "value" in data[0]

def test_nutrition_chart():
    """Test the nutrition chart endpoint"""
    response = client.get("/api/v1/food/nutrition-chart")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "label" in data[0]
    assert "value" in data[0]

def test_analyze_food_image_missing_path():
    """Test food analysis with missing image path"""
    request_data = {"image_path": ""}
    response = client.post("/api/v1/food/analyze", json=request_data)
    assert response.status_code == 400

def test_analyze_food_image_invalid_path():
    """Test food analysis with invalid image path"""
    request_data = {"image_path": "/nonexistent/image.jpg"}
    response = client.post("/api/v1/food/analyze", json=request_data)
    assert response.status_code == 400 