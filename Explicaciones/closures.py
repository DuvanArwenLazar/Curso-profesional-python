# Explicacion: Programando closures.

# Hola 3 -> HolaHolaHola. 
# Duvan 2 -> DuvanDuvan.

# Funcion: Contiene la nested function (funcion aninada). Sera un repetidor de "n" veces.
def envolvente(n):
    def frase(cadena):
        # Afirmamos que cadena sera un str, en caso de que no surgira un error.
        assert type(cadena) == str, "NO se permiten numeros." 

        # Trabajara con un valor de un scope superior (n)
        return cadena * n 
    return frase

def run():
    repeat_5 = envolvente(5)
    ''' Se ejecuta la funcion envolvente con parametro 5, luego crea una funcion aninada que afirma que la cadena debe
        ser una cadena y, en caso contrario, generara un error. Luego, concatenara la cadena con ella misma n veces. '''

    # Se pintara Hola 5 veces.
    print(repeat_5("Hola"))
    
if __name__ == '__main__':
    run()