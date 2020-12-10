from db.cliente_db import ClienteInDB
from db.cliente_db import get_cliente,save_cliente,delete_cliente,update_cliente
from models.cliente_model import Cliente
from datetime import date
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.post("/cliente/registroSave")
async def save_cliente(cliente: Cliente):
    return save_cliente(cliente)

@api.put("/cliente/registroPut")
async def update_cliente(cliente: Cliente):
    db_response=save_cliente(cliente)
    if db_response==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        return db_response

@api.delete("/cliente/registroDel")
async def delete_cliente(documento: str):
    db_response=delete_cliente(documento)
    if db_response==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        return db_response

@api.get("/cliente/registroGet")
async def get_cliente(documento: str):
    cliente=get_cliente(documento)
    if cliente==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        return cliente

@api.get("/cliente/registroGet/{documento}")
async def get_cliente(documento:str):
    cliente=get_cliente(documento)
    if cliente==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        return cliente


@api.get("/")
async def root():
    return {"message":"si funciona"}