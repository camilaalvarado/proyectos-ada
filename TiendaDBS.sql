CREATE TABLE  categoria (
    ID INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT
  );


CREATE TABLE producto (
    ID INTEGER PRIMARY KEY,
    nombre TEXT,
    marca TEXT,
    categoria_id TEXT,
    precio_unitario REAL
);

 CREATE TABLE sucursal (
    ID PRIMARY KEY,
    nombre TEXT,
    direccion TEXT
);

 CREATE TABLE cliente (
    ID PRIMARY KEY,
    nombre TEXT,
    telefono INTEGER
);

 CREATE TABLE orden (
    ID PRIMARY KEY,
    cliente_id INTEGER,
    sucursal_id INTEGER ,
    fecha INTEGER ,
    total REAL
);

CREATE TABLE  stock (
    ID PRIMARY KEY,
    sucursal_id int UNIQUE NOT NULL,
    producto_id int UNIQUE NOT NULL,
    cantidad INTEGER
    
);

 CREATE TABLE item (
    ID PRIMARY KEY,
    orden_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    monto_venta REAL
);

INSERT INTO categoria  (ID, nombre)
VALUES ( 24, "Audio y video");

INSERT INTO producto (ID, nombre, marca, categoria_id, precio_unitario)
VALUES (105746, "Televisor 55 pulgadas", "Samsung", 24, "1,699,000");

INSERT INTO sucursal (ID, nombre, direccion)
VALUES (9, "Flamingo Pereira", "CR 6 20-76 Pereira");

INSERT INTO  cliente (ID, nombre, telefono)
VALUES (102345, "Daniel Perez", 3185095077);

INSERT INTO orden (ID, cliente_id, sucursal_id, fecha, total)
VALUES (10402, 102345, 9, 28/09/2023, "1,699,000");

INSERT INTO  stock  (ID, sucursal_id, producto_id, cantidad)
VALUES (1025, 9, 105746, 100);

INSERT INTO item (ID, orden_id, producto_id, cantidad, monto_venta)
VALUES (1002, 10402, 105746, 1, "1,699,000");