class Punto:
    def __init__(self, eje_x: int, eje_y: int):
        self.eje_x: int = eje_x
        self.eje_y: int = eje_y

    def mostrar(self):
        print(self.eje_x, self.eje_y)

    def mover(self, nuevo_eje_x, nuevo_eje_y):
        self.eje_x = nuevo_eje_x
        self.eje_y = nuevo_eje_y
        print(nuevo_eje_x, nuevo_eje_y)

    def calcular_distancia(self):
        pass


if __name__ == "__main__":
    p1 = Punto(5, 3)
    p1.mostrar()
    p1.mover(8, 11)