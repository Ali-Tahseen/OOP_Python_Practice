# Example 7
# Getters and Setters
from item import Item

# Since class item doesn't have broken phone attributes
# Inheritance
class Phone(Item):
    pay_rate = 0.5
    #  super functions will be enable us to access the attributes from parent class
    def __init__(self, name: str, price: float, quantity: float, broken_phones=0):
        #  Call to super function to access the attributes/methods from parent class
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than or equal to zero!"
    # This above assert checks to see if we giev positive numbers to ensure that we don't get negative numbers as inputs

    # Assign the received arguments to the attributes
        self.broken_phones = broken_phones