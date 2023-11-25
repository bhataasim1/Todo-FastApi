from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from Models.user_model import User

router = APIRouter(prefix="/user", tags=["User"])
templates = Jinja2Templates(directory="Frontend")


@router.post("/register")
async def register(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    email = form_data.get("email")
    password = form_data.get("password")

    await User.create(username=username, email=email, password=password)
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(request: Request):
    form_data = await request.form()
    email = form_data.get("email")
    password = form_data.get("password")

    user = await User.filter(email=email).first()
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Credentials"})

    if user.password != password:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Credentials"})

    return RedirectResponse(url="/dashboard", status_code=302)

@router.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})