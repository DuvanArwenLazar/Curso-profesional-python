# Explicacion: Verificar si una cadena de caracteres es palindroma o no.

# Funcion que hace la verificacion.
def palindrome(cadena: str) -> bool:
    # Reemplazamos los espacios vacios (" "), por una cadena vacia (""). Ademas, convertimos a minusculas.
    cadena = cadena.replace(" ", "").lower()

    # Le damos vuelva a un iterable (En este caso, la cadena) y lo comparamos con la cadena inicial. Esto devolvera un bool.
    return cadena == cadena[::-1]

# Funcion que correra el codigo principal
def programa():
    print(palindrome("ana"))

if __name__ == '__main__':
    programa()