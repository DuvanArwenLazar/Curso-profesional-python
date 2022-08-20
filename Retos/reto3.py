# Explicacion: Realizar la secuencia de fibonnaci con un limite y usando generators.
import time

# Le pedimos el maximo al usuario.
num_max = int(input("-> Digite el numero maximo de la secuencia: "))

# Ahora la funcion tiene un parametro, que se utilizara como limite para la funcion.
def fibo_gen(num_max):
    n1 = 0
    n2 = 1 
    counter = 0 

    while True:
        if counter == 0:
            counter += 1
            yield n1

        elif counter == 1: 
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux 
            counter += 1

            if(aux <= num_max):
                yield aux
            else:
                break
            
if __name__ == '__main__':
    # Guardamos el resultado de aplicar la funcion y la recorremos.
    fibonnaci = fibo_gen(num_max) 
    for element in fibonnaci:
        print(element)

        time.sleep(1)