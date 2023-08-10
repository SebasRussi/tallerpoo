class Carta:
    DIAMANTE = "\u2663"
    CORAZON = "\u2764"
    TREBOL = "\u2666"
    ESPADA = "\u2660"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def mostrar(self):
        print(f"{self.valor}{self.pinta}")


if __name__ == "__main__":
    carta1 = Carta("A", Carta.TREBOL)
    carta1.mostrar()
