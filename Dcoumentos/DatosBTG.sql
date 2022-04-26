-- ################################# INICIO CLIENTE #####################
INSERT INTO cliente (nombre, apellidos, ciudad)
VALUES ('Joan David', 'Colina Echeverry', 'Cali');

INSERT INTO cliente (nombre, apellidos, ciudad)
VALUES ('Angelica', 'Jimenez', 'Restrepo');

INSERT INTO cliente (nombre, apellidos, ciudad)
VALUES ('Jhonanta', 'Lozada', 'Cali');

INSERT INTO cliente (nombre, apellidos, ciudad)
VALUES ('Andres', 'Maya', 'Medellin');

INSERT INTO cliente (nombre, apellidos, ciudad)
VALUES ('Javier', 'Marulanda', 'Medellin');


-- ################################# FIN CLIENTE #####################

-- ################################# INICIO PRODUCTO #####################
INSERT INTO producto (nombre, tipoProducto)
VALUES ('PS5', 'electronico');

INSERT INTO producto (nombre, tipoProducto)
VALUES ('lovecraft', 'libro');

INSERT INTO producto (nombre, tipoProducto)
VALUES ('PS4', 'electronico');

INSERT INTO producto (nombre, tipoProducto)
VALUES ('lavadora', 'hogar');

INSERT INTO producto (nombre, tipoProducto)
VALUES ('carro', 'automovil');


-- ################################# FIN PRODCUTO #####################

-- ################################# INICIO SUCURSAL #####################
INSERT INTO sucursal(nombre, ciudad)
VALUES ('ciudad jardin', 'Cali');

INSERT INTO sucursal(nombre, ciudad)
VALUES ('las palmas', 'Medellin');

INSERT INTO sucursal(nombre, ciudad)
VALUES ('pueblo', 'Restrepo');


-- ################################# FIN SUCURSAL #####################

-- ################################# INICIO INSCRIPCION #####################
INSERT INTO inscripcion(idProducto, idCliente)
VALUES (1, 1);

INSERT INTO inscripcion(idProducto, idCliente)
VALUES (3, 1);

INSERT INTO inscripcion(idProducto, idCliente)
VALUES (2, 2);

INSERT INTO inscripcion(idProducto, idCliente)
VALUES (4, 2);

INSERT INTO inscripcion(idProducto, idCliente)
VALUES (1, 4);

INSERT INTO inscripcion(idProducto, idCliente)
VALUES (5, 5);


-- ################################# FIN INSCRIPCION #####################

-- ################################# INICIO DISPONIBILIDAD #####################
INSERT INTO disponibilidad(idSucursal, idProducto)
VALUES (1, 1);

INSERT INTO disponibilidad(idSucursal, idProducto)
VALUES (1, 3);

INSERT INTO disponibilidad(idSucursal, idProducto)
VALUES (2, 1);

INSERT INTO disponibilidad(idSucursal, idProducto)
VALUES (2, 2);

INSERT INTO disponibilidad(idSucursal, idProducto)
VALUES (2, 3);

INSERT INTO Disponibilidad(idSucursal, idProducto)
VALUES (2, 4);

INSERT INTO disponibilidad(idSucursal, idProducto)
VALUES (3, 4);

INSERT INTO disponibilidad(idSucursal, idProducto)
VALUES (3, 5);


-- ################################# FIN DISPONIBILIDAD #####################

-- ################################# INICIO VISITAN #####################
INSERT INTO visitan(idSucursal, idCliente, fechaVisita)
VALUES (1, 1,'2022-01-01');

INSERT INTO visitan(idSucursal, idCliente, fechaVisita)
VALUES (2, 1,'2022-01-02');

INSERT INTO visitan(idSucursal, idCliente, fechaVisita)
VALUES (2, 4,'2022-01-03');

INSERT INTO visitan(idSucursal, idCliente, fechaVisita)
VALUES (3, 5,'2022-01-03');


-- ################################# FIN VISITAN #####################