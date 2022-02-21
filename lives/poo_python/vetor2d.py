class Vetor2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vetor2D(x, y)

    def __sub__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vetor2D(x, y)

    def __mul__(self, valor):
        x = self.x * valor
        y = self.y * valor
        return Vetor2D(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vetor2D({self.x}, {self.y})"

    def __bool__(self):
        return self.x != 0 or self.y != 0
    