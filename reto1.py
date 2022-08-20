# Programa: Verificar si un numero es primo o no. Utilizaremos python como lenguaje de tipado "estatico".
n = int(input("-> Bienvenido \n -> Digite un numero: "))

# Funcion: 
def numeroPrimo(n: int) -> int:
    i: int = 0
    contador: int = 0

    while i <= n:
        # valor: int = divmod(n, i)
        if(n%2== 0): 
            contador += 1
            '''Si la division del numero (que digita el usuario), por el iterador es igual a 0, entonces es un 
                divisor del numero, por lo que se agrega al contador. '''

        i+=1

    if(n == 0 or n == 1):
        print(f"-> El numero NO es primo ni compuesto")
        
    else:
        if(n == 2):
            print(f"-> El numero {n} es primo.")
        else:
            if(contador > 2):
                print(f"-> El numero {n} es compuesto.")
            else:
                print(f"El numero {n} es primo.")

if __name__ == '__main__':
    numeroPrimo(n)


