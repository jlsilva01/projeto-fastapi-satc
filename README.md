# CRUD FastAPI In-Memory

[![Lint & Tests](https://img.shields.io/github/actions/workflow/status/jlsilva01/projeto-fastapi-satc/main.yml?branch=main)](https://github.com/jlsilva01/projeto-fastapi-satc/actions)  
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://github.com/jlsilva01/projeto-fastapi-satc)  
[![Docker Pulls](https://img.shields.io/docker/pulls/jlsilva01/projeto-fastapi-satc)](https://hub.docker.com/r/jlsilva01/projeto-fastapi-satc)  
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://jlsilva01.github.io/projeto-fastapi-satc/)  

Este projeto é um exemplo de API CRUD simples, construída com **FastAPI**, onde todos os dados são mantidos **em memória** (sem banco de dados).

---

## 📋 Funcionalidades

- **CRUD completo** de recursos (Create, Read, Update, Delete)  
- **Em memória**: não requer nenhum banco de dados externo  
- **Validação automática** de dados com Pydantic  
- **Documentação interativa** via OpenAPI (Swagger UI + ReDoc)  
- **Testes e lint** automatizados via **pre-commit**  
- **Containerização** com Docker e Docker Compose  
- **Documentação estática** gerada com MkDocs  

---

## 🔧 Tecnologias

- **Linguagem:** Python 3.11+  
- **Framework web:** FastAPI  
- **Servidor ASGI:** Uvicorn  
- **Qualidade de código:** pre-commit (ruff, black, isort, flake8, mypy)  
- **Container:** Docker  
- **Orquestração local:** Docker Compose  
- **Documentação:** MkDocs + mkdocstrings + mkdocs-material

---

## 🚀 Como usar

### 1. Clonar o repositório

```bash
git clone https://github.com/jlsilva01/projeto-fastapi-satc.git
cd projeto-fastapi-satc
```

### 2. Instalar dependências & pre-commit

```bash
uv venv
source .venv/bin/activate
uv sync

# instalar hooks do pre-commit
uv run pre-commit install
```

### 3. Executar localmente

```bash
uv run uvicorn app.main:app --reload
```

Acesse a API em `http://localhost:8000` e a documentação automática em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc:       `http://localhost:8000/redoc`

---

## 🐳 Docker & Docker Compose

1. **Construir a imagem**  
    ```bash
    docker build -t projeto-fastapi-satc .
    ```

2. **Executar com Docker**  
   ```bash
   docker run -d -p 8000:8000 projeto-fastapi-satc
   ```

3. **Ou usar Docker Compose**  
   ```bash
   docker-compose up -d
   ```
   - Serviço exposto em `http://localhost:8000`

---

## 📚 Documentação (MkDocs)

Toda a documentação está em `docs/`:

```bash
uv run mkdocs build
uv run mkdocs serve
```

Acesse o site em `http://127.0.0.1:8000`.

Para publicar o site estático:

```bash
uv run mkdocs gh-deploy
```

---

## 🤝 Contribuindo

1. Abra uma **issue** para discutir sua feature ou bug.  
2. Faça um Fork do repo.
2. Crie um **branch**:  

   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```
3. Faça suas alterações e **commit** seguindo o [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).  
4. Envie um **pull request** para `main`.  
5. Aguarde revisão e merge.

---

## ⚖️ Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).  

---

## Referências

- FastAPI: https://fastapi.tiangolo.com/  
- Uvicorn: https://www.uvicorn.org/  
- Pydantic: https://pydantic-docs.helpmanual.io/  
- pre-commit: https://pre-commit.com/  
- Ruff: https://beta.ruff.rs/  
- Black: https://black.readthedocs.io/  
- isort: https://pycqa.github.io/isort/  
- flake8: https://flake8.pycqa.org/  
- MyPy: http://mypy-lang.org/  
- Docker: https://www.docker.com/  
- Docker Compose: https://docs.docker.com/compose/  
- MkDocs: https://www.mkdocs.org/  
- mkdocstrings: https://mkdocstrings.github.io/  
- Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/  
- Estruturação de projetos de Data Science: https://codecut.ai/how-to-structure-a-data-science-project-for-readability-and-transparency-2/  


