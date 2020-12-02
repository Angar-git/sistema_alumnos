DROP DATABASE IF EXISTS alumnos;
CREATE DATABASE ALUMNOS;

USE ALUMNOS;

DROP TABLE IF EXISTS tAlumnos;
CREATE TABLE tAlumnos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    boleta INT UNIQUE ,
    nombre VARCHAR(255),
    aPaterno VARCHAR(255),
    aMaterno VARCHAR(255),
    CURP VARCHAR(255) UNIQUE ,
    activo TINYINT(1)
);


SELECT * FROM tAlumnos


DROP PROCEDURE IF EXISTS sp_altaAlumno;
DELIMITER **
CREATE PROCEDURE sp_altaAlumno(xBol INT, xNom VARCHAR(255), xAPat VARCHAR(255), xAMat VARCHAR(255), xCurp VARCHAR(255))
BEGIN 
    DECLARE msj VARCHAR(255);
    DECLARE existencia int;
        SET existencia = (SELECT COUNT(*) FROM tAlumnos where boleta = xBol);
        IF(existencia = 0) THEN
            INSERT INTO tAlumnos(boleta, nombre, aPaterno, aMaterno, CURP, activo) 
            VALUES (xBol, xNom, xAPat, xAMat, xCurp, 1);
            SET msj = "AGREGADO";
        ELSE
            SET msj = "ERROR";
        END IF;
    SELECT msj as RESULTADO;
end; **
DELIMITER ;


CALL sp_altaAlumno(2015090116, "Sandy", "Cespedes", "Guerrero", "CURPSANDY")

