# Template FastAPI Project

This is a template FastAPI project that demonstrates how to structure your application into separate modules and containers. The project consists of a FastAPI application and a PostgreSQL database, each encapsulated within its own Docker container.

## Project Structure

```
project_folder/
│
├── api/
│ ├── item_model.py # Defines the Item model
│ ├── item_routes.py # Defines API routes related to items
│ ├── database.py # Handles the database session
│ └── main.py # Main entry point for FastAPI
│
└── docker-compose.yml # Defines Docker services and their interactions
``` 


## Components and Workflow

1. **Docker Compose**: The `docker-compose.yml` file specifies two services - `postgres` and `api`. The `postgres` service runs a PostgreSQL database container, and the `api` service runs the FastAPI application container. They are linked, allowing the FastAPI app to communicate with the PostgreSQL database.

2. **Item Model**: The `Item` model is defined in `item_model.py`. It describes the structure of the data to be stored in the PostgreSQL database.

3. **Item Routes**: API routes related to items are defined in `item_routes.py`. This includes creating items, retrieving individual items, and listing all items.

4. **Database Handling**: The `database.py` file manages the database session using SQLAlchemy. The `get_db` function provides a database session to be used in route functions.

5. **Main Entry Point**: The main FastAPI application is set up in `main.py`. The application includes the routes defined in `item_routes.py` and sets up the database structure using `Base.metadata.create_all`.

## How to Run

1. Clone the repository and navigate to the project folder.

2. Make sure you have Docker and Docker Compose installed on your machine.

3. In the terminal, run the following command to build and start the Docker containers:
   
```bash
   docker-compose up --build
```

The FastAPI application will be accessible at http://localhost:8000. You can use tools like curl or Postman to interact with the API endpoints.

## Conclusion
This template FastAPI project demonstrates a structured approach to building web applications with Docker containers. By separating components into individual files and modules, the project becomes more organized and maintainable.



