from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import save_db, board

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(save_db.router)
app.include_router(board.router)