


class Temperature:
    def __init__(self, value, unit="C"):
        self._value = value
        self._unit = unit.upper()
        if self._unit not in ("C", "F", "K"):
            raise ValueError("Temperature unit must be 'C', 'F', or 'K'.")
    

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def to_celsius(self):
    
        if self.unit =="C":
            return self.value
        
        elif self.unit == "F":
            return (self.value -32)* 5/9
        
        elif self.unit == "K":
            return self.value -273.15

celsius = Temperature(25, "C")
fahrenheit = Temperature(77, "F")
kelvin = Temperature(298.15, "K")

print(celsius.value, celsius.unit)
print(fahrenheit.value, fahrenheit.unit)
print(kelvin.value, kelvin.unit)



# some small tests to see if the class works as expected
t = Temperature(25, "c")
#print(t.value, t.unit)    # should give: 25 C

t2 = Temperature(10)
print(t2.value, t2.unit)  # should give: 10 C

#t_bad = Temperature(25, "X")   # should raise ValueError

#t.unit = "Banana"  # should raise AttributeError since unit is read-only



print(Temperature(32, "F").to_celsius())  # should give: 0.0
print(Temperature(273.15, "K").to_celsius())  # should give: 0.0
print(Temperature(25, "C").to_celsius()) # should give: 25.0


