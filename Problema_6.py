class Producto:
    def __init__(self, producto, codigo, anio, precio):
        self.producto = producto
        self.codigo = codigo
        self.anio = anio
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.producto}\nCódigo: {self.codigo}\nPrecio: {self.precio}\nAño: {self.anio}"
    
class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def productos_filtrados_anio(self, anio):
        filtrado = []

        for producto in self.productos:
            if producto.anio == anio:
                filtrado.append(producto)
        
        return filtrado
    
    def mostrar(self):
        for producto in self.productos:
            print(producto)
    
if __name__ == '__main__':
    cata_logo = Catalogo()

    producto1 = Producto("Amortiguadores", anio=2019, precio=410, codigo=123456)
    producto2 = Producto("Bujía", anio=2023, precio=60, codigo=456789)
    producto3 = Producto("Radiador", anio=2023, precio=300, codigo=789101)

    cata_logo.agregar(producto1)
    cata_logo.agregar(producto2)
    cata_logo.agregar(producto3)

    cata_logo.mostrar()

    #Filtramos la fecha 2023
    print("-" * 50)
    print("Productos del año 2023:\n")
    for producto in cata_logo.productos_filtrados_anio(2023):
        print(f"{producto}\n")