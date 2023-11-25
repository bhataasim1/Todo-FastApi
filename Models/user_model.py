from tortoise.models import Model
from tortoise import fields
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Model):
    __tablename__ = "user"

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
    # todo_table = relationship("Todo", back_populates="creator")