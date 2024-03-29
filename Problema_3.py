import math

class Circulo:
    def __init__(self):
        while True:
            try:
                radio = float(input("Introduce el radio: "))
                self.radio = radio
                
                if self.radio < 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido")

    def area(self):
        area = math.pi * (self.radio ** 2)
        print(f"El área es: {area}")

if __name__ == '__main__':
    circu = Circulo()
    area = circu.area()