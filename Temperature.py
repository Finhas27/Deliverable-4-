





class Temperature:
    TOLERANCE = 1e-9

    def __init__(self,value: float, unit="C"):
      
        self._value = float(value)
        self._unit = unit.upper()
        if self._unit not in ("C", "F", "K"):
            raise ValueError("Temperature unit must be 'C', 'F', or 'K'.")
        if self.to_kelvin() < -self.TOLERANCE:
            raise ValueError("Temperature is below absolute zero.")
        
        # Using -TOLERANCE instead of 0 gives a small margin for
        # floating-point errors, so values at absolute zero are not rejected.

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
            return abs(self.to_kelvin() - other.to_kelvin()) <=self.TOLERANCE
        return NotImplemented
    # Insitance: askes if the other object is an Temperature object, 
    # if it is, it converts both to Kelvin and checks if the difference is within the tolerance. 
    # If not, it returns NotImplemented. as in it does not know how to compare the two objects.

    def __ne__(self, other):
        if isinstance(other, Temperature):
            return not (self == other)
        return NotImplemented

        # The __ne__ method checks for inequality. 
        # If __eq__ changes, __ne__ will automatically reflect that change, 
        # ensuring consistency in equality and inequality comparisons.
    
    def __lt__(self, other):
        if isinstance(other, Temperature):
            return self.to_kelvin() < other.to_kelvin() -self.TOLERANCE
        return NotImplemented

    # The __lt__ method checks if the current temperature is less than another temperature.
    # It converts both temperatures to Kelvin for comparison.

    def __le__(self, other):
        if isinstance(other, Temperature):
            return self.to_kelvin() <= other.to_kelvin() + self.TOLERANCE
        return NotImplemented

    # The __le__ method checks if the current temperature is less than or equal to another temperature.

    def __gt__(self, other):
        if isinstance(other, Temperature):
            return self.to_kelvin() > other.to_kelvin() + self.TOLERANCE
        return NotImplemented

    # The __gt__ method checks if the current temperature is greater than another temperature.

    def __ge__(self, other):
        if isinstance(other, Temperature):
            return self.to_kelvin() >= other.to_kelvin() - self.TOLERANCE
        return NotImplemented

    # The __ge__ method checks if the current temperature is greater than or equal to another temperature.

    
    

    