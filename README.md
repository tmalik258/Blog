# Blog API Project README

## Project Overview

This project is a blog application built using Django REST Framework for the backend. The aim is to provide a modern API for users to read, create, and manage blog posts.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Features

- User authentication and authorization
- CRUD operations for blog posts

## Technologies Used

### Backend
- Django
- Django REST Framework
- dj_rest_auth for user authentication

## Installation

### Prerequisites
- Python 3.12.0
- PostgreSQL (or another preferred database)

## Backend Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/blog-project.git
    cd blog-project/backend
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install backend dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Update the `DATABASES` setting in `settings.py` to match your database configuration.

5. **Run migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Start the development server:**

    ```sh
    python manage.py runserver
    ```


## Running the Project

### Without Docker

1. **Start the backend server:**

    ```sh
    cd backend
    python manage.py runserver
    ```

3. Access the backend at `http://localhost:8000`.

## API Endpoints

- **Authentication:**
  - `POST /api/v1/dj-rest-auth/login/`
  - `POST /api/v1/dj-rest-auth/logout/`
  - `POST /api/v1/dj-rest-auth/register/`

- **Blog Posts:**
  - `GET /api/v1/posts/`
  - `POST /api/v1/posts/`
  - `GET /api/v1/posts/:id/`
  - `PUT /api/v1/posts/:id/`
  - `DELETE /api/v1/posts/:id/`


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


---
