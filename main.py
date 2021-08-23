import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

app = FastAPI()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema()))

