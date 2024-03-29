class Cuadrado:
    def __init__(self):
        while True:
            try:
                lado = float(input("Introduce el lado del cuadrado: "))
                if lado <= 0:
                    raise ValueError
                self.lado = lado
                break
            except ValueError:
                print("¡Valor inválido!")

    def area(self):
        area = self.lado * self.lado
        print(f"El área es: {area}")