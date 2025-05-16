# Prompted Plate: AI-Powered Nutritional Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent tool that processes images of food using OpenAI's GPT model to provide an educated guess of nutritional information. The data is then stored and visualized to help track dietary intake over time. 

## Table of Contents

1.  [Overview](#overview)
2.  [Features](#features)
    * [Core Functionality](#core-functionality)
    * [Planned Enhancements](#planned-enhancements)
    * [Optional Future Features](#optional-future-features)
3.  [Tech Stack](#tech-stack)
4.  [Architectural Overview](#architectural-overview)
    * [Hosting & Virtualization](#hosting--virtualization)
    * [Containerization](#containerization)
    * [CI/CD Automation](#cicd-automation)
    * [Networking](#networking)
5.  [API Endpoints](#api-endpoints)
6.  [Potential Limitations](#potential-limitations)
7.  [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation & Setup](#installation--setup)
    * [Running the Application](#running-the-application)
8.  [CI/CD Pipeline](#cicd-pipeline)
9.  [Disclaimer](#disclaimer)

## Overview

This project aims to simplify nutritional tracking by leveraging the power of AI. Users can take a picture of their meal, and the application will:
1.  Send the image to a backend service.
2.  The backend service queries an OpenAI GPT model with a specialized prompt to analyze the image.
3.  GPT returns an estimated nutritional breakdown (calories, protein, carbs, fats) in a structured JSON format.
4.  This nutritional data is then stored and can be visualized, allowing users to track their eating habits over time.

This project serves as a portfolio piece demonstrating skills in:
* Backend API development (Python with FastAPI).
* Frontend web development (HTML, CSS, JavaScript, Chart.js).
* Database management (MongoDB).
* AI API integration (OpenAI GPT).
* DevOps practices (Docker, Jenkins for CI/CD).
* Self-hosting solutions (Proxmox).

## Features

### Core Functionality (Implemented)

* **Image Upload:** Users can upload an image of their food via a web interface.
* **AI Nutritional Analysis:** The backend sends the image to OpenAI's GPT-4 Vision API for nutritional estimation.
* **Structured JSON Output:** A specific prompt guides GPT to return data in a predefined JSON format.
* **Data Persistence:** Nutritional information, along with timestamps, is stored in a MongoDB database.
* **Basic Visualization:**
    * Display of daily total calories.
    * Bar chart showing daily macronutrient breakdown (protein, carbs, fat) using Chart.js.
* **Dockerized Application:** The backend and database are containerized for easy deployment and management.

### Planned Enhancements (Next Steps)

* **Jenkins CI/CD Pipeline:** Full automation of build, testing, and deployment for the backend application.
* **Improved Frontend UI/UX:**
    * Enhanced styling and responsiveness.
    * Chronological food log display.
    * Loading indicators and better error handling.
* **Enhanced Analytical Features:**
    * Backend endpoints for historical data (e.g., trends over the last 7 days).
    * Frontend date selection to view past nutritional data.
    * Line charts for calorie trends over time.
* **Robust OpenAI JSON Validation:** Improved backend error handling for OpenAI's responses.

### Optional Future Features (Exploratory)

* **User Accounts:** Basic registration and login to support multiple users.
* **Image Storage & Display:** Store uploaded images and display thumbnails in the food log.
* **Manual Entry/Correction:** Allow users to manually input or correct nutritional data.
* **Progressive Web App (PWA):** Enhance the web interface with PWA features.
* **Advanced Prompt Engineering:** Further refinement of prompts for improved accuracy.

## Tech Stack

* **Backend:**
    * Language: **Python 3.x**
    * Framework: **FastAPI**
    * OpenAI API Interaction: `openai` Python library
    * Image Pre-processing (optional): Pillow
* **Frontend:**
    * **HTML5, CSS3, JavaScript (ES6+)**
    * Visualization: **Chart.js**
    * API Communication: `Workspace` API
* **Database:**
    * **MongoDB** (NoSQL, Document Store)
* **DevOps & Hosting:**
    * Virtualization: **Proxmox VE**
    * Containerization: **Docker, Docker Compose**
    * CI/CD: **Jenkins**
    * Reverse Proxy: **Nginx** (or Traefik/Caddy)
    * Version Control: **Git & GitHub**

## Architectural Overview

The application is designed with a microservices-inspired approach, leveraging containerization for modularity and scalability.

### Hosting & Virtualization

* The entire application stack is intended to be hosted on a **Proxmox VE** server.
* Separate Virtual Machines (VMs) or Linux Containers (LXCs) are used for different services (e.g., application backend, database, Jenkins).

### Containerization

* **Docker** is used to containerize the backend Python application and the MongoDB database.
* A `Dockerfile` defines the image for the backend application.
* `docker-compose.yml` is used to define and manage the multi-container setup (backend API, database).

### CI/CD Automation

* **Jenkins** is configured for Continuous Integration and Continuous Deployment (CI/CD).
* The Jenkins pipeline, defined in a `Jenkinsfile`:
    1.  Monitors the GitHub repository for changes.
    2.  Automatically builds the backend Docker image.
    3.  (Future) Runs automated tests.
    4.  Pushes the new image to a Docker registry.
    5.  Deploys the updated container(s) to the Proxmox environment.

### Networking

* A **Reverse Proxy** (e.g., Nginx) is set up to:
    * Handle incoming HTTPS requests.
    * Route traffic to the appropriate backend service.
    * Manage SSL/TLS certificates (e.g., via Let's Encrypt).
* Port forwarding on the local network router may be required to expose the service to the internet (for phone access).

## API Endpoints

The backend API (built with FastAPI) exposes the following main endpoints:

* `POST /upload_image`:
    * Accepts an image file.
    * Communicates with OpenAI API for nutritional analysis.
    * Stores the results in the database.
    * Returns the nutritional information.
* `GET /get_nutritional_data?period=today&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`:
    * Retrieves food logs from the database based on query parameters.
    * Aggregates nutritional information.
    * Returns data suitable for frontend visualization.

*(Further endpoints for user management or detailed data queries may be added as features evolve.)*

## Potential Limitations

* **Accuracy of AI Estimation:** Nutritional data from OpenAI GPT is an "educated guess" and may not always be accurate. It depends heavily on image quality, portion size estimation (which is inherently difficult from a 2D image), and the complexity of the food.
* **OpenAI API Costs:** GPT-4 Vision API calls incur costs. Monitor usage for this hobby project.
* **JSON Consistency:** While prompted for JSON, the AI might occasionally return malformed or inconsistently structured data. Robust error handling is crucial.
* **Security:** If exposing the application to the internet, proper security measures for the server, network, and application code are paramount.

## Getting Started

### Prerequisites

* **Proxmox VE** server (or any system capable of running Docker).
* **Docker** and **Docker Compose** installed.
* **Python 3.8+** and `pip` (for local backend development if not using Docker exclusively).
* **Node.js** and `npm` (if you plan to use build tools for the frontend, otherwise not strictly necessary for basic HTML/JS).
* An **OpenAI API Key** with access to GPT-4 Vision models.
* Git.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-nutritional-tracker.git](https://github.com/your-username/ai-nutritional-tracker.git)
    cd ai-nutritional-tracker
    ```

2.  **Configure Environment Variables:**
    * Copy the example environment file for the backend:
        ```bash
        cp backend/.env.example backend/.env
        ```
    * Edit `backend/.env` and add your OpenAI API Key and any other required configurations (e.g., database connection details if not using default Docker Compose setup).
        ```env
        OPENAI_API_KEY="your_openai_api_key_here"
        # MONGODB_URI="mongodb://mongo:27017/" (Example for Docker Compose)
        ```
    * **IMPORTANT:** Ensure `backend/.env` is listed in your `.gitignore` file and is **never** committed to the repository.

3.  **Build and Run with Docker Compose (Recommended):**
    * Ensure Docker and Docker Compose are running.
    * From the project root directory:
        ```bash
        docker-compose up --build -d
        ```
    This will build the backend image (if not already built) and start the backend service and MongoDB database containers in detached mode.

4.  **Frontend Setup:**
    * The frontend files (`frontend/index.html`, `frontend/style.css`, `frontend/script.js`) are typically served by a simple web server or can be opened directly in a browser for development.
    * Ensure the JavaScript (`frontend/script.js`) is configured to point to the correct backend API URL (e.g., `http://localhost:8000/upload_image` if running locally or the URL of your reverse proxy).

### Running the Application

* **Backend API:** If using Docker Compose, the API will typically be available at `http://localhost:8000` (or the port you configure). FastAPI provides interactive API documentation at `http://localhost:8000/docs`.
* **Frontend:** Open `frontend/index.html` in your web browser.
* **Accessing from Phone:** If hosted on your Proxmox server and exposed via a reverse proxy and port forwarding, you should be able to access the frontend using your server's public IP address or domain name.

## CI/CD Pipeline

This project aims to use **Jenkins** for automating the build, test, and deployment cycle.

* **`Jenkinsfile`:** A `Jenkinsfile` (declarative pipeline) will be included in the root of the repository.
* **Pipeline Stages (Planned):**
    1.  **Checkout:** Pulls the latest code from the GitHub repository.
    2.  **Build:** Builds the Docker image for the backend application.
    3.  **Test (Future):** Runs automated tests (e.g., unit tests, integration tests).
    4.  **Push:** Pushes the built Docker image to a Docker registry (e.g., Docker Hub or a private registry).
    5.  **Deploy:** Connects to the Proxmox host (via SSH) and updates the running application by pulling the new image and restarting the relevant Docker containers.

*(Details on setting up Jenkins and connecting it to this repository will be added once the pipeline is fully implemented.)*

## Disclaimer

This application provides nutritional information estimates based on AI analysis for informational and hobbyist purposes only. **It is not a substitute for professional nutritional advice or medical guidance.** The accuracy of the nutritional data is not guaranteed. Always consult with a qualified nutritionist or healthcare provider for dietary advice.
