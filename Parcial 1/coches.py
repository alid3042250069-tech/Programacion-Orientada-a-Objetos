"""  
 Programación Orientada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares


class coches:
    marca=""
    color="sin color"
    velocidad=0
    potencia=0
    aslentos=0

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

coche1=coches()
coche2=coches()
print(f"El color del coche 1 es:{coche1.color}")
coche1.color="Rojo y Blanco"
coche2.color="Blanco y Negro"
print(f"El color del coche 2 es:{coche2.color}")
print(f"La velocidad final del es de:{coche1.velocidad}")

for i in range(1,11):
    coche1.acelerar()


print(f"La velocidad final del es de:{coche1.velocidad}")
