# Use uma imagem oficial do Python sobre Alpine (3.13)
FROM python:3.13-alpine

# Diretório de trabalho
WORKDIR /app

# Instala dependências de build para compilar pacotes Python nativos
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Atualiza pip
RUN pip install --upgrade pip

# 3. copia só os arquivos de definição de dependências para 
#    acelerar o cache de camada do Docker
COPY /pyproject.toml /poetry.lock* ./

# 4. instala o CLI do uv e cria o virtualenv local
RUN pip install --no-cache-dir uv \
 && uv venv \
 && source .venv/bin/activate \
 && uv sync

# 6. adiciona o binário do venv ao PATH
ENV PATH="/app/.venv/bin:${PATH}"

# Copia todo o código da aplicação
COPY . .

# Expõe a porta usada pelo FastAPI/Uvicorn
EXPOSE 8000

# Comando padrão para iniciar o servidor FastAPI via uv
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
