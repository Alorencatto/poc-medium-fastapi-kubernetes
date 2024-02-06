# FIAP - Pos Tech - Self-service restaurant

## Event Stormming

-[Miro](https://miro.com/welcomeonboard/M0QySElxVFd1a0ozTUs5eUFxUHh3ZTYxeUZoM2kxb2lTWlJBR0RTWDc0aVRLWFg1SWgzam9CcFJuM3FFOG95SHwzMDc0NDU3MzU1MjY5Nzg4Njk5fDI=?share_link_id=271651641849)

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
