def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

# Para arreglarlo podemos o eliminar la operacion o simplemente cambiarla para que no devuelva siempre el mismo valor 
def operacion(x):
    if x > 0:
        return True
    else:
        return False #algo asi ahora tendria cierta utilidad.


