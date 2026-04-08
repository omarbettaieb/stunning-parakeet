# Profit Analytics Backend

Production-oriented backend foundation for a private, single-tenant ecommerce profit analytics app.

## Stack
- Python 3.12
- FastAPI
- SQLAlchemy 2.x
- Alembic
- PostgreSQL
- Redis
- Celery

## Quick start

1. Copy environment file:
   ```bash
   cp .env.example .env
   ```
2. Start services:
   ```bash
   docker compose up --build
   ```
3. Check API health:
   ```bash
   curl http://localhost:8000/api/v1/health
   ```

## Local development (without Docker)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload
```

## Useful commands

```bash
make lint
make check-models
make run
```

## Notes
- This repository currently includes the core domain model layer and application bootstrap.
- Alembic migration scripts, authentication routes, and Shopify sync implementations are intentionally deferred.
