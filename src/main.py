from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .password_hashing import verify_password
from .token_api import verify_jwt_token, generate_jwt_token
from .faked_users import users
from .createDataFrame import createDataFrame
import json

app = FastAPI()

bearer_scheme = HTTPBearer()

df = createDataFrame("data/fastfood.csv")

@app.get("/fastfood-nutrition")
def protected_route(authorization: HTTPAuthorizationCredentials = Depends(bearer_scheme), food_name: Union[str, None] = None):
    token = authorization.credentials
    payload = verify_jwt_token(token)
    if payload:
        result = df.copy()
        if food_name is not None:
            result = result[["restaurant", "item", "total_fat", "sugar", "sodium"]]
            result = result[result.item.str.contains(food_name, case=False)]
            result = result.sort_values(by=["total_fat", "sugar", "sodium"], ascending=[False, False, False]).head()
        return json.loads(result.to_json(orient="records"))
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
