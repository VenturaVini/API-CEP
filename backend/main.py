from fastapi import FastAPI
from routers import api_cep

app = FastAPI()


app.include_router(api_cep.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4800)