# Ejercicio: Usa tu creatividad para poner en practica los decoradores.

# Funcion
def decoradora(funct):
    # envoltura
    def wrap():
        print("-" * 30) # Pinrtamos en pantalla el simbolo "-" 30 veces.
        funct()
        print("-" * 30)
    
    return wrap

# Funcion a decorar
@decoradora
def random_func():
    print("Hola Mundo")

# Llamamos a la funcion. 
random_func()
'''
Resultado esperado:   ------------------------------ 
                      Hola Mundo
                      ------------------------------
'''