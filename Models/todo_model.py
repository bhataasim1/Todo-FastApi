from tortoise.models import Model
from tortoise import fields
from Models.user_model import User
from sqlalchemy.orm import relationship

class Todo(Model):
    __tablename__ = "todo_table"
    
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    completed = fields.BooleanField(default=False)
    # user = fields.ForeignKeyField("models.User", related_name="todos")
    # creator = relationship("User", back_populates="todo_table")
