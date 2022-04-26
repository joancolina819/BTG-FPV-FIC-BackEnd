from pymongo import MongoClient

client_mongo=MongoClient('localhost')
db=client_mongo["dbBTGFondos"]


#########################################################################
## ESTE SERVICIO ES DE PRUEBAS PARA PODER CREAR RAPIDAMENTE EL USUARIO ##
#########################################################################
def eliminarCliente():

    myquery = { "_id": "1" }

    clientes=db["clientesFondos"]

    clientes.delete_one(myquery)
    return "Cliente eliminado correctamente"


def insertarCliente():

    clientes=db["clientesFondos"]
    cliente_to_insert={
        "_id":"1",
        "nombre":"Joan David",
        "identifcacion":"1144587895",
        "correoElectronico":"JoandaviPrueba@outlook.com",
        "apellido":"Colina Echeverry",
        "edad":24,
        "fondos":[],
        "invesment":[],
        "presupuesto":500000
    }
    clientes.insert_one(cliente_to_insert)
    return "Cliente insertado correctamente"

#########################################################################
## ESTE SERVICIO ES DE PRUEBAS PARA PODER CREAR RAPIDAMENTE LOS FONDOS ##
#########################################################################
def insertarFondos():

    fondos=db["fondos"]
    fondos_to_insert=[
        {
            "_id": "1",
            "nombre": "FPV_BTG_PACTUAL_RECAUDADORA",
            "monto_minimo_vinculacion": 75000,
            "categoria": "FPV",
            "inversion_cliente":0,
            "id": 1
        },
        {
            "_id": "2",
            "nombre": "FPV_BTG_PACTUAL_ECOPETROL",
            "monto_minimo_vinculacion": 125000,
            "categoria": "FPV",
            "inversion_cliente":0,
            "id": 2
        },
        {
            "_id": "3",
            "nombre": "DEUDAPRIVADA",
            "monto_minimo_vinculacion": 50000,
            "categoria": "FIC",
            "inversion_cliente":0,
            "id": 3
        },
        {
            "_id": "4",
            "nombre": "FDO-ACCIONES",
            "monto_minimo_vinculacion": 250000,
            "categoria": "FIC",
            "inversion_cliente":0,
            "id": 4
        },
        {
            "_id": "5",
            "nombre": "FPV_BTG_PACTUAL_DINAMICA",
            "monto_minimo_vinculacion": 100000,
            "categoria": "FPV",
            "inversion_cliente":0,
            "id": 5
        }
    ]

    fondos.insert_many(fondos_to_insert)
    return "fondos insertados correctamente"

#########################################################################
## ESTE SERVICIO ES DE PRUEBAS PARA CORREGIR RAPIDAMENTE EL CLIENTE   ##
#########################################################################
def corregirCliente():

    clientes=db["clientesFondos"]
    clientes.update_one(
        {
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