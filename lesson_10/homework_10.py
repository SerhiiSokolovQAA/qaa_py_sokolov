from math import sin, radians


class Romb:
    def __init__(self, a, alpha):
        if a > 0 and alpha > 0 and alpha < 180:
            self.a = a
            self.alpha = alpha
        else:
            raise ValueError("Wrong value!")

    def __str__(self):
        return f"Romb with a = {self.a}, alpha = {self.alpha}, beta = {self.beta}."

    def periment(self):
        return 4 * self.a

    def __add__(self, other):
        return ((self.a) ** 2) * sin(radians(self.alpha)) + ((other.a) ** 2) * sin(radians(other.alpha))


romb = Romb(10, 60) + Romb(20, 80)

print(romb)