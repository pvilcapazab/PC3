import random

def generar_numeros():
    numeros = []
    for i in range(20):
        numeros.append(random.randrange(1, 101))
    return numeros

def mostrar_aleatorios(numeros):
    print(f"Lista de números aleatorios:\n{numeros}")

def mostrar_ordenados(numeros):
    numeros.sort()
    print(f"Lista de números aleatorios ordenados:\n{numeros}")

if __name__ == '__main__':
    numeros = generar_numeros()
    mostrar_aleatorios(numeros)
    mostrar_ordenados(numeros)