from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os
import logging

logger=logging.getLogger()
logger.setLevel(logging.INFO)
client_mongo=MongoClient('localhost')
# base_path= os.environ["basePath"]
base_path= "/2FVC"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["acces-control-allow-methods"]
    )

@app.get(base_path+"/fondos")
async def getFondos():

    db=client_mongo["dbBTGFondos"]

    fondos=db["fondos"]

    fondos_list=[]
    contador =1
    for documento in fondos.find({}):
        documento["id"]=contador
        contador=contador+1
        fondos_list.append(documento)
        
    return fondos_list


@app.get(base_path+"/myfondos")
async def getFondos(id_client: str):

    db=client_mongo["dbBTGFondos"]

    clientes=db["clientesFondos"]
    cliente=clientes.find({
        "_id":id_client
    })[0]

    fondos=db["fondos"]
    my_fondos_list=[]

    contador =1
    for fondo in cliente["fondos"]:
        my_fondo=fondos.find({
            "_id":fondo
            })[0]
        my_fondo["id"]=contador
        contador+1
        my_fondos_list.append(my_fondo)
        
    return my_fondos_list

@app.get(base_path+"/usuario")
async def getUsuario():

    db=client_mongo["dbBTGFondos"]

    clientes=db["clientesFondos"]

    return clientes.find({
        "nombre":"Joan David",
        "apellido": "Colina Echeverry"
    })[0]


#########################################################################
## ESTE SERVICIO ES DE PRUEBAS PARA PODER CREAR RAPIDAMENTE EL USUARIO ##
#########################################################################
@app.post("/cliente")
async def root():
    db=client_mongo["dbBTGFondos"]

    clientes=db["clientesFondos"]
    cliente_to_insert={
        "_id":"1",
        "nombre":"Joan David",
        "apellido":"Colina Echeverry",
        "edad":24,
        "fondos":[],
        "presupuesto":500000
    }
    clientes.insert_one(cliente_to_insert)
    return "Cliente insertado correctamente"