"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class coches:
    def __init__(self,color,marca,velocidad):
        pass
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad

    def acelerar(self):
     self.__velocidad+=1

    def frenar(self):
     self.__velocidad-=1

    def tocar_claxon(self):
     print("bip bip bip")


#Instanciar o crear objetos de la clase Coches

coche1=coches("blanco","UVW",220)
coche2=coches("azul","nissan",180)

#print(f"El color del coche uno es:{coche1.__color}")
#No se pueden utlizar los atributos por que son privados 
coche1.tocar_claxon()

print(f"El claxon del coche 1 hace:{
  coche1.tocar_claxon()}")

print(f"El claxon del coche 2 hace:{
  coche2.tocar_claxon()}")

coche1.acelerar()
print(f"La velocidad del coche 1 es de:{coche1.__velocidad()}")





