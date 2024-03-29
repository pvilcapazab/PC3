def suma():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 + num2
            return resultado
        except ValueError:
            print("Tipo de dato no válido")

def resta():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 - num2
            return resultado
        except ValueError:
            print("Tipo de dato no válido")

def producto():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 * num2
            return resultado
        except ValueError:
            print("Tipo de dato no válido")    

def division():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 / num2
            return resultado
        except ValueError:
            print("Tipo de dato no válido")
        except ZeroDivisionError:
            print("No es posible dividir entre cero")

if __name__ == '__main__':
    print("Sumando dos numeros:")
    print(f"La suma es: {suma()}")

    print("Restando dos numeros:")
    print(f"La resta es: {resta()}")

    print("Multiplicando dos numeros:")
    print(f"El producto es: {producto()}")
    
    print("Dividiendo dos numeros:")
    print(f"La división es: {division()}")