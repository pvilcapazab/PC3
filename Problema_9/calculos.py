import operaciones

while True:
    print("-"*60)
    opcion = input("¿Qué función desea realizar?\n1.Suma\n2.Resta\n3.Producto\n4.División\n5.Salir\n")
    
    if opcion == "1":
        print(f"La suma es: {operaciones.suma()}")
    elif opcion == "2":
        print(f"La resta es; {operaciones.resta()}")
    elif opcion == "3":
        print(f"El producto es: {operaciones.producto()}")
    elif opcion == "4":
        print(f"La división es: {operaciones.division()}")
    elif opcion == "5":
        break
    else:
        print("Opción no válida")