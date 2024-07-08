# Task Management API

Task Management API is a Django project that provides an API for task management. The project uses the built-in SQLite database and is deployed using Docker Compose.

## Project Structure

- `Dockerfile`: Describes the Docker image for the Django web application.
- `docker-compose.yml`: Docker Compose configuration for running the web application.
- `schema.yml`: API schema (likely OpenAPI/Swagger) describing the API endpoints.
- `requirements.txt`: List of Python dependencies.


## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/alexlobko/task-management-api
    cd task-management-api
    ```

2. Build and start the containers:

    ```bash
    docker-compose up --build
    ```

    This command will build the Docker image and start the containers for the web application.

    To start the containers in the background, use:

    ```bash
    docker-compose up -d --build
    ```
   
3. After the containers are up, run the database migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```
   
4. Create a superuser for accessing the admin panel:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

    Follow the prompts to create the superuser.

## Usage

### API Endpoints

The API schema is located in the `schema.yml` file. You can use tools like Swagger UI or Postman to interact with the API using this schema.

To view the API schema, you can also use the following endpoints:
- Redoc: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)
- Swagger: [http://127.0.0.1:8000/api/schema/swagger/](http://127.0.0.1:8000/api/schema/swagger/)

### Accessing the Admin Panel

The Django admin panel is available at: http://localhost:8000/admin/

Use the superuser credentials created earlier to log in.

## Configuration

### Database Configuration

The `settings.py` file is configured to use the built-in SQLite database. The database configuration looks like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```
If you need to change the database settings, update the corresponding parameters in settings.py.

## Testing
To run the tests, use the following command:
```bush
docker-compose exec web python manage.py test
```

## Stopping
To stop the containers, use:
```bush
docker-compose down
```