# Example 7
# Getters and Setters
import csv

class Item:
    pay_rate = 0.8 # Class Attribute and the pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: float):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
    # This above assert checks to see if we giev positive numbers to ensure that we don't get negative numbers as inputs

    # Assign the received arguments to the attributes
        self.__name = name
        # double underscore to make it private and perfectly read only
        self.__price = price
        self.quantity = quantity


        # Actions to execute
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price*increment_value

    @property
    # Read only attributes
    # set attributes only once then cannot change it
    def name(self):
        return self.__name
        # double underscore to make it private and perfectly read only
    
    # Can still set after double underscore and chnage the attribute name to something else
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise ValueError("Name must be at least 10 characters long!")
        else:
            self.__name = value


    def calculate_total_price(self):
        return self.__price * self.quantity
    # Need the attributes once to be passed then can use self for the rest

    
    @classmethod
    #  for intantiating instances from some structure data that we own 
    def instantiate_from_csv(cls):
        with open("D:/Python OOP/items.csv", 'r') as file: # cls is the class itself
            # 'r' is the mode of the file is reading the file only
            reader = csv.DictReader(file)
            # DictReader is a class that reads the file and returns a dictionary
            items = list(reader)
        for item in items:
            # instantiate our instantces
            Item(
                name=item.get('name'),
                price =float(item.get('price')),
                quantity =float(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e. 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def connect(self, smpt_server):
        pass

    def prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name}{self.quantity} in stock.
        The price is {self.price}.
        """

    def send(self):
        pass

    def send_email(self):
        self.connect()
        self.prepare_body()
        self.send()

    # Methods can be private as well

    




