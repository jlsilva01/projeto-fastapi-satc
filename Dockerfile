# Use uma imagem oficial do Python sobre Alpine (3.13)
FROM python:3.13-alpine

# Diretório de trabalho
WORKDIR /app

# Instala dependências de build para compilar pacotes Python nativos
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Atualiza pip
RUN pip install --upgrade pip

# Copia apenas o pyproject.toml para instalar dependências
COPY pyproject.toml .

# Instala dependências de CLI e do projeto
RUN pip install uv mkdocs mkdocstrings && \
    pip install .

# Copia todo o código da aplicação
COPY . .

# Expõe a porta usada pelo FastAPI/Uvicorn
EXPOSE 8001

# Comando padrão para iniciar o servidor FastAPI via uv
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
