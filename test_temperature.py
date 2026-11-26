

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
