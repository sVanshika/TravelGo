from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, EmailStr
from core.firebase import create_user, verify_firebase_token
import os
import requests 

from dotenv import load_dotenv

load_dotenv()
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")


router = APIRouter()

# Request Model for Signup
class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str  # This is used only in request, not response

# Response Model (Excludes Password)
class UserResponse(BaseModel):
    name: str
    email: EmailStr

# Request model for login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Response model for login
class LoginResponse(BaseModel):
    idToken: str  # Token jo frontend use karega


@router.post("/signup", response_model=UserResponse)  
def signup(user: SignupRequest):
    """
    Signup Endpoint: Creates a new user in Firebase Authentication.
    """
    if not user.email or not user.password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    # Call Firebase function to create user
    create_user(user.name, user.email, user.password)

    return UserResponse(name=user.name, email=user.email) 

@router.post("/login", response_model=LoginResponse)
def login(user: LoginRequest):
    
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    
    payload = {
        "email": user.email,
        "password": user.password,
        "returnSecureToken": True
    }

    response = requests.post(url, json=payload)
    data = response.json()

    if "idToken" not in data:
        raise HTTPException(status_code=400, detail=data.get("error", {}).get("message", "Login failed"))

    return {"idToken": data["idToken"]}

@router.get("/protected")
def protected_route(authorization: str = Header(None)):
    """
    Protected API Route: Requires Firebase Token.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization Token")

    token = authorization.split("Bearer ")[-1]
    user = verify_firebase_token(token)

    return {"message": "Access granted!", "user": user}
