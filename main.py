def saludar(nombre):
    print("Hola " + nombre)

#Esta division le faltaba tener la validacion por si el usuario intenta dividir por cero
def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

saludar("Mundo")
print(dividir(10, 0))
