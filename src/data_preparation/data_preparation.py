from pymongo import MongoClient

client_mongo=MongoClient('localhost')
db=client_mongo["dbBTGFondos"]


#########################################################################
## ESTE SERVICIO ES DE PRUEBAS PARA PODER CREAR RAPIDAMENTE EL USUARIO ##
#########################################################################
def insertarCliente():

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

#########################################################################
## ESTE SERVICIO ES DE PRUEBAS PARA PODER CREAR RAPIDAMENTE LOS FONDOS ##
#########################################################################
def insertarFondos():

    fondos=db["fondos"]
    fondos_to_insert=[
        {
            "_id": "1",
            "nombre": "FPV_BTG_PACTUAL_RECAUDADORA",
            "monto_minimo_vinculacion": "75000",
            "categoria": "FPV",
            "id": 1
        },
        {
            "_id": "2",
            "nombre": "FPV_BTG_PACTUAL_ECOPETROL",
            "monto_minimo_vinculacion": "125000",
            "categoria": "FPV",
            "id": 2
        },
        {
            "_id": "3",
            "nombre": "DEUDAPRIVADA",
            "monto_minimo_vinculacion": "50000",
            "categoria": "FIC",
            "id": 3
        },
        {
            "_id": "4",
            "nombre": "FDO-ACCIONES",
            "monto_minimo_vinculacion": "250000",
            "categoria": "FIC",
            "id": 4
        },
        {
            "_id": "5",
            "nombre": "FPV_BTG_PACTUAL_DINAMICA",
            "monto_minimo_vinculacion": "100000",
            "categoria": "FPV",
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