from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

# In-memory user store (replace with database later)
users_db = {}


class UserRegister(BaseModel):
    login: str
    password: str


class UserLogin(BaseModel):
    login: str
    password: str


@router.get("/")
def get_auth() -> dict[str, str]:
    """
    Get auth endpoint.

    Parameters:
        None

    Returns:
        dict[str, str]: Success message indicating the endpoint is operational.
    """
    return {"message": "Auth endpoint is operational"}


@router.post("/register")
def register(user: UserRegister) -> dict[str, str]:
    """
    Register a new user.

    Parameters:
        user: UserRegister - User registration data (login, password)

    Returns:
        dict[str, str]: Success message
    """
    if user.login in users_db:
        raise HTTPException(status_code=400, detail="User with this login already exists")
    
    if len(user.password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
    
    users_db[user.login] = user.password
    return {"message": "User registered successfully", "login": user.login}


@router.post("/login")
def login(user: UserLogin) -> dict[str, str]:
    """
    Login user.

    Parameters:
        user: UserLogin - User login data (login, password)

    Returns:
        dict[str, str]: Success message with login
    """
    if user.login not in users_db:
        raise HTTPException(status_code=401, detail="Invalid login or password")
    
    if users_db[user.login] != user.password:
        raise HTTPException(status_code=401, detail="Invalid login or password")
    
    return {"message": "Login successful", "login": user.login}
