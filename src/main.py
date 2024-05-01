from fastapi import FastAPI, Depends, HTTPException, Form, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .password_hashing import verify_password
from .token_api import verify_jwt_token, generate_jwt_token
from .faked_users import users

app = FastAPI()

bearer_scheme = HTTPBearer()

@app.get("/fastfood-nutrition")
def protected_route(authorization: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = authorization.credentials
    payload = verify_jwt_token(token)
    if payload:
        return {"message": "Access granted to fastfood nutrition", "user_id": payload.get("user_id")}
    else:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    user = users[username]
    
    if user:
        if verify_password(password, users[username]["hashed_password"]):
            token = generate_jwt_token({'user_id': username})
            return {"token": token }
    
    raise HTTPException(status_code=401, detail="Invalid username or password")
