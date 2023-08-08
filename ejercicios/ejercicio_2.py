class Punto:
    def __init__(self):
        self.eje_x: int = 8
        self.eje_y: int = -6
        self.otro_ejex = 5
        self.otro_ejey = -5

    def mostrar(self):
        print(self.eje_x, self.eje_y)

    def mover(self, nuevo_eje_x, nuevo_eje_y):
        self.eje_x = nuevo_eje_x
        self.eje_y = nuevo_eje_y
        print(nuevo_eje_x, nuevo_eje_y)

    def calcular_distancia(self):
        distancia = (((self.otro_ejex - self.eje_x) ** 2) + ((self.otro_ejey - self.eje_y) ** 2)) ** 0.5
        print(distancia)


if __name__ == "__main__":
    p1 = Punto()
    p1.mostrar()
    p1.mover(1, -2)
    p1.calcular_distancia()