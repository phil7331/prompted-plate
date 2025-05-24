from pydantic import BaseModel
from typing import List

class ChartDataItem(BaseModel):
    label: str
    value: int

def get_dummy_chart_data() -> List[ChartDataItem]:
    """Returns some dummy data for the chart."""
    return [
        ChartDataItem(label="January", value=65),
        ChartDataItem(label="February", value=59),
        ChartDataItem(label="March", value=80),
        ChartDataItem(label="April", value=81),
        ChartDataItem(label="May", value=56),
        ChartDataItem(label="June", value=55),
        ChartDataItem(label="July", value=40),
    ]