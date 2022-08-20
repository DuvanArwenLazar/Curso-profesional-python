# Explicacion: Eliminar repetidos en una lista -> [1, 1, 2, 2, 4] -> [1, 2, 4]

# Funcion. Como parametro tiene la lista que vamos a eliminar.
def remove_duplicates(some_list):
    # Lista que tendra los elementos sin repetir.
    without_list = []

    # Recorremos la lista
    for element in some_list:
        # Si el elemento NO esta en la 'without_list', agregamos el elemento.
        if element not in without_list:
            without_list.append(element)

    return without_list

def run():
    random_list = [1, 1, 2, 2, 4] # Salida esperada: [1, 2, 4]

    # Llamamos a la funcion.
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()

