from ninja import Router
from ninja.security import django_auth
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token

from .models import CustomUser
from . import schemas

router = Router()


@router.get("/set-csrf-cookie")
def set_csrf_cookie(request):
    return {"csrftoken": get_token(request)}

@router.post("/login")
def login_user(request, payload: schemas.SignInSchema):
    user = authenticate(request, email=payload.email, password=payload.password)
    if user is not None:
        login(request, user)
        return {"success": True}
    return {"success": False, "error": "Invalid credentials"}

@router.post("/logout", auth=django_auth)
def logout_view(request):
    logout(request)
    return {"message": "Logged out"}

@router.get("/user", auth=django_auth)
def get_user(request):
    return request.user

@router.post("/register")
def register_user(request, payload: schemas.SignInSchema):
    try: 
        user = CustomUser.objects.create_user(email=payload.email, password=payload.password)
        return {"email": user.email}
    except Exception as e:
        return {"error": str(e)}