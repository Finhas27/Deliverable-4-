import pytest
from fraction import Fraction


# Initialisation
def test_initialisation():
    fraction = Fraction(2, 3)

    assert fraction.numerator == 2
    assert fraction.denominator == 3


def test_invalid_types():
    with pytest.raises(TypeError):
        Fraction("1", 2)

    with pytest.raises(TypeError):
        Fraction(1, "2")

    with pytest.raises(TypeError):
        Fraction(1.5, 2)

    with pytest.raises(TypeError):
        Fraction(1, 2.5)


def test_invalid_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)

    with pytest.raises(ValueError):
        Fraction(1, -2)


# String representations
def test_str():
    assert str(Fraction(1, 2)) == "1/2"


def test_repr():
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"


# Comparisons
def test_eq():
    assert Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(1, 2) == Fraction(2, 4)
    assert not Fraction(1, 2) == Fraction(1, 3)


def test_ne():
    assert Fraction(1, 2) != Fraction(1, 3)


def test_lt():
    assert Fraction(1, 3) < Fraction(1, 2)

def test_le():
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert not Fraction(1, 2) <= Fraction(1, 3)


def test_gt():
    assert Fraction(1, 2) > Fraction(1, 3)


def test_ge():
    assert Fraction(1, 2) >= Fraction(1, 2)


# Arithmetic
def test_add():
    assert Fraction(1, 2) + Fraction(1, 2) == Fraction(1, 1)
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)


def test_sub():
    assert Fraction(1, 2) - Fraction(1, 2) == Fraction(0, 1)
    assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)


def test_mul():
    assert Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(2, 3) * Fraction(3, 4) == Fraction(1, 2)


def test_div():
    assert Fraction(1, 2) / Fraction(1, 2) == Fraction(1, 1)
    assert Fraction(1, 2) / Fraction(1, 3) == Fraction(3, 2)


# Edge cases
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 1)


def test_division_negative():
    assert Fraction(-1, 2) / Fraction(1, 2) == Fraction(-1, 1)
    assert Fraction(1, 2) / Fraction(-1, 2) == Fraction(-1, 1)
    assert Fraction(-1, 2) / Fraction(-1, 2) == Fraction(1, 1)


def test_unsupported_types():
    assert not Fraction(1, 2) == 5
    assert Fraction(1, 2) != 5

    with pytest.raises(TypeError):
        Fraction(1, 2) + 5

    with pytest.raises(TypeError):
        Fraction(1, 2) - 5

    with pytest.raises(TypeError):
        Fraction(1, 2) * 5

    with pytest.raises(TypeError):
        Fraction(1, 2) / 5

    with pytest.raises(TypeError):
        Fraction(1, 2) < 5

    with pytest.raises(TypeError):
        Fraction(1, 2) <= 5

    with pytest.raises(TypeError):
        Fraction(1, 2) > 5

    with pytest.raises(TypeError):
        Fraction(1, 2) >= 5

print("All tests passed successfully.")