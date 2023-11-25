from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from Models.todo_model import Todo
from Models.user_model import User
from Schema.todo_schema import GetTodoSchema, PostTodo, PutTodo

router = APIRouter(prefix="/api/todo", tags=["Todo"])

@router.get("/alltodos", response_model=list[GetTodoSchema])
async def get_all_todos():
    data = Todo.all()
    return await GetTodoSchema.from_queryset(data)

@router.get("/{id}", response_model=GetTodoSchema)
async def get_todo_by_id(id: int):
    return await GetTodoSchema.from_queryset_single(Todo.get(id=id))

@router.post("/create", response_model=GetTodoSchema)
async def create_todo( todo: PostTodo ):
    new_todo = await Todo.create(**todo.dict(exclude_unset=True))
    return await GetTodoSchema.from_tortoise_orm(new_todo)

@router.put("/update/{id}", response_model=GetTodoSchema)
async def update_todo( id: int, todo: PutTodo ):
    data = await GetTodoSchema.from_queryset_single(Todo.get(id=id))
    exists = await Todo.filter(id=id).exists()
    if exists:
        await Todo.filter(id=id).update(**todo.dict(exclude_unset=True))
        return await GetTodoSchema.from_queryset_single(Todo.get(id=id))
    else:
        raise HTTPException(status_code=404, detail=f"Todo with id: {id} does not exist")

@router.delete("/delete/{id}", response_model=dict)
async def delete_todo_by_id( id: int ):
    exists = await Todo.filter(id=id).delete()
    if not exists:
        raise HTTPException(status_code=404, detail=f"Todo with id: {id} does not exist")
    return {"message": f"Deleted todo with id: {id}"}