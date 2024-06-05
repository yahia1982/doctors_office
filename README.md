# Doctor's office
## Overview
The Doctor's Office is a Flask application designed to assist patients, .
doctors and administration staff in managing their appointments and consult their medical history efficiently. It employs various technologies to deliver a robust and user-friendly experience.

## Technologies Used
- Python 3.12
- Flask (web framework)
- SQLite (Used for demonstration purposes. For a real application, consider using PostgreSQL or another robust database.)
- Flask login (Used for demonstration purposes. For a real application, consider using a robust solution like FusionAuth or Keycloak.)
## Running the Application with Docker
To run the application using Docker, follow these steps:

1. Build the Docker image:
   ```
   docker build -t main .
   ```

2. Run the Docker container:
   ```
   docker run -p 5000:80 task_manager
   ```
   
2. Or use docker-compose:
   ```
   docker-compose up -d
   ```

## Running the Application Directly
If you prefer to run the application directly, follow these steps:
### 1- Prerequisites
- Python 3.12 should be installed on your machine.
### 2- Setup:
- Open the project in your preferred editor.
### 3- Install Dependencies:
   ```
   pip install -r requirements.txt
   ```
### 4- Run the Application:
   ```
   python amin.py
   ```

## Accessing the Application
Once the application is running, open a web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

## Note
Ensure that you have proper permissions and dependencies installed before running the application.