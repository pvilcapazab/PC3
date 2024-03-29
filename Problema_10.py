import Problema_3
import Problema_4
import Area_Cuadrado

while True:
    print("-" * 60)
    opcion = input("¿Qué función desea realizar?\n1.Calcular el area de un ciculo\n2.Calcular el area de un rectángulo\n3.Calcular el area de un cuadrado\n4.Salir\n")
    if opcion == "1":
        area_circulo = Problema_3.Circulo()
        area_circulo.area()
    elif opcion == "2":
        area_rectangulo = Problema_4.Rectangulo()
        area_rectangulo.area()
    elif opcion == "3":
        area_cua = Area_Cuadrado.Cuadrado()
        area_cua.area()
    elif opcion == "4":
        break
    else:
        print("Opción no válida")