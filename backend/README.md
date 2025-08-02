# Prompted Plate Backend

AI-powered food analysis API using FastAPI and Google Gemini AI.

## Features

- 🍽️ Food image analysis with nutritional information
- 📊 Chart data endpoints
- 🔒 Secure file upload handling
- 📝 Comprehensive API documentation
- 🧪 Test suite included

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py      # Application configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── food.py          # Pydantic data models
│   ├── routes/
│   │   ├── __init__.py
│   │   └── food.py          # API endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── food_analysis_service.py  # Gemini AI integration
│   │   └── chart_data_service.py     # Chart data logic
│   └── utils/
│       ├── __init__.py
│       └── validators.py    # Validation utilities
├── tests/
│   ├── __init__.py
│   └── test_food_analysis.py
├── pyproject.toml           # Poetry configuration
├── requirements.txt         # Python dependencies
├── env.example             # Environment variables template
└── README.md
```

## Setup

### Prerequisites

- Python 3.11+
- Poetry (recommended) or pip
- Gemini AI API key

### Installation

1. **Clone the repository**
   ```bash
   cd backend
   ```

2. **Install dependencies**
   ```bash
   # Using Poetry (recommended)
   poetry install
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

4. **Run the application**
   ```bash
   # Using Poetry
   poetry run uvicorn app.main:app --reload
   
   # Or using uvicorn directly
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Base URLs
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### Food Analysis Endpoints

- `GET /api/v1/food/` - Food API root
- `POST /api/v1/food/analyze` - Analyze food image by path
- `POST /api/v1/food/analyze-upload` - Analyze uploaded food image
- `GET /api/v1/food/chart-data` - Get dummy chart data
- `GET /api/v1/food/nutrition-chart` - Get nutrition chart data

## Testing

Run the test suite:

```bash
# Using Poetry
poetry run pytest

# Or using pytest directly
pytest
```

## Development

### Code Structure

- **Models**: Pydantic models for data validation
- **Services**: Business logic and external API integrations
- **Routes**: FastAPI endpoints and request handling
- **Config**: Application settings and environment variables
- **Utils**: Helper functions and utilities

### Adding New Features

1. Create models in `app/models/`
2. Add business logic in `app/services/`
3. Create endpoints in `app/routes/`
4. Add tests in `tests/`
5. Update documentation

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini AI API key | Yes |
| `GEMINI_MODEL_NAME` | Gemini model to use | No (default: gemini-2.0-flash-lite) |
| `MONGODB_URL` | MongoDB connection string | No (for future use) |
| `DATABASE_NAME` | Database name | No (for future use) |

## Docker

Build and run with Docker:

```bash
docker build -t prompted-plate-backend .
docker run -p 8000:8000 --env-file .env prompted-plate-backend
``` 