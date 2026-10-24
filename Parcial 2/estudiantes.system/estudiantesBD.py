from conexionBD import conectar

class EstudiantesBD:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNota(self):
        return self._nota

    def setNota(self, nota):
        self._nota = nota

    def insertar(self):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "INSERT INTO estudiante (nombre, nota) VALUES (%s, %s)"
                valores = (self.getNombre(), self.getNota())
                cursor.execute(sql, valores)
                conexionBD.commit()
                cursor.close()
                conexionBD.close()
                return True
            else:
                return False
        except Exception as e:
            return False
   
    def eliminar(self, id_estudiante):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "DELETE FROM estudiante WHERE id = %s"
                cursor.execute(sql, (id_estudiante,))
                conexionBD.commit()
                cursor.close()
                conexionBD.close()
                return True
            else:
                return False
        except Exception as e:
            return False

    @property
    def modificar(self, id_estudiante):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "UPDATE estudiante SET nombre = %s, nota = %s WHERE id = %s"
                valores = (self.getNombre(), self.getNota(), id_estudiante)
                cursor.execute(sql, valores)
                conexionBD.commit()
                cursor.close()
                conexionBD.close()
                return True
            else:
                return False
        except Exception as e:
            return False

    @property
    def consultar(self):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                cursor.execute("SELECT * FROM estudiante")
                registros = cursor.fetchall()
                cursor.close()
                conexionBD.close()
                return registros
            else:
                return []
        except Exception as e:
            return []

    @property
    def buscar(self, id_estudiante):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "SELECT * FROM estudiante WHERE id = %s"
                cursor.execute(sql, (id_estudiante,))
                registros = cursor.fetchall()
                cursor.close()
                conexionBD.close()
                return registros
            else:
                return []
        except Exception as e:
            return []