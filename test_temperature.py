

import pytest
from temperature import Temperature


def test_default_unit():
    t = Temperature(10)
    assert t.unit == "C"
   # Check that default unit is Celsius

def test_case_insensitivity():
    t = Temperature(10, "f")
    assert t.unit == "F"
    # Check that lowercase unit is converted to uppercase.

def test_unit_is_read_only():
    t = Temperature(10)
    with pytest.raises(AttributeError):
        t.unit = "F"
        # Check that the unit is read-only and cannot be changed after initialization
        # read-only means that the attribute cannot be modified after the object is created.

def test_value_is_read_only():
    t = Temperature(10)
    with pytest.raises(AttributeError):
        t.value = 20
        # Check that the value is read-only and cannot be changed after initialization
        

def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(10, "X")
        # Check that an invalid unit raises a ValueError.


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-273.16, "C")
        # Check that a temperature below absolute zero in Celsius raises a ValueError.

def test_below_absolute_zero_fahrenheit():
    with pytest.raises(ValueError):
        Temperature(-459.68, "F")
        # Check that a temperature below absolute zero in Fahrenheit raises a ValueError.

def test_below_absolute_zero_kelvin():
    with pytest.raises(ValueError):
        Temperature(-1, "K")
        # Check that a temperature below absolute zero in Kelvin raises a ValueError.




#---------------------------------------------------------
# Test cases for temperature conversions    
def test_freeze_point():
    t = Temperature(0, "C")
    assert t.to_fahrenheit() == pytest.approx(32, abs=1e-9)
    assert t.to_kelvin() == pytest.approx(273.15, abs=1e-9)



def test_boiling_point():
    t = Temperature(100, "C")
    assert t.to_fahrenheit() == pytest.approx(212, abs=1e-9)
    assert t.to_kelvin() == pytest.approx(373.15, abs=1e-9)


def test_human_body_temperature():
    t = Temperature(37, "C")
    assert t.to_fahrenheit() == pytest.approx(98.6, abs=1e-9)
    assert t.to_kelvin() == pytest.approx(310.15, abs=1e-9)


def test_absolute_zero():
    t = Temperature(0, "K")
    assert t.to_celsius() == pytest.approx(-273.15, abs=1e-9)
    assert t.to_fahrenheit() == pytest.approx(-459.67, abs=1e-9)


def test_crossing_points():
    t = Temperature(-40, "C")
    assert t.to_kelvin() == pytest.approx(233.15, abs=1e-9)
    assert t.to_fahrenheit() == pytest.approx(-40, abs=1e-9)
    assert Temperature(-40, "F").to_celsius() == pytest.approx(-40, abs=1e-9)


#---------------------------------------------------------

def test_round_trip():
    t = Temperature(25, "C")
    convert_to_f = t.to_fahrenheit()
    convert_back_to_k = Temperature(convert_to_f, "F").to_kelvin()
    convert_back_to_c = Temperature(convert_back_to_k, "K").to_celsius()
    assert convert_back_to_c == pytest.approx(25, abs=1e-9)

# Converts temperature from C -> F -> K -> C 
# and checks if the final value is approximately equal to the original value that is (25°C).