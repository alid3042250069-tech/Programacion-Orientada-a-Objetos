import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='bd_estudiante',
        )
        return conexion
    except Exception as e:
        print("....Por el momento no es posible conectarse con la Base de Datos ¡inténtelo más tarde!")
        return None