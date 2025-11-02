from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter()

#cria uma nova categoria
@router.post("/", response_model=schemas.CategoriaRead, status_code=201)
def criar_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    nova_categoria = crud.create_categoria(db=db, categoria=categoria)
    return nova_categoria

#lista todas as categorias
@router.get("/", response_model=List[schemas.CategoriaRead])
def listar_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = crud.get_categorias(db, skip=skip, limit=limit)
    return categorias

#retorna categoria pelo id
@router.get("/{categoria_id}", response_model=schemas.CategoriaRead)
def obter_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.get_categorias_id(db, categoria_id=categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

#Depends(get_db) = injeta automaticamente a conexão com o banco.