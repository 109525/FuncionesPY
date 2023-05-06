#Funcion que compare dos numeros y muestre cual de ellos es el mayor, además, debe verificar que los datos sean enteros o decimales.
def ComparacioNumeros(numero1, numero2):
    if isinstance(numero1, int):
        print(f"El {numero1} es entero")
    elif isinstance(numero1, float):
        print(f"{numero1} es decimal")
    else:
        print("Esto no es decimal ni entero")
    if isinstance(numero2, int):
        print(f"El {numero2} es entero")
    elif isinstance(numero2, float):
        print(f"{numero2} es decimal")
    else:
        print("Esto no es decimal ni entero")
    if numero1 >= numero2:
        print(f"{numero1} mayor que {numero2}")
    else:
        print(f"{numero2} mayor que {numero1}")
    
ComparacioNumeros(35, 24.8)