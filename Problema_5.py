class Alumno:
    def __init__(self, alumno, num_registro):
        self.alumno = alumno
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.alumno}\nNúmero de registro: {self.num_registro}\nEdad: {self.edad}\nNotas: {self.notas}")

    def setAge(self):
        while True:
            try:
                edad = int(input("Ingrese la edad del estudiante: "))

                if edad <= 0:
                    raise ValueError
                
                self.edad = edad
                break
            except:
                print("¡Error! La edad es un entero positivo")

    def setNota(self):
        while True:
            try:
                nota = float(input("Ingrese la nota del estudiante: "))

                if nota < 0:
                    raise ValueError
                
                self.notas.append(nota)
                break
            except:
                print("¡Error! La nota es un valor positivo o cero")

if __name__ == '__main__':
    estudiante = Alumno("Manuel", 123456)
    estudiante.display()

    edad = estudiante.setAge()
    
    nota = estudiante.setNota()
    nota = estudiante.setNota()
    
    estudiante.display()