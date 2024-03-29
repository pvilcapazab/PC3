class Rectangulo:
    def __init__(self):
        while True:
            try:
                largo = float(input("Introduce el largo del rectángulo: "))
                ancho = float(input("Introduce el ancho del rectángulo: "))
                self.largo, self.ancho = largo, ancho
                if (largo or ancho) < 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido")
    def area(self):
            area = self.largo * self.ancho
            print(f"El área es: {area}")

if __name__ == '__main__':
    recta = Rectangulo()
    recta.area()