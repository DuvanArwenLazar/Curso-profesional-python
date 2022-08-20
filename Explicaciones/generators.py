# Explicacion: Mejorando la secuencia de fibonnaci.
import time

def fibo_gen():
    # Usamos variables en lugar de atributos.
    n1 = 0
    n2 = 1 
    counter = 0 

    while True:
        # Vuelta numero uno.
        if counter == 0:
            counter += 1
            yield n1

        # Vuelta numero dos.
        elif counter == 1: 
            counter += 1
            yield n2
        else:
            aux = n1 + n2

            # Intercambiamos los valores.
            n1, n2 = n2, aux 
            counter += 1
            yield aux

if __name__ == '__main__':
    # Guardamos el resultado de aplicar la funcion y la recorremos.
    fibonnaci = fibo_gen() 
    for element in fibonnaci:
        print(element)

        time.sleep(1)

