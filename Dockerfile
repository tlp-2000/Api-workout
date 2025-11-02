# Imagem base com Python
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Exposição da porta do FastAPI
EXPOSE 8000

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
