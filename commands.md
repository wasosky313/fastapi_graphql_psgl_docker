fastapi uvicorn sqlalchemy graphene graphene-sqlalchemy alembic psycopg2 black python-dotenv

alembic init alembic

docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head

# para crear datos en la base
mutation CreateNewPost {
  createNewPost(title: "New Title1", content: "New Content 1") {
    ok
  }
}

# hacer consultas
query{
  allPosts{
    title
    content
  }
}



