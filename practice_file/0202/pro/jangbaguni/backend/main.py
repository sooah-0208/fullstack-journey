from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,                  
    allow_methods=["*"],
    allow_headers=["*"],
)

class loginModel(BaseModel):
    email: str
    pwd: str

class bagModel(BaseModel):
    no: int
    product: str
    price: str

@app.get('/')
def get():
    return{"status": True}


users = [
    {"email": "1@1", "pwd": "1111", "id": 1},
    {"email": "2@2", "pwd": "2222", "id": 2},
    {"email": "3@3", "pwd": "3333", "id": 3},
]

def user_check(email: str, pwd: str):
    for user in users:
        if user["email"] == email and user["pwd"] == pwd:
            return user   
    return None  

@app.post('/login')
def login(data:loginModel, response: Response):
    user = user_check(data.email, data.pwd)
    if not user:
        return {'status':False}
        
    response.set_cookie(
        key="token",
        value=str(user['id']),
        httponly=True,
        samesite="lax",
        path='/'
    )
    print(data.email, data.pwd)
    return {"status": True, "user":user}

@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(
        key="token",
        path="/"
    )
    return {"status": True}

@app.get('/bag')
def me(request: Request):
    bags = request.cookies.get("jangbaguni")
    token = request.cookies.get("token")
    if not bags:
        return{"status":False}
    user = get_user_id(token)
    if not user:
        return{"status":False}
    return{"status":True, "bags": bags}

def get_user_id(token:str):
    for user in users:
        if str(user['id']) == token:
            return user
        return None

@app.get('/me')
def me(request: Request):
    token = request.cookies.get("token")
    if not token:
        return{"status":False}
    user = get_user_id(token)
    if not user:
        return{"status":False}
    return{"status":True, "user":{"id":user['id'], "email":user['email']}}