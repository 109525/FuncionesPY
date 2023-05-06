#FUNCIONES: Ahorran lineas de codigo, para reutilizar codigo, dividir el programa en pequeñas tareas. 
#DECLARAR UNA FUNCION: 
"""def NombreFuncion(parametro1, parametro2...): 
Conjunto de instrucciones
NombreFuncion(Arguento1, Argumento2...)
"""
#Funcion sin parametros 
def DerechosHumanos():
    print("Derecho a la vida\nDerecho a la salud\nDerecho a la educación\nDerecho a la lire expresion\nDerecho a la libertad\nDerecho al libre desarrollo de la personalidad")
    DerechosHumanos()
    
def MayoresDeEdad():
    print("Derecho a morir dignamente\nDerecho al trabajo\nDerecho a una vejez digna\nDerecho a votar")
MayoresDeEdad()

#Funcion con parametros: 
#Declarar una funcion que muestre los derechos humanos y drechos mayores de edad, si la edad es mayor o igual que 1, de lo contrario que solo muestre los derechos humanos.

def Derechos(Nombre, edad = 23):
    print(f"{Nombre} tus derechos son: ")
    if edad >= 18: 
        DerechosHumanos()
        MayoresDeEdad()
    else:
        DerechosHumanos()
#edad = int(input("Ingrese la edad: "))
Derechos("Karina", 9)

#funcion division: divisor 0  debe arrojar un mensaje de error, de lo contrario muestre el resultado
Divisor = 3
def Division(Dividendo, Divisor):
    if Divisor == 0:
        print("No existe la division por cero")
    else:
        print(f"El cociente es, {Dividendo // Divisor}")
Division(20, 5)
print(Divisor)


    