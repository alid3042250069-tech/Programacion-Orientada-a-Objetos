from tkinter import Label, Button, Entry, Tk, messagebox
from estudiantesBD import EstudiantesBD

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Estudiantes")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0, 0)
        self.main()

    # Vistas y Limpieza de Pantalla
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n\t...::: M E N U   P R I N C I P A L :::...\n\t").pack(pady=20)
        Button(self.ventana, text="\n\t 1.- Estudiantes\n\t", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana, text="\n\t 2.- Salir \n\t", command=self.ventana.quit).pack(pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n\t...::: M E N U   E S T U D I A N T E S :::...\n\t").pack(pady=20)
        Button(self.ventana, text="\n\t 1.- Agregar\n\t", command=self.insertar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 2.- Borrar \n\t", command=self.eliminar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 3.- Modificar\n\t", command=self.modificar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 4.- Consultar \n\t", command=self.consultar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 5.- Buscar\n\t", command=self.buscar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 6.- Salir \n\t", command=self.main).pack(pady=5)
             
    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="... Ingresar los datos del estudiante ...").pack(pady=10)
        
        Label(self.ventana, text="Nombre").pack(pady=5)
        self.nombre = Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)
        
        Label(self.ventana, text="Nota").pack(pady=5)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady=5)
        
        Button(self.ventana, text="Guardar", command=self.insertar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="... Ingresar el ID del Estudiante a borrar ...").pack(pady=10)
        
        Label(self.ventana, text="ID del Estudiante").pack(pady=5)
        self.id_estudiante = Entry(self.ventana)
        self.id_estudiante.focus()
        self.id_estudiante.pack(pady=5)

        Button(self.ventana, text="Borrar", command=self.eliminar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="... Modificar datos del estudiante ...").pack(pady=10)
        
        Label(self.ventana, text="ID del estudiante a modificar").pack(pady=5)
        self.id_estudiante = Entry(self.ventana)
        self.id_estudiante.focus()
        self.id_estudiante.pack(pady=5)

        Label(self.ventana, text="Nuevo Nombre").pack(pady=5)
        self.nombre = Entry(self.ventana)
        self.nombre.pack(pady=5)
        
        Label(self.ventana, text="Nueva Nota").pack(pady=5)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady=5)
        
        Button(self.ventana, text="Modificar", command=self.modificar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="... Consultar Estudiantes ...").pack(pady=10)
        filas = ""
        filas = self.consulta_controller(filas)
        Label(self.ventana, text=f"{filas}", justify="left").pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def buscar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="... Buscar Estudiante por ID ...").pack(pady=10)
        
        Label(self.ventana, text="ID del Estudiante").pack(pady=5)
        self.id_buscar = Entry(self.ventana)
        self.id_buscar.focus()
        self.id_buscar.pack(pady=5)

        Button(self.ventana, text="Buscar", command=self.buscar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    # Controladores
    def respuesta_sql(self, respuesta):
        if respuesta:   
            messagebox.showinfo(title="Exitoso", message="... ¡Acción Realizada con Éxito! ...")
        else:
            messagebox.showerror(title="Error", message="... Opción inválida o error en la operación ...")   

    def insertar_controller(self):
        nombre = self.nombre.get().upper().strip()
        nota = self.nota.get().strip()
        estudiante1 = EstudiantesBD(nombre, nota)
        respuesta = estudiante1.insertar()
        self.respuesta_sql(respuesta)

    def eliminar_controller(self):
        id_val = self.id_estudiante.get().strip()
        estudiante1 = EstudiantesBD('', 0)
        respuesta = estudiante1.eliminar(id_val)
        self.respuesta_sql(respuesta)

    def modificar_controller(self):
        id_val = self.id_estudiante.get().strip()
        nombre = self.nombre.get().upper().strip()
        nota = self.nota.get().strip()
        estudiante1 = EstudiantesBD(nombre, nota)
        respuesta = estudiante1.modificar(id_val)
        self.respuesta_sql(respuesta)

    def consulta_controller(self, filas):
        estudiante1 = EstudiantesBD('', 0)
        registros = estudiante1.consultar()
        if registros and len(registros) > 0:
            num_estudiante = 1
            for fila in registros:
                filas += f"Estudiante # {num_estudiante}\t ID: {fila[0]}\t Nombre: {fila[1]}\t Nota: {fila[2]}\n"
                num_estudiante += 1
        else:
            filas = "... No hay registros de estudiantes ..."
        return filas

    def buscar_controller(self):
        id_val = self.id_buscar.get().strip()
        estudiante1 = EstudiantesBD('', 0)
        registros = estudiante1.buscar(id_val)
        
        self.borrarPantalla()
        Label(self.ventana, text="... Resultado de la Búsqueda ...").pack(pady=10)
        
        if registros and len(registros) > 0:
            resultado = ""
            for fila in registros:
                resultado += f"ID: {fila[0]}\nNombre: {fila[1]}\nNota: {fila[2]}\n"
            Label(self.ventana, text=resultado, justify="left").pack(pady=10)
        else:
            Label(self.ventana, text="... No se encontró ningún estudiante con ese ID ...").pack(pady=10)
            
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()


    