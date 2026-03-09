import sys

class NumberSet:
    def __init__(self, limit=100):
        self.limit = limit
        self.numbers = list(range(1, limit + 1))

    def extract(self, number_to_remove):
        """
        Extrae un número del conjunto tras validar que sea correcto.
        """
        if not isinstance(number_to_remove, int):
            raise ValueError("El valor debe ser un número entero.")
        if number_to_remove < 1 or number_to_remove > self.limit:
            raise ValueError(f"El número debe estar entre 1 y {self.limit}.")
        if number_to_remove in self.numbers:
            self.numbers.remove(number_to_remove)
            print(f"Número {number_to_remove} extraído exitosamente.")
        else:
            print("El número ya no se encuentra en el conjunto.")

    def calculate_missing(self):
        """
        Calcula el número faltante usando la suma de Gauss.
        """
        expected_sum = (self.limit * (self.limit + 1)) // 2
        actual_sum = sum(self.numbers)
        return expected_sum - actual_sum

def main():
    if len(sys.argv) < 2:
        return
    try:
        target = int(sys.argv[1])
        game = NumberSet()
        game.extract(target)
        missing = game.calculate_missing()
        print(f"El número faltante es: {missing}")

    except ValueError as e:
        print(f"Error de validación: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()