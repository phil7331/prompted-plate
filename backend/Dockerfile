# Use a Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy Poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
# --no-dev to exclude development dependencies (good for production)
# --no-root to not install your own package as an editable one
# virtualenvs.create false ensures dependencies are installed directly into the system site-packages
RUN poetry config virtualenvs.create false && \
    poetry install --no-ansi --no-root

# Copy your application code
# Ensure this is done AFTER dependency installation to leverage Docker's build cache
COPY ./app /app/app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using poetry run
# This ensures uvicorn is found within Poetry's managed environment.
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]