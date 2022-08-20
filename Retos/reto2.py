# Ejercicio: Hacer un programa que realize divisiones utilizando closures.

# Funcion.
def make_division_by(n):
    def nested_function(x):
        # Al igual que en 'closures.py', tambien voy a generar un error en caso de que el formato no sea el deseado.
        assert type(x) == int, "NO se permiten letras." 

        # Retornamos la division entre x y n (Quien es un valor de "Scope superior")
        return x / n
    
    return nested_function

# Pruebas.
division_by_3 = make_division_by(3)
print(division_by_3(18)) # La salida es esperada es 6.

division_by_5 = make_division_by(5)
print(division_by_5(100)) # La salida es esperada es 20.

division_by_18 = make_division_by(18)
print(division_by_18(54)) # La salida es esperada es 3.