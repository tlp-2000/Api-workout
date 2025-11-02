from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

''' 
response_model = define o modelo Pydantic usado para validar e formatar a resposta JSON.
Assim garantimos que o cliente recebe apenas os campos que queremos.

Depends = O FastAPI chama a função get_db() antes de executar a rota, e injeta automaticamente uma 
sessão de banco (Session) na função.
Isso evita ter que abrir/fechar conexão manualmente em cada rota.
'''
router = APIRouter()

@router.post("/",response_model=schemas.CentroTreinamentoRead,status_code=201)
def criar_centro_treinamento(centro: schemas.CentroTreinamentoCreate, db: Session = Depends(get_db)):
    novo_centro = crud.create_centro_treinamento(db=db,centro=centro)
    return novo_centro

@router.get("/",response_model=List[schemas.CentroTreinamentoRead])
def listar_centro_treinamentos(skip:int=0, limit:int=100, db:Session = Depends(get_db)):
    centros = crud.get_centro_treinamento(db=db,skip=skip,limit=limit)
    return centros

@router.get("/{centro_id}",response_model=schemas.CentroTreinamentoRead)
def obter_centro_treinamento(centro_id,db:Session = Depends(get_db)):
    centro = crud.get_centro_treinamento_id(db,centro_id=centro_id)
    if centro is None:
        raise HTTPException(status_code=404,detail="NAO ENCOTRADO")
    return centro


