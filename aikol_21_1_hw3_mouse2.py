import math


class Fraction:
    def init(self, numerator, denumerator):
        self.numerator = int(numerator)
        self.denumerator = int(denumerator)

        def add(self, other):
          znam = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
          chisl = znam // self.denumerator * self.numerator + znam // other.denumerator * other.numerator
          return f"{chisl}/{znam}"

        def sub(self, other):
          znam = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
          chisl = znam // self.denumerator * self.numerator - znam // other.denumerator * other.numerator
          return  f"{chisl}/{znam}"

        def mul(self, other):
          znam = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
          chisl = znam // self.denumerator * self.numerator - znam // other.denumerator * other.numerator
          return  f"{chisl}/{znam}"

        def floordiv(self, other):
          znam = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
          chisl = znam // self.denumerator * self.numerator - znam // other.denumerator * other.numerator
          return  f"{chisl}/{znam}"