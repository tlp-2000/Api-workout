from fastapi import FastAPI
from app.database import Base, engine
from app.routers import categoria,centro_treinamento,atletas

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="WorkoutAPI")


# Inclui o router da categoria
app.include_router(categoria.router, prefix="/categorias", tags=["Categorias"])
app.include_router(centro_treinamento.router,prefix="/centro_treinamento",tags=['Centros De Treinamentos'])
app.include_router(atletas.router, prefix="/atletas",tags=["Atleatas"])



@app.get("/")
def root():
    return {"message": "WorkoutAPI está rodando!"}
