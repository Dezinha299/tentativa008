from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}


def create_estudante(estudante: Estudante):
    return estudante


def update_estudante(id_estudante: int):
    return id_estudante > 0


def delete_estudante(id_estudante: int):
    return id_estudante > 0


class Estudante(BaseModel):
    nome: str
    curso: str
    ativo: bool

