# Modulo Time
import time

# clase: Representa los objetos iterador que vamos a instancear.
class FiboIter():

    # Medodos necesarios de la clase.
    def __iter__(self):
        # Numeros iniciales necesarios para la sucesion.
        self.n1 = 0
        self.n2 = 1

        # Contador para ver cuantas vueltas se realizan.
        self.counter = 0

        # Retornamos al objeto
        return self

    def __next__(self): # Todos los metodos de una clase necesitan el parametro "self" para poder existir.
        if self.counter == 0: # Primera vuelta.
            self.counter += 1
            return self.n1
        elif self.counter == 1: # Segunda vuelta.
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux

            self.n1, self.n2 = self.n2, self.aux # 'n1' ahora tiene el valor de 'n2', y 'n2' el valor de 'aux'.
            self.counter += 1
            return self.aux # aux representa el ultimo valor de la secuencia.

if __name__ == '__main__':
    # Instanciamos la clase "FiboIter".
    fibonnaci = FiboIter()

    # Recorremos el iterador.
    for element in fibonnaci:
        print(element)

        # El programa se pausara un segundo durante cada vuelta del ciclo.
        time.sleep(1)



