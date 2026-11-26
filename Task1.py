

class Temperature:
    TOLERANCE = 1e-9

class Temperature:
    def __init__(self,value: float, unit="C"):
        self._value = float(value)
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

    def to_fahrenheit(self):
        if self.unit == "C":
            return (self.value * 9/5) + 32
        
        elif self.unit == "F":
            return self.value
        
        elif self.unit == "K":
            return (self.value - 273.15) * 9/5 + 32
   
    def to_kelvin(self):
        if self.unit == "C":
            return self.value + 273.15
        
        elif self.unit == "F":
            return (self.value - 32) * 5/9 + 273.15
        
        elif self.unit == "K":
            return self.value

        
    def convert_to(self, target_unit):
        target_unit = target_unit.upper()
        if target_unit not in ("C", "F", "K"):
            raise ValueError("Target unit must be 'C', 'F', or 'K'.")

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        elif target_unit == "K":
            return Temperature(self.to_kelvin(), "K")
        
    def __str__(self):
        return f"{self.value:.2f} °{self.unit}"

    def __repr__(self):
        return f"Temperature({self.value}, '{self.unit}')"

    def __eq__(self, other):
        if isinstance(other, Temperature):
            return abs(self.to_kelvin() - other.to_kelvin()) <= Temperature.TOLERANCE
        return NotImplemented
    # Insitance: askes if the other object is an Temperature object, 
    # if it is, it converts both to Kelvin and checks if the difference is within the tolerance. 
    # If not, it returns NotImplemented. as in it does not know how to compare the two objects.
    
t = Temperature(0, "C")
t_f = t.convert_to("f")
print(t_f.value, t_f.unit)   # should give: 32.0 F
        
    
  
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
#print(t2.value, t2.unit)  # should give: 10 C

#t_bad = Temperature(25, "X")   # should raise ValueError

#t.unit = "Banana"  # should raise AttributeError since unit is read-only

#assert Temperature(32, "F").to_celsius() == 5.0 -- tested with assert, to se if value is correct, 
# but commented out to avoid stopping the script


print(Temperature(0, "C") == 0)
print(Temperature(0, "C") == "hello")

t = Temperature(25, "C")
print(str(t))     # 25.00 °C
print(repr(t))    # Temperature(25.0, 'C')
# A lite test to see if the conversion methods work correctly


print(Temperature(-40, "F").to_kelvin())
assert abs(Temperature(-40, "F").to_kelvin() - 233.15) <= Temperature.TOLERANCE
# The code gets more tolerant to floating point errors, so it checks if the difference is less than or equal to 0.1

""" Celsius """
print(f"{Temperature(32, "F").to_celsius()} C")  # should give: 0.0
print(f"{Temperature(273.15, "K").to_celsius()} C")  # should give: 0.0
print(f"{Temperature(25, "C").to_celsius()} C") # should give: 25.0

""" Fahrenheit """
print(f"{Temperature(32, "F").to_fahrenheit()} F")  # should give: 32.0
print(f"{Temperature(273.15, "K").to_fahrenheit()} F")  # should give: 32.0
print(f"{Temperature(25, "C").to_fahrenheit()} F")  # should give: 77.0

""" Kelvin """
print(f"{Temperature(0, "C").to_kelvin()} K")       # should give: 273.15
print(f"{Temperature(212, "F").to_kelvin()} K")     # should give: 373.15
print(f"{Temperature(300, "K").to_kelvin()} K")     # should give: 300.0

print(Temperature(25, "C"))
print(Temperature(98.6, "f"))

print(Temperature(0, "C") == Temperature(32, "F"))