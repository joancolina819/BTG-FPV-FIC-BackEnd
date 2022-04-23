from fastapi import FastAPI
from pymongo import MongoClient

client_mongo=MongoClient('localhost')

app = FastAPI()

@app.get("2FVC/fondos")
async def getFondos():

    db=client_mongo["dbBTGFondos"]

    fondos=db["fondos"]
    fondos_list=[]
    for documento in fondos.find({}):
        fondos_list.append(documento)
        
    return fondos_list

@app.get("/")
async def root():
    return {"message": "Hello World"}