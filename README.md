# Assignment API

## Setup

- If you want to run the application locally, adjust the database connection string in the `.env` file using the `DATABASE_URL` key.
- To install dependencies for the application use `requirements.txt` file.

## Running the Application

To run the application, execute the following command in the terminal:

```bash
fastapi run app/main.py --port 8080
```

## Setting up tests

- To install dependencies for the tests use `requirements-tests.txt` file.

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