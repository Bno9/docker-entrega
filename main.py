from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ler_root():
    return {"mensagem": "Olá, mundo!"}
