from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/",response_model=schemas.AtletaRead,status_code=201)
def criar_atleta(atleta:schemas.AtletaCreate,db:Session= Depends(get_db)):
    novo_atleta = crud.create_atleta(db=db,atleta=atleta)
    return novo_atleta

@router.get("/",response_model=List[schemas.AtletaRead])
def lista_atleta(skip:int=0,limit:int=100,db:Session = Depends(get_db)):
    atletas = crud.get_atletas(db, skip = skip, limit = limit)
    return atletas

@router.get("/{atleta_id}",response_model=schemas.AtletaRead)
def obter_atleta(atleta_id : int, db:Session = Depends(get_db)):
    atleta = crud.get_atletas_id(db, atleta_id=atleta_id)
    if atleta is None:
        raise HTTPException(status_code=401,detail="NAO ENCONTRADO")
    return atleta


@router.get("/categoria/{categoria_id}",response_model=List[schemas.AtletaRead])
def listar_atletas_por_categoria(categoria_id: int, db: Session = Depends(get_db)):
    atletas = crud.get_atletas_by_categoria(db,categoria_id=categoria_id)
    if atletas is None:
        raise HTTPException(status_code=401,detail="NENHUM ATLETA ENCONTRADO POR ESSA CATEGORIA")
    return atletas


@router.get("/centro_treinamento/{centro_treinamento_id}",response_model=List[schemas.AtletaRead])
def listar_atletas_por_centro_treinamento(centro_treinamento_id: int, db : Session = Depends(get_db)):
    atletas = crud.get_atletas_by_centro_treinamento(db, centro_treinamento_id= centro_treinamento_id)
    if atletas is None:
        raise HTTPException(status_code=401,detail="NENHUM ATLETA ENCONTRADO POR ESSE CENTRO DE TREINAMENTO")
    return atletas
        


