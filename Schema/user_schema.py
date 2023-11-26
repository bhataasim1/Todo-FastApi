from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator
from Models.user_model import User

GetUserSchema = pydantic_model_creator(User, name="User")

class createUser(BaseModel):
    username: str = Field(..., min_length=5, max_length=20, unique=True, example="aasim")
    email: str = Field(..., unique=True, example="aasim@gmail.com")
    password: str = Field(..., min_length=5, example="aasim123")

class loginUser(BaseModel):
    email: str = Field(..., example="aasim@gmail.com")
    password: str = Field(..., example="aasim123")