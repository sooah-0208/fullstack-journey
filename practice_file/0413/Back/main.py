from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import save_db, board

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
    "http://aiedu.tplinkdns.com",
    "http://aiedu.tplinkdns.com:6100",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(save_db.router)
app.include_router(board.router)

@app.get('/')
def read_root():
    return {"message":"Hello World"}