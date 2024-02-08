# Poc Medium FastAPI Kubernetes

## Usage

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

### How to run

1. `docker compose up -d postgres` - Start the database.
2. `docker compose run --rm migrations` - Run the migrations.
3. `docker compose up api`
4. Go to `https://localhost:8000/docs` to see the swagger documentation.

## Development

### Migrations command examples

- `alembic -c migrations/alembic/alembic.ini revision --autogenerate -m" First commit" `
- `alembic -c migrations/alembic/alembic.ini upgrade head`
