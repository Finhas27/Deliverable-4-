"""Task 2"""

class Fraction:
    # Initialisation
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")

        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer")

        self.numerator = numerator
        self.denominator = denominator

    # String representations
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    # Comparison methods
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return not self.__eq__(other)
        
    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return self.numerator * other.denominator >= other.numerator * self.denominator
 
    # Arithmetic methods
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        if denominator < 0:
            numerator *= -1
            denominator *= -1

        return Fraction(numerator, denominator)

        