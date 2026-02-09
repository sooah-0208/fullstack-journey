from fastapi import APIRouter

router = APIRouter(tags=['게시판'], prefix='/board')

@router.get(path="")
def get_root():
    return {"method": "GET"}

@router.post(path="")
def post_root():
    return {"method": "POST"}

@router.put(path="")
def put_root():
    return {"method": "PUT"}

@router.delete(path="")
def delete_root():
    return {"method": "DELETE"}

@router.patch(path="")
def patch_root():
    return {"method": "PATCH"}

