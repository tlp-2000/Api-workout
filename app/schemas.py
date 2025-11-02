from pydantic import BaseModel, Field
import uuid
from typing import Optional

# Base compartilhada PARA COISAS COMUNS DA TABELA COMO
class CategoriaBase(BaseModel):
    nome: str = Field(description="Nome da categoria",examples=["Musculaçao"],max_length=60)


class CategoriaCreate(CategoriaBase):
    pass

# Modelo de retorno (saída) PARA O METODO GET 
class CategoriaRead(CategoriaBase):
    pk_id: int
    id: str

#PERMITE QUE O PYDANTIC LEIA OBJETOS SQLALCHEMY DIRETAMENTE
    class Config:
        orm_mode = True



class CentroTreinamentoBase(BaseModel):
    nome: str = Field(description="Nome",examples=['Centro Y'],max_length=20)
    endereco :str = Field(description="ENDERECO",examples=["RUA Y"],max_length=50)
    proprietario : str = Field(description="DONO DO CENTRO",examples=["Rogerio"],max_length=30)


class CentroTreinamentoCreate(CentroTreinamentoBase):
    pass


class CentroTreinamentoRead(CentroTreinamentoBase):
    pk_id : int
    id: str



class Config: # type: ignore
    orm_mode = True



class AtletaBase(BaseModel):
    nome : str = Field(description="Nome Do Atleta",examples=["JOAO"],max_length=30)
    cpf : str = Field(description="Cpf Do Atleta",examples=["01234567009"],max_length=11)
    idade: int
    peso: int
    categoria_id: int
    centro_treinamento_id: int


class AtletaCreate(AtletaBase):
    pass

class AtletaRead(AtletaBase):
    pk_id : int
    id : str
    nome: str
    cpf: str
    idade: int
    peso: int

    categoria : Optional[CategoriaRead]
    centro_treinamento : Optional[CentroTreinamentoRead]



class Config:
    orm_mode = True