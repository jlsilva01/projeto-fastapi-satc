from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Item

router = APIRouter()

# Store in-memory
_db: List[Item] = []

@router.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(i.id == item.id for i in _db):
        raise HTTPException(status_code=400, detail="Item já existe")
    _db.append(item)
    return item

@router.get("/items", response_model=List[Item])
def list_items():
    return _db

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in _db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, novo: Item):
    for idx, item in enumerate(_db):
        if item.id == item_id:
            _db[idx] = novo
            return novo
    raise HTTPException(status_code=404, detail="Item não encontrado")

@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, item in enumerate(_db):
        if item.id == item_id:
            _db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item não encontrado")

# Criar o rota raiz com o Hello World
@router.get("/", response_model=str)
def read_root():
    return "Bem vindo ao exemplo de CRUD em memória com FastAPI!"

