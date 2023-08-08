class Punto:
    def __init__(self, eje_x: int, eje_y: int, otro_ejex, otro_ejey):
        self.eje_x: int = eje_x
        self.eje_y: int = eje_y
        self.otro_ejex = otro_ejex
        self.otro_ejey = otro_ejey

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
    p1 = Punto(-4, -3, 2, 5)

    p1.mostrar()
    p1.mover(8, 11)
    p1.calcular_distancia()