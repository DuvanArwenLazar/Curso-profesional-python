# Ejercicio: Realizar un programa que elimine los elementos 

# Funcion.
def remove_d(lista_random):
    return list(set(lista_random))

def run():
    lista_random = [1, 2, 2, 3, 4, 4] # Salida esperada: [1, 2, 3, 4]
    print(remove_d(lista_random))

if __name__ == '__main__':
    run()