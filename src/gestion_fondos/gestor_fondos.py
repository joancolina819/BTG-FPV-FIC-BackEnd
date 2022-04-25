from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os
from src.utils.util import build_error_response
from src.data_preparation.data_preparation import insertarCliente, insertarFondos, corregirCliente, eliminarCliente
import logging
import uuid
from datetime import datetime


logger=logging.getLogger()
logger.setLevel(logging.INFO)

client_mongo=MongoClient('localhost')
db=client_mongo["dbBTGFondos"]
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
async def get_fondos():
    logger.info("## start get_fondos")
    try:

        fondos=db["fondos"]
        fondos_list =list(fondos.find({}))
        logger.info(f"todos los fondos {fondos_list}")

        logger.info("## exit get_fondos")
        return fondos_list
    except BaseException as e:
        logger.error("## exit get_fondos")
        return build_error_response(e)


@app.get(base_path+"/myfondos")
async def get_my_fondos(id_client: str):
    logger.info("## start get_my_fondos")
    try:

        clients=db["clientesFondos"]
        client=clients.find({
            "_id":id_client
        })[0]
        logger.info(f"cliente {client}")

        fondos=db["fondos"]
        my_fondos_list=[]   

        for fondo in client["fondos"]:
            my_fondo=fondos.find({
                "_id":fondo
                })[0]
            my_fondos_list.append(my_fondo)
            
        logger.info(f"todos los fondos del cliente {my_fondos_list}")

        logger.info("## exit get_my_fondos")
        return my_fondos_list
    except BaseException as e:
        logger.error("## exit get_my_fondos")
        return build_error_response(e)



@app.get(base_path+"/usuario")
async def get_user(client_name: str,client_last_name: str):
    logger.info("## start get_user")
    try:

        clients=db["clientesFondos"]

        logger.info("## exit get_user")
        return clients.find({
            "nombre":client_name,
            "apellido": client_last_name
        })[0]
    except BaseException as e:
        logger.error("## exit get_user")
        return build_error_response(e)


@app.post(base_path+"/cancelacion")
async def cancellation(id_client: str,id_fondo: str):
    logger.info("## start cancellation")
    try:

        clients=db["clientesFondos"]
        client=clients.find({
            "_id":id_client
        })[0]
        logger.info(f"cliente {client}")

        fondos=db["fondos"]
        my_fondo=fondos.find({
                "_id":id_fondo
                })[0]
        fondos_client=client["fondos"]
        logger.info(f"fondo a cancelar {my_fondo}")

        if id_fondo in fondos_client:
            new_valor_to_client= int(client["presupuesto"]) + int(my_fondo["monto_minimo_vinculacion"])
            logger.info(f"nuevo presupuesto del cliente {new_valor_to_client}")
            fondos_client.remove(id_fondo)

            clients.update_one({
                "_id":id_client
            },
            {
                "$set":{
                    "fondos":fondos_client,
                    "presupuesto":new_valor_to_client
                }
            }
            )
            logger.info("cancelacion exitosa")
            insert_record_row(client,my_fondo,"CANCELACION")

            response="Cancelacion exitosa"
        else:
            fondo_name=my_fondo["nombre"]
            response=f"El cliente no esta suscrito al fondo {fondo_name}"
            logger.info(response)

        logger.info("## exit cancellation")
        return response
    except BaseException as e:
        logger.error("## exit cancellation")
        return build_error_response(e)


@app.post(base_path+"/suscripcion")
async def subscription(id_client: str,id_fondo: str):
    logger.info("## start subscription")
    try:

        ## OBTENCION DE LA COLECCION DE CLIENTE
        clients=db["clientesFondos"]
        client=clients.find({
            "_id":id_client
        })[0]
        logger.info(f"cliente {client}")

        ## OBTENCION DE LA COLECCION DE FONDOS
        fondos=db["fondos"]
        my_fondo=fondos.find({
                "_id":id_fondo
                })[0]
        fondos_client=client["fondos"]
        logger.info(f"fondo a suscribir {my_fondo}")

        if not id_fondo in fondos_client and int(client["presupuesto"]) >= int(my_fondo["monto_minimo_vinculacion"]):
            new_valor_to_client= int(client["presupuesto"]) - int(my_fondo["monto_minimo_vinculacion"])
            logger.info(f"nuevo presupuesto del cliente {new_valor_to_client}")
            fondos_client.append(id_fondo)

            clients.update_one({
                "_id":id_client
            },
            {
                "$set":{
                    "fondos":fondos_client,
                    "presupuesto":new_valor_to_client
                }
            }
            )
            logger.info("suscripcion exitosa")
            insert_record_row(client,my_fondo,"SUSCRIPCION")
            response="Suscripcion exitosa"
        else:
            fondo_name=my_fondo["nombre"]
            response=f"El cliente ya esta suscrito al fondo {fondo_name} o no cuenta con dinero suficiente para la suscripcion"
            logger.info(response)
        
        logger.info("## exit subscription")
        return response
    except BaseException as e:
        logger.error("## exit subscription")
        return build_error_response(e)


def insert_record_row(client,my_fondo,transaction_type):
    logger.info("## start insert_record_row")
    try:

        records=db["historialTransacciones"]
        
        transaction_to_insert={
            "_id":str(uuid.uuid4()),
            "nombre":client["nombre"],
            "apellido":client["apellido"],
            "edad":client["edad"],
            "hora de transaccion":datetime.now(),
            "fondo":my_fondo["nombre"],
            'tipo de transaccion':transaction_type
        }
        logger.info(f"trasaccion a insertar {transaction_to_insert}")
        records.insert_one(transaction_to_insert)
        logger.info("transaccion insertada")

        logger.info("## exit insert_record_row")
        return True
    except BaseException as e:
        logger.error(e)
        logger.info("## exit insert_record_row")
        return False


@app.get(base_path+"/historial")
async def get_record():
    logger.info("## start get_record")
    try:
    
        record=db["historialTransacciones"]

        record_list=[]
        counter =1
        for document in record.find({}):
            document["id"]=counter
            counter=counter+1
            record_list.append(document)
            logger.info(f"registro agregado al resultado {document}")
            
        logger.info("## exit get_record")
        return record_list
    except BaseException as e:
        logger.error("## exit get_record")
        return build_error_response(e)


@app.post(base_path+"/datapreparation")
async def data_preparation():
    logger.info("## start data_preparation")
    try:
        eliminarCliente()
        insertarCliente() 
        insertarFondos()
        logger.info("## exit data_preparation")
        return "Datos creados correctamente"
    except BaseException as e:
        logger.error("## exit data_preparation")
        corregirCliente()
        return build_error_response(e)