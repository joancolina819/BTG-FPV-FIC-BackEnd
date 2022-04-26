# BTG-FPV-FIC-BackEnd
repositorio para almacenar el codigo fuente de  BTG FPV-FIC

--------------------------------------------------------------------------------------------------

Pasos para la ejecucion del codigo sin utilizar Docker (Se da por supuesto que ya se tiene python instalado y puede ejecutar comando pip):

1. Para la descarga de todas las dependencias:

 pip install -r requirements.txt

2. Para ejecutar el API REST:

python -m uvicorn src.gestion_fondos.gestor_fondos:app --reload

3. para utilizar lo servicios Ejecute la interfaz grafica o utilice otra aplicacion com Postman 
