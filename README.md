# Assignment API

## Setup

- If you want to run the application locally, adjust the database connection string in the `.env` file using the `DATABASE_URL` key.

## Running the Application

To run the application, execute the following command in the terminal:

```bash
fastapi run app/main.py --port 8080
```

## Seeding Test Data

To seed the data required for tests, run the following command:

```bash
python seed.py
```

## Running Tests

To run the tests, use the following command:

```bash
pytest tests/*
```

## Running Services with Docker

To run the services as Docker containers, execute:

```bash
docker compose up -d
```