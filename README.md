# 📝 Task Manager API (Django + Docker)

A simple **Task Management API** built using **Django REST Framework** and Docker.  
Users can register, log in, and manage their personal task lists securely with features like search, filtering, and authentication.

---

## 🚀 Features

- ✅ User registration & login (JWT-based)
- ✅ Create, view, update, delete tasks
- ✅ List only completed tasks
- ✅ Search tasks by title or description
- ✅ PostgreSQL database (Dockerized)
- ✅ Token-based authentication
- ✅ Built and deployed with Docker Compose
- ✅ Swagger-based interactive API docs

---

## 🛠️ Tech Stack

- Python 3.11
- Django 5.2.1
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- JWT (JSON Web Tokens)

---

---

## 📚 API Documentation (Swagger)

Interactive API docs are available via Swagger UI:

📍 [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

You can view all endpoints, try them out with live input, and inspect request/response formats.

---

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:Jugalkishor1/Task-Manger-api-drf.git
cd Task-Manger-api-drf
```

---

### 2. Build the Docker Image

```bash
docker-compose build
```

---

### 3. Create a Superuser

```bash
docker compose run --rm app sh -c "python manage.py createsuperuser"
```

You’ll be prompted to enter a username, email, and password.

---

### 4. Start the Application

```bash
docker-compose up
```

The API will be available at:  
📍 **http://localhost:8000**
📚 Swagger Docs: **http://localhost:8000/api/docs/**

---

## 🔐 Authentication

All task-related endpoints require **JWT authentication**.  
Use the `/api/login/` endpoint to get your `access` and `refresh` tokens, and include the access token in your headers:

```http
Authorization: Bearer your_access_token
```

---

## 🧪 API Endpoints

| Method | Endpoint                    | Description                        |
|--------|-----------------------------|------------------------------------|
| POST   | `/api/register/`            | Register a new user                |
| POST   | `/api/login/`               | Obtain JWT token                   |
| GET    | `/api/tasks/`               | List all tasks for logged-in user |
| POST   | `/api/tasks/`               | Create a new task                  |
| GET    | `/api/tasks/<id>/`          | Retrieve a specific task           |
| PUT    | `/api/tasks/<id>/`          | Update a task                      |
| DELETE | `/api/tasks/<id>/`          | Delete a task                      |
| GET    | `/api/tasks/completed/`     | List all completed tasks           |
| GET    | `/api/tasks/search/?q=xyz`  | Search tasks by title/description  |

---

## 🧑‍💻 Local Dev Without Docker (Optional)

```bash
# Create a virtual environment
python -m venv env

# Activate it
source env/bin/activate  # On Windows: .\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations and start the server
python manage.py migrate
python manage.py runserver
```

---

## ✉️ Contact

Made with ❤️ by Jugal Kishor  
📧 Email: jugalpatel1054@gmail.com  
🔗 GitHub: [jugalkishor1](https://github.com/jugalkishor1)
