# Blog Project README

## Project Overview

This project is a blog application built using React for the frontend and Django REST Framework for the backend. The aim is to provide a modern and interactive interface for users to read, create, and manage blog posts.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- CRUD operations for blog posts
- Responsive design for mobile and desktop
- Comments section for each post
- User profile management

## Technologies Used

### Frontend
- React
- Vite
- Axios
- Redux (or Context API) for state management
- Tailwind CSS for styling

### Backend
- Django
- Django REST Framework
- PostgreSQL (or any other preferred database)
- dj_rest_auth for user authentication

## Installation

### Prerequisites
- Node.js
- Python 3.12.0
- PostgreSQL (or another preferred database)
- Docker (optional, for containerization)

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

## Frontend Setup

1. **Navigate to the frontend directory:**

    ```sh
    cd ../frontend
    ```

2. **Install frontend dependencies:**

    ```sh
    npm install
    ```

3. **Start the development server:**

    ```sh
    npm run dev
    ```

## Running the Project

### With Docker

1. **Build and run the containers:**

    ```sh
    docker-compose up --build
    ```

2. Access the frontend at `http://localhost:3000` and the backend at `http://localhost:8000`.

### Without Docker

1. **Start the backend server:**

    ```sh
    cd backend
    python manage.py runserver
    ```

2. **Start the frontend server:**

    ```sh
    cd frontend
    npm run dev
    ```

3. Access the frontend at `http://localhost:3000` and the backend at `http://localhost:8000`.

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

- **Comments:**
  - `GET /api/v1/posts/:postId/comments/`
  - `POST /api/v1/posts/:postId/comments/`

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any section according to your specific needs and project details.
