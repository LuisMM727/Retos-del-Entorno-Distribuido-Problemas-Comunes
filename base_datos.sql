CREATE DATABASE IF NOT EXISTS gestion_gastos_db
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE gestion_gastos_db;


CREATE TABLE IF NOT EXISTS gastos_gasto (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    monto DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    descripcion TEXT NULL,
    fecha DATE NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
