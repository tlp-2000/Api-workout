from sqlalchemy import Column, ForeignKey, Integer, String,Float
from app.database import Base
from sqlalchemy.orm import relationship

#Base = Transaforma as Classe do Python Em Tableas Sql
#index = True - Cria Um Indice No Banco
#nullable = Campo Obrigatorio (nao pode ser nulo)

class Categoria(Base):
    __tablename__ = "categorias"

    pk_id = Column(Integer, primary_key=True, index=True) #CHAVE PRIMARIO AUTOINCREMENTAL
    id = Column(String, unique=True, index=True)         #IDENTIFICADOR PADRAO SERA UM UUID EM STRING
    nome = Column(String(40), nullable=False)

    atletas = relationship("Atleta",back_populates="categoria")


class CentroTreinamento(Base):
    __tablename__ = "centro_treinamento"

    pk_id = Column(Integer,primary_key=True,index=True)  #CHAVE PRIMARIO AUTOINCREMENTAL
    id = Column(String,unique=True,index=True)            #IDENTIFICADOR PADRAO SERA UM UUID EM STRING
    nome = Column(String(20),nullable=False)  
    endereco = Column(String(50),nullable = False)
    proprietario = Column(String(30),nullable=False)

    atletas = relationship("Atleta",back_populates="centro_treinamento")



class Atleta(Base):
    __tablename__ = "atletas"
    pk_id = Column(Integer,primary_key = True,index = True)
    id = Column(String,unique=True,index=True)  
    nome = Column(String(30),nullable=False) 
    cpf = Column(String(11),nullable=False) 
    idade = Column(Integer,nullable=False)
    peso = Column(Float,nullable=False)

    #Chaves Estrageiras
    categoria_id = Column(Integer,ForeignKey("categorias.pk_id"))
    centro_treinamento_id = Column(Integer,ForeignKey("centro_treinamento.pk_id"))

    #RELACIONAMENTO REVERSOS
    categoria = relationship("Categoria", back_populates="atletas")
    centro_treinamento = relationship("CentroTreinamento", back_populates="atletas")


