# Programa: Verificar si un numero es primo o no.
# Funcion. Utilizaremos python como lenguaje de tipado "estatico".
# from numbers import Integral

# a = 10
# b = 5

# hola = divmod(a, b)
# print(hola)

def numeroPrimo(n: int) -> int:
    i: int = 0
    contador: int = 0

    while i <= n:
        valor: int = divmod(n, i)
        if(valor[1] == 0): 
            contador += 1
            '''Si la division del numero (que digita el usuario), por el iterador es igual a 0, entonces es un 
                divisor del numero, por lo que se agrega al contador. '''
    i+=1

    if(contador > 2):
        print(f"-> El numero {n} es primo.")
    else:
        print(f"El numero {n} es compuesto")

if __name__ == '__main__':
    n: int = input("-> Bienvenido \n -> Digite un numero: ")
    
    # Convertimos a entero la variable 'n'.
    # int(n)

    # Llamamos la funcion.
    numeroPrimo(n)


