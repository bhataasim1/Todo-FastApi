from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True, min_length=5)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100, min_length=5)
    # todo_table = relationship("Todo", back_populates="creator")

    class Meta:
        table = "user"
