


class Temperature:
    def __init__(self, value, unit="C"):
        self.value = value
        self.unit = unit.upper()

celsius = Temperature(25, "C")
fahrenheit = Temperature(77, "F")
kelvin = Temperature(298.15, "K")

print(celsius.value, celsius.unit)
print(fahrenheit.value, fahrenheit.unit)
print(kelvin.value, kelvin.unit)

#small test 
t = Temperature(25, "c")
print(t.value, t.unit)    # skal gi: 25 C

t2 = Temperature(10)
print(t2.value, t2.unit)  # skal gi: 10 C

