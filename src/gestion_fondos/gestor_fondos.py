from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os
import logging
import uuid
from datetime import datetime


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
        contador=contador+1
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


@app.post(base_path+"/suscripcion")
async def suscripcion(id_client: str,id_fondo: str):

    ## CONEXION A LA BASE DE DATOS
    db=client_mongo["dbBTGFondos"]

    ## OBTENCION DE LA COLECCION DE CLIENTE
    clientes=db["clientesFondos"]
    cliente=clientes.find({
        "_id":id_client
    })[0]

    ## OBTENCION DE LA COLECCION DE FONDOS
    fondos=db["fondos"]
    my_fondo=fondos.find({
            "_id":id_fondo
            })[0]
    new_fondos=cliente["fondos"]

    if not id_fondo in new_fondos and int(cliente["presupuesto"]) > int(my_fondo["monto_minimo_vinculacion"]):
        new_valor_to_client= int(cliente["presupuesto"]) - int(my_fondo["monto_minimo_vinculacion"])
        new_fondos.append(id_fondo)

        clientes.update_one({
            "_id":id_client
        },
        {
            "$set":{
                "fondos":new_fondos,
                "presupuesto":new_valor_to_client
            }
        }
        )
        insert_registro_historial(cliente,my_fondo,"SUSCRIPCION")
        response="Suscripcion exitosa"
    else:
        response="El cliente ya esta suscrito al fondo o no se cuenta con dinero suficiente para la suscripcion"
        
    return response


def insert_registro_historial(cliente,my_fondo,tipo_transaccion):
    db=client_mongo["dbBTGFondos"]

    historial=db["historialTransacciones"]
    transaccion_to_insert={
        "_id":str(uuid.uuid4()),
        "nombre":cliente["nombre"],
        "apellido":cliente["apellido"],
        "edad":cliente["edad"],
        "hora de transaccion":datetime.now(),
        "fondo":my_fondo["nombre"],
        'tipo de transaccion':tipo_transaccion
    }
    historial.insert_one(transaccion_to_insert)


@app.get(base_path+"/historial")
async def getUsuario():

    db=client_mongo["dbBTGFondos"]

    historial=db["historialTransacciones"]

    historial_list=[]
    contador =1
    for documento in historial.find({}):
        documento["id"]=contador
        contador=contador+1
        historial_list.append(documento)
        
    return historial_list
#########################################################################
## ESTE SERVICIO ES DE PRUEBAS PARA PODER CREAR RAPIDAMENTE EL USUARIO ##
#########################################################################
@app.post("/cliente")
async def insertarCliente():
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


@app.post("/corregircliente")
async def corregirCliente():
    db=client_mongo["dbBTGFondos"]

    clientes=db["clientesFondos"]
    clientes.update_one({
        "_id":"1"
    },
    {
        "$set":{
            "fondos":[],
            "presupuesto":500000
        }
    },
    )
    return "Cliente corregido"