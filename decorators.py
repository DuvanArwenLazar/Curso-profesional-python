# Explicacion: Programando decoradores. Este decorador determina cuanto tarda en ejecutarse una funcion.

# Importamos este modulo para trabajar con fechas.
from datetime import datetime

# Funcion.
def execution_time(func):
    # Envoltura.
    def wrapper():
        # Vamos a recopilar la fecha de inicio y final de la ejecucion de la funcion.
        initial_time = datetime.now()
        func()
        final_time = datetime.now() 

        # Ahora restamos ambas fechas para saber la diferencia (tiempo de ejecucion)
        time_elapsed = final_time - initial_time
        
        # Mostramos ese resultado.
        print("-> Pasaron " + str(time_elapsed.total_seconds()) + " segundos.")
    
    return wrapper

# Con esto decoramos la funcion "random_func"
@execution_time
def random_func(): # Funcion a teestear cuanto tiempo tarda en ejecutarse. Esta funcion solo da 1000 vueltas al bucle.
    for _ in range(1, 10000):
        pass

# Ejecucion despues de decorarla.
random_func()