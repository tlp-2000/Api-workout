from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# Caminho do arquivo SQLite
SQLALCHEMY_DATABASE_URL = settings.database_url

# Cria o engine (conexão com o banco)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

# Cria a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()

# Dependência de sessão para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
