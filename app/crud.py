from sqlalchemy.orm import Session
from app import modelos, schemas
import uuid


#db.query = cria uma consulta no banco de dados
#filter = igual a um clasula where
#limit(limit) = LIMITAR A QUANTIDADE DE REGISTROS RETORNAVEL
#offset(skip) = PULA OS PRIMEIROS N REGISTROS

#lista todas as categorias com paginaçao
def get_categorias(db:Session,skip: int = 0, limit : int = 100):
    return db.query(modelos.Categoria).offset(skip).limit(limit).all()

#busca a categoria pelo pk_id chave primaria
def get_categorias_id(db:Session,categoria_id : int):
    return db.query(modelos.Categoria).filter(modelos.Categoria.pk_id == categoria_id).first()


#cria uma nova categoria com uuid4 automatico
def create_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = modelos.Categoria(
        id=str(uuid.uuid4()),  # gera UUID automático
        nome=categoria.nome
    ) # type: ignore
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def get_centro_treinamento(db:Session,skip:int = 0, limit : int = 100):
    return db.query(modelos.CentroTreinamento).offset(skip).limit(limit).all()


def get_centro_treinamento_id(db:Session,centro_id:int):
    return db.query(modelos.CentroTreinamento).filter(modelos.CentroTreinamento.pk_id == centro_id).first()


def create_centro_treinamento(db:Session,centro: schemas.CentroTreinamentoCreate):
    db_centro = modelos.CentroTreinamento(
        id=str(uuid.uuid4()),
        nome = centro.nome, # type: ignore
        endereco=centro.endereco,
        proprietario=centro.proprietario
    ) # type: ignore


    db.add(db_centro)    #Adicionar um novo objeto a sessao
    db.commit()          #Confimar a operaçao
    db.refresh(db_centro) #Atualizar o banco de dados
    return db_centro

def get_atletas(db:Session, skip: int = 0, limit : int = 100):
    return db.query(modelos.Atleta).offset(skip).limit(limit).all()

def get_atletas_id(db:Session,atleta_id:int):
    return db.query(modelos.Atleta).filter(modelos.Atleta.pk_id == atleta_id).first()

def create_atleta(db:Session,atleta:schemas.AtletaCreate):
    db_atleta = modelos.Atleta(
        id=str(uuid.uuid4()),
        nome = atleta.nome,
        cpf = atleta.cpf, # type: ignore
        idade = atleta.idade,
        peso = atleta.peso,
        categoria_id = atleta.categoria_id,
        centro_treinamento_id = atleta.centro_treinamento_id
    ) # type: ignore
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

def get_atletas_by_categoria(db:Session, categoria_id : int):
    return db.query(modelos.Atleta).filter(modelos.Atleta.categoria_id == categoria_id).all()

def get_atletas_by_centro_treinamento(db:Session, centro_treinamento_id : int):
    return db.query(modelos.Atleta).filter(modelos.Atleta.centro_treinamento_id == centro_treinamento_id).all()