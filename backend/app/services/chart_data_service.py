from typing import List
from ..models.food import ChartDataItem

class ChartDataService:
    """Service for providing chart data"""
    
    @staticmethod
    def get_dummy_chart_data() -> List[ChartDataItem]:
        """Returns dummy data for charts"""
        return [
            ChartDataItem(label="January", value=65),
            ChartDataItem(label="February", value=59),
            ChartDataItem(label="March", value=80),
            ChartDataItem(label="April", value=81),
            ChartDataItem(label="May", value=56),
            ChartDataItem(label="June", value=55),
            ChartDataItem(label="July", value=40),
        ]
    
    @staticmethod
    def get_nutrition_chart_data() -> List[ChartDataItem]:
        """Returns nutrition-related chart data"""
        return [
            ChartDataItem(label="Protein", value=25),
            ChartDataItem(label="Carbs", value=45),
            ChartDataItem(label="Fat", value=30),
        ] 