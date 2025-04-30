from fastapi import FastAPI
from app.api.v1.routes import router as v1_router

app = FastAPI(
    title="CRUD API",
    version="1.0.0",
    description="Exemplo de CRUD em memória com versionamento de endpoints"
)

# prefixo /api/v1 para versionamento
app.include_router(v1_router, prefix="/api/v1")
