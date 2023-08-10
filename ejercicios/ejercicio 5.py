import math


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        print(area)

    def calcular_perimetro(self):
        perimetro = (2 * math.pi * self.radio)
        print(perimetro)


if __name__ == "__main__":
    cir1 = Circulo(5, 3)
    cir1.calcular_area()
    cir1.calcular_perimetro()
