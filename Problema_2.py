def lista_calificaciones():
    while True:
        try:
            calificaciones = input('Ingrese las calificaciones separadas por comas: ')
            notas = calificaciones.split(',')
            notas = [int(n) for n in notas]
            return notas
        except:
            print("¡Error de tipeo o de formato!")

if __name__ == '__main__':
    print(f"Las notas son: {lista_calificaciones()}")