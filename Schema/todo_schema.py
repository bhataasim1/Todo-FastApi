from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from Models.todo_model import Todo

GetTodoSchema = pydantic_model_creator(Todo, name="Todo")

class PostTodo(BaseModel):
    title: str = Field(..., max_length=100, example="Build Todo with FastApi")
    description: Optional[str] = Field(None, example="This is Description of Todo with FastApi")

class PutTodo(BaseModel):
    title: Optional[str] = Field(None, max_length=100, example="Completed Assignment")
    description: Optional[str] = Field(None, example="Successfully completed assignment of Todo with FastApi")
    completed: Optional[bool] = Field(None, example=False)

