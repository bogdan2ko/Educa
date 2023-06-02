# Educa

Educa is a web application built using Django and Django Rest Framework (DRF) that aims to provide an interactive and user-friendly platform for educational purposes. 
The application allows users to access various educational resources, create courses, enroll in courses, and participate in discussions. 
This README file provides an overview of the application's features, installation instructions, and usage guidelines.

## Features
User registration and authentication: Users can create an account, log in, and manage their profiles.
Course management: Users with appropriate permissions can create courses, update course details, and delete courses.
Enrollment: Users can enroll in available courses and track their progress.
Resource upload: Course creators can upload educational resources such as documents, videos, and presentations.
API endpoints: The application provides a set of API endpoints built using DRF for seamless integration with other services or client applications.

## Installation
To run Educa on your local machine, follow these steps:

1. Clone the repository: 
``` git clone https://github.com/your-username/educa.git     ```
2. Navigate to the project directory:
``` cd educa       ``` 
3. Create and activate a virtual environment: 
``` python -m venv venv ```
``` source venv/bin/activate  # for Linux/macOS```
``` venv\Scripts\activate  # for Windows   ```    
4. Install the dependencies:
``` pip install -r requirements.txt       ```
5. Set up the database:
``` python manage.py migrate     ```
6. Create a superuser (admin) account:
``` python manage.py createsuperuser      ```
7. Start the development server:
```     python manage.py runserver        ```
8. Open your web browser and navigate to http://localhost:8000 to access the application.

## Usage

1. Open the application in your web browser.

2. Create a new account or log in using your existing credentials.

3. Browse the available courses or create your own courses if you have the necessary permissions.

4. Enroll in courses of your interest and start learning.

5. Participate in course discussions to ask questions, provide answers, and engage with other users.

6. Upload educational resources to share with other users (if you have the appropriate permissions).

## API Documentation

The application provides a set of API endpoints for interacting with the data. 
The API documentation can be accessed by navigating to /api/docs/ when the application is running locally.
 
