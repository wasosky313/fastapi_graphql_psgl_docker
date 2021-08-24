# Esto es ya graphene
from pydantic import BaseModel
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Post


class PostSchema(BaseModel):
    title: str
    content: str


class PostModel(SQLAlchemyObjectType):
    class Meta:
        model = Post
