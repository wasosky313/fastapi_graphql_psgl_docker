# Esto es ya graphene
from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str
