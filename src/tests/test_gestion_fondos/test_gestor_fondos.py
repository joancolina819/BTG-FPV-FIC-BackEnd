from fastapi.testclient import TestClient
from unittest.mock import patch
from unittest import mock

def import_class_app():
    from src.gestion_fondos.gestor_fondos import app
    test_client= TestClient(app)
    return test_client

@mock.patch("pymongo.collection.Collection.find")
def test_get_record(mock_find):
    test_client =import_class_app()

    expected =[
        {
            'test' : 'test', 
            'test1' : 'test1'
        }
    ]
    mock_find.return_value =expected

    response = test_client.get("/2FVC/historial")
    assert response.status_code == 200
    assert response.json() == expected


@mock.patch("pymongo.collection.Collection.find")
def test_get_fondos(mock_find):
    test_client =import_class_app()

    expected =[
        {
            'test' : 'test', 
            'test1' : 'test1'
        },
        {
            'test' : 'test', 
            'test1' : 'test1'
        }
    ]
    mock_find.return_value =expected

    response = test_client.get("/2FVC/fondos")
    assert response.status_code == 200
    assert response.json() == expected


@mock.patch("pymongo.collection.Collection.find")
def test_get_my_fondos(mock_find):
    test_client =import_class_app()

    expected_client =[
        {
            'test' : 'test', 
            'fondos' : '1'
        }
    ]
    expected_fondo =[
        {
            'test' : 'test', 
            'fondos' : '1'
        }
    ]
    mock_find.side_effect =[expected_client,expected_fondo]

    response = test_client.get("/2FVC/myfondos?id_client=1")
    assert response.status_code == 200
    assert response.json() == expected_fondo


@mock.patch("pymongo.collection.Collection.find")
def test_get_user(mock_find):
    test_client =import_class_app()

    expected =[
        {
            'test' : 'test', 
            'test1' : 'test1'
        }
    ]
    mock_find.return_value =expected

    response = test_client.get("/2FVC/fondos?client_name=test&client_last_name=test")
    assert response.status_code == 200
    assert response.json() == expected

@mock.patch("src.gestion_fondos.gestor_fondos.insert_record_row")
@mock.patch("pymongo.collection.Collection.find")
def test_cancellation(mock_find, mock_record):
    test_client =import_class_app()

    expected_client =[
        {
            'test' : 'test', 
            'fondos' : ["1","2"],
            "presupuesto":1000
        }
    ]
    expected_fondo =[
        {
            'test' : 'test', 
            "monto_minimo_vinculacion":50,
            "inversion_cliente":100
        }
    ]

    expected="Cancelacion exitosa"

    mock_record.return_value=None
    mock_find.side_effect =[expected_client,expected_fondo]

    response = test_client.post("/2FVC/cancelacion?id_client=1&id_fondo=1&invesment=10000")
    # assert response.status_code == 200
    assert response.json() == expected

@mock.patch("src.gestion_fondos.gestor_fondos.insert_record_row")
@mock.patch("pymongo.collection.Collection.find")
def test_no_cancellation(mock_find, mock_record):
    test_client =import_class_app()

    expected_client =[
        {
            'test' : 'test', 
            'fondos' : [],
            "presupuesto":1000
        }
    ]
    expected_fondo =[
        {
            "nombre":"test",
            'test' : 'test', 
            "monto_minimo_vinculacion":50,
            "inversion_cliente":100
        }
    ]

    expected="El cliente no esta suscrito al fondo test"

    mock_record.return_value=None
    mock_find.side_effect =[expected_client,expected_fondo]

    response = test_client.post("/2FVC/cancelacion?id_client=1&id_fondo=1&invesment=10000")
    assert response.status_code == 200
    assert response.json() == expected


@mock.patch("src.gestion_fondos.gestor_fondos.insert_record_row")
@mock.patch("pymongo.collection.Collection.find")
def test_subscription(mock_find, mock_record):
    test_client =import_class_app()

    expected_client =[
        {
            'test' : 'test', 
            'fondos' : [],
            "presupuesto":1000,
            "invesment":[]
        }
    ]
    expected_fondo =[
        {
            'test' : 'test', 
            "monto_minimo_vinculacion":50
        }
    ]

    expected="Suscripcion exitosa"

    mock_record.return_value=None
    mock_find.side_effect =[expected_client,expected_fondo]

    response = test_client.post("/2FVC/suscripcion?id_client=1&id_fondo=1&invesment=10000")
    assert response.status_code == 200
    assert response.json() == expected


@mock.patch("src.gestion_fondos.gestor_fondos.insert_record_row")
@mock.patch("pymongo.collection.Collection.find")
def test_no_subscription_by_id(mock_find, mock_record):
    test_client =import_class_app()

    expected_client =[
        {
            'test' : 'test', 
            'fondos' : ["1"],
            "presupuesto":1000,
            "invesment":[]
        }
    ]
    expected_fondo =[
        {
            "nombre":"test",
            'test' : 'test', 
            "monto_minimo_vinculacion":50
        }
    ]

    expected="El cliente ya esta suscrito al fondo test o no cuenta con dinero suficiente para la suscripcion"

    mock_record.return_value=None
    mock_find.side_effect =[expected_client,expected_fondo]

    response = test_client.post("/2FVC/suscripcion?id_client=1&id_fondo=1&invesment=10000")
    assert response.status_code == 200
    assert response.json() == expected

@mock.patch("pymongo.collection.Collection.insert_one")
def test_insert_record_row(mock_find):
    from src.gestion_fondos.gestor_fondos import insert_record_row
    invesment=1
    client ={
            'nombre' : 'test', 
            'apellido' : "test",
            "edad":"12"
        }
    my_fondo={
            'nombre' : 'test', 
        }
    transaction_type="test"

    mock_find.return_value =None

    response = insert_record_row(client,my_fondo,transaction_type,invesment)
    assert response == True

@mock.patch("pymongo.collection.Collection.insert_one")
def test_insert_record_row_failed(mock_find):
    from src.gestion_fondos.gestor_fondos import insert_record_row
    invesment=1
    client ={
            'nombre' : 'test', 
            'apellido' : "test",
            "edad":"12"
        }
    my_fondo={
            'nombre' : 'test', 
        }
    transaction_type="test"

    mock_find.side_effect = Exception("test")

    response = insert_record_row(client,my_fondo,transaction_type,invesment)
    assert response == False