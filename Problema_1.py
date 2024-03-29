def fraccion_porcentaje():
    while True:
        try:
            fraccion = input("Ingrese una fracción en el formato X/Y: ")
            x, y = fraccion.split("/")
            x, y = int(x), int(y)

            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError
            elif (x or y) < 0:
                raise ValueError

            porcentaje = round((x / y) * 100)

            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{porcentaje}%"
        except ValueError:
            print("¡Valor inválido!")
        except ZeroDivisionError:
            print("¡No se puede dividir entre cero!")

if __name__ == '__main__':
    print(fraccion_porcentaje())