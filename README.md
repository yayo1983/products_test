
# Product Management System

This is an Products Management System built with Django, using Django REST Framework for API endpoints. 
The project is containerized with Docker and configured to use SQLite as the database.

## Features

- **Create Product**: Create and manage products with SKU, name, and stock.
- **Product Update**: Update stock for products.
- **Order Management**: Place orders for products.
- **Stock Alerts**: Trigger alerts when stock is below a certain threshold.
- **API Documentation**: Automatically generated API documentation with Swagger.

## Project Structure
```
product_system/
├── products/               # Django app for API endpoints
├── products_test/          # Project settings and configurations
├── Dockerfile              # Dockerfile for containerizing the application
├── docker-compose.yml      # Docker Compose configuration
├── pyproject.toml          # Poetry configuration file
├── poetry.lock             # Poetry lock file
└── README.md               # Project README file
```

## Save repo in github
```
git init
git add .
git commit -m "Primer commit"

git remote add origin <URL_del_repositorio>

git push -u origin master o main
```

## Prerequisites

- Docker
- Docker Compose


## Install dependencies projects 
```
poetry install
```

## Run test
```
python3 manage.py test
```

## Run project
```
python3 manage.py runserver
```

## Execute project using Docker or Build and run the Docker container

1. Build the Docker image
```
docker-compose build
```
2. Run the Docker container
```
docker-compose up
```