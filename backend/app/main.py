from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .dummy_data import get_dummy_chart_data, ChartDataItem
# from motor.motor_asyncio import AsyncIOMotorClient # Uncomment for MongoDB integration

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:8080",  # Vue.js frontend development server
    "http://localhost:5173",  # Vite development server (common for Vue 3)
    "http://frontend:8080"   # Docker service name for frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MongoDB Setup (Example - uncomment and configure if needed) ---
# MONGODB_URL = "mongodb://mongo:27017" # 'mongo' is the service name in docker-compose
# client = AsyncIOMotorClient(MONGODB_URL)
# database = client.mydatabase # Replace 'mydatabase' with your DB name
# collection = database.mycollection # Replace 'mycollection' with your collection name

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

@app.get("/api/chart-data", response_model=List[ChartDataItem])
async def get_chart_data():
    """
    Endpoint to get dummy chart data.
    Later, this could fetch data from MongoDB.
    """
    # Example: Fetching from dummy data
    data = get_dummy_chart_data()

    # --- Example: Fetching from MongoDB (Uncomment and adapt) ---
    # documents = []
    # cursor = collection.find({})
    # async for document in cursor:
    #     # Assuming your documents have 'label' and 'value' fields
    #     documents.append(ChartDataItem(label=document.get("label"), value=document.get("value")))
    # if not documents: # If DB is empty, return dummy data
    #     return get_dummy_chart_data()
    # return documents
    return data

# Example: Add some data to MongoDB (Uncomment and adapt for initial data seeding)
# @app.on_event("startup")
# async def startup_db_client():
#     # This is an example of how you might insert some initial data
#     # For a real application, you'd want a more robust seeding strategy
#     # Check if data already exists to avoid duplicates
#     if await collection.count_documents({}) == 0:
#         dummy_data_for_db = [
#             {"label": "DB January", "value": 70},
#             {"label": "DB February", "value": 60},
#             {"label": "DB March", "value": 90},
#         ]
#         await collection.insert_many(dummy_data_for_db)
#         print("Added initial data to MongoDB.")

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     client.close()