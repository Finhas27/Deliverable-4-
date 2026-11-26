


class Temperature:
    def __init__(self, value, unit="C"):
        self.value = value
        self.unit = unit.upper()
        if self.unit not in ("C", "F", "K"):
            raise ValueError("Temperature unit must be 'C', 'F', or 'K'.")

celsius = Temperature(25, "C")
fahrenheit = Temperature(77, "F")
kelvin = Temperature(298.15, "K")

print(celsius.value, celsius.unit)
print(fahrenheit.value, fahrenheit.unit)
print(kelvin.value, kelvin.unit)

#small test 
t = Temperature(25, "c")
#print(t.value, t.unit)    # should give: 25 C

t2 = Temperature(10)
#print(t2.value, t2.unit)  # should give: 10 C


"b" in ("a", "b", "c")    # True
"x" in ("a", "b", "c")    # False

t = Temperature(25, "c")
print(t.value, t.unit)     # should give : 25 C

t_bad = Temperature(25, "X")   # should raise ValueError