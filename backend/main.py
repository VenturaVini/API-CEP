from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import api_cep

app = FastAPI()

# Permite requisições de qualquer origem
origins = ["*"]  # Isso permite todas as origens. Para restringir, defina uma lista de URLs específicas.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Inclui as rotas
app.include_router(api_cep.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4800)
