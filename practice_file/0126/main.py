from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os  #물리적 파일 관리
from controller.urls import urls


app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__),'upload')
app.mount('/upload',StaticFiles(directory=static_dir), name='upload')



apis = urls()
for r in apis:
    app.include_router(r)
