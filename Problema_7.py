import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def constructor(self):
        self.punto = (self.x, self.y)

    def __str__(self):
        return f"(X,Y) = ({self.x},{self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y != 0:
            print(f"({self.x},{self.y}) Se encuentra sobre el eje Y")
        elif self.x != 0 and self.y == 0:
            print(f"({self.x},{self.y}) Se encuentra sobre el eje X")
        elif self.x == 0 and self.y == 0:
            print(f"({self.x},{self.y}) Se encuentra sobre el origen")
        elif self.x > 0 and self.y > 0:
            print(f"({self.x},{self.y}) Se encuentra sobre el primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print(f"({self.x},{self.y}) Se encuentra sobre el segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print(f"({self.x},{self.y}) Se encuentra sobre el tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print(f"({self.x},{self.y}) Se encuentra sobre el cuarto cuadrante")

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
    
    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)

class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def constructor(self):
        if self.punto_inicial is None:
            self.punto_inicial = Punto(0, 0)
        if self.punto_final is None:
            self.punto_final = Punto(0, 0)
        self.vector = (self.punto_final.x - self.punto_inicial.x, self.punto_final.y - self.punto_inicial.y)
    
    def base(self):
        print(f"La base del rectangulo mide: {abs(self.vector[0])}")

    def altura(self):
        print(f"La altura del rectangulo mide: {abs(self.vector[1])}")

    def area(self):
        print(f"El area del rectangulo es: {self.vector[0] * self.vector[1]}")

if __name__ == '__main__':
    #Ejemplos dados
    A = Punto(2, 2)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    print(f"Punto A: {A}")
    print(f"Punto B: {B}")
    print(f"Punto C: {C}")
    print(f"Punto D: {D}")

    A.cuadrante()
    C.cuadrante()
    D.cuadrante()

    print(f"El vector AB es: {A.vector(B)}")
    print(f"El vector BA es: {B.vector(A)}")

    print(f"La distancia del punto A hacia el punto B es: {A.distancia(B)}")
    print(f"La distancia del punto B hacia el punto A es: {B.distancia(A)}")

    puntos = (A, B, C)
    distancia = [p.distancia(D) for p in puntos]
    print(f"La distancia máxima al origen es: {max(distancia)} y le pertenece a {puntos[distancia.index(max(distancia))]}")

    rectangulo_AB = Rectangulo(A, B)
    rectangulo_AB.constructor()

    rectangulo_AB.base()
    rectangulo_AB.altura()
    rectangulo_AB.area()