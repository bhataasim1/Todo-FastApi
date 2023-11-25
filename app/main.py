from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from Routes.todo import router as TodoRouter
from Routes.user import router as UserRouter

app = FastAPI()
templates = Jinja2Templates(directory="Frontend")

app.include_router(TodoRouter)
app.include_router(UserRouter)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["Models.todo_model", "Models.user_model"]},
    generate_schemas=True,
    add_exception_handlers=True
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})