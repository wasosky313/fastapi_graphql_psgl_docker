fastapi uvicorn sqlalchemy graphene graphene-sqlalchemy alembic psycopg2 black python-dotenv

alembic init alembic

docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head

