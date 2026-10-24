from estudiantes.estudiantesBD import EstudiantesBD

class App:
    def __init__(self):
        self.main()
        

    def esperarTecla(self):
        input("... ¡Oprima cualquier tecla para continuar! ...")

    def borrarPantalla(self):
        print("\033c")
        

    def main(self):
        opcion = True
        while opcion:
           self.borrarPantalla()
           print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
           opcion = input("\n\t 1.- Estudiante \n\t 2.- Salir \n\t  \n \t\tElige una Opcion: ").strip().lower()
           match opcion:
                  case '1':
                     self.borrarPantalla()
                     self.menu_estudiante()
                  case '2':
                     self.borrarPantalla()
                     print("\n\t ...Salir del Sistema...")
                     opcion = False
                  case _:
                     input("\n\t ...Opcion Invalida, vuelve a intentarlo por favor ...")

    def menu_estudiante(self):
       opcion = True
       while opcion:
          self.borrarPantalla()
          sub_opcion = self.menuAcciones("Estudiante")
          match sub_opcion:
             case '1':
                nombre, nota = self.datos_estudiante("Coche")
                estudiante1 = EstudiantesBD(nombre, nota)
                respuesta = estudiante1.insertar()
                self.respuesta_sql(respuesta)
                self.esperarTecla()

             case '2':
                self.borrarPantalla()
                estudiante1 = EstudiantesBD('',0,)
                id_eliminar = input("Ingresa el id a eliminar: ").strip()
                respuesta = estudiante1.eliminar(id_eliminar)
                self.respuesta_sql(respuesta)
                self.esperarTecla()
        
             case '3':     
                self.borrarPantalla()
                id_modificar = input("Ingresa el id a modificar: ").strip()
                nombre, nota = self.datos_estudiante("Modificar Coche")
                coche1 = EstudiantesBD(nombre, nota)
                respuesta = coche1.modificar(id_modificar)
                self.respuesta_sql(respuesta)
                self.esperarTecla()
      
             case '4':
                self.borrarPantalla()
                coche1 = EstudiantesBD('', 0,)
                registros = coche1.consultar()
                if len(registros) > 0:
                    num_estudiante = 1
                    for fila in registros:
                        print(f"Estudiante # {num_estudiante}\n\t ID: {fila[0]}\n\t Nombre: {fila[1]}\n\t Nota: {fila[2]}\n")
                        num_estudiante += 1
                else:
                    print("\n\t... No hay registros de coches ...")
                self.esperarTecla()

             case '5':
                self.borrarPantalla()
                estudiante1 = EstudiantesBD('',0)
                id_buscar = input("Ingresa el ID del coche a buscar: ").strip()
                registros = estudiante1.buscar(id_buscar)
                if len(registros) > 0:
                    for fila in registros:
                        print(f"\n\t ID: {fila[0]}\n\t Nombre: {fila[1]}\n\t Nota: {fila[2]}\n")
                else:
                    print("\n\t... No se encontro ningun coche con ese ID ...")
                self.esperarTecla()

             case '6':
                opcion = False

             case _:
                input("\n\t ...Opcion Invalida, vuelve a intentarlo por favor ...")

    def respuesta_sql(self, respuesta):
       if respuesta:   
           input("\n\t...¡Accion Realizada con Exito!...")
       else:
           input("\n\t.... ¡Opcion invalida o error en la operacion, oprima cualquier tecla para continuar !....")       

    def menuAcciones(self, tipo):
        print(f"\n\t\t\t...::: M E N U   de  {tipo} :::... \n")
        opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Consultar \n\t 5.- Buscar\n\t 6.- Salir \n \t\tElige una Opcion: ").strip().lower()
        return opcion

    def borrarPantalla(self):
        print("\033c")


    def respuesta_sql(self,respuesta):
       if respuesta:   
           input("\n\t...¡Accion Realizada con Exito!...")
       else:
           input("\n\t .... ¡Opcion invalidad oprima cualquier tecla para continuar !....")       


    def datos_estudiante(self,tipo):
      self.borrarPantalla()
      print(f"Ingresa el {tipo} de dato")
      nombre=input("Dame el nombre:").upper().strip()
      nota=input("Dame la nota:")

      return nombre , nota
    
if __name__=="__main__":
    app=App()

