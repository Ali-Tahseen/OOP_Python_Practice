# # Example 1
# # Creating a class
# class Item:
#     pass


# item1 = Item()
# # item1 is
# # item1 is an instance of the class Item

# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# # Example 2
# # First method
# class Item:
#     def calculate_total_price(self):
#         return self.price * self.quantity
#         # self first argument is the object that is calling the method

# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price())
# # Can do multiple objects like item2 and so on

# # Second method
# class Item:
#     def calculate_total_price(self, x,y):
#         return x * y
#         # self first argument is the object that is calling the method

# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item()
# item2.name = "Phone"
# item2.price = 100
# item2.quantity = 5
# print(item2.calculate_total_price(item2.price, item2.quantity))
# # Can do multiple objects like item3 and so on


# # Example 3
# # Constructor
# class Item:
#     # can ensure that each attribute has a certain data type
#     def __init__(self, name: str, price: int, quantity: int):
#     # can initialize the attributes like: def __init__(self, name, price, quantity=0):
#     # Then it's not mandatory to pass the quantity
#     # __init__ is a constructor and gets triggered when the object is created
#         # print(f"An instance created: {name}, {price}, {quantity}")
#     # Run Validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
#     # This above assert checks to see if we giev positive numbers to ensure that we don't get negative numbers as inputs

#     # Assign the received arguments to the attributes
#         self.name = name
#         self.price = price
#         self.quantity = quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity
#     # Need the attributes once to be passed then can use self for the rest

# item1 = Item("Phone", 100, 5)
# print(item1.calculate_total_price())


# # Can pass more attributes like
# item1.has_numpad = False

# # Example 4
# # Class Attribute
# class Item:
#     pay_rate = 0.8 # Class Attribute and the pay rate after 20% discount
#     def __init__(self, name: str, price: int, quantity: int):
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
#     # This above assert checks to see if we giev positive numbers to ensure that we don't get negative numbers as inputs

#     # Assign the received arguments to the attributes
#         self.name = name
#         self.price = price
#         self.quantity = quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity
#     # Need the attributes once to be passed then can use self for the rest
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate

# item1 = Item("Phone", 100, 5)
# # Can access the class attribute like
# # print(Item.pay_rate)
# # Can access the class attribute like an object didn't find the attribute in an instantce level so it went to the class level
# # print(item1.pay_rate)
# # Built in attribute to see the attributes of class level
# # print(Item.__dict__)
# # Built in attribute to see the attributes of instance level
# # print(item1.__dict__)
# item1.apply_discount()
# # print(item1.price)

# # Can access attribute using instance level
# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# # Example 5
# # Most Replayed
# import csv

# class Item:
#     pay_rate = 0.8 # Class Attribute and the pay rate after 20% discount
#     all = []
#     def __init__(self, name: str, price: float, quantity: float):
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
#     # This above assert checks to see if we giev positive numbers to ensure that we don't get negative numbers as inputs

#     # Assign the received arguments to the attributes
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)
        
#     def calculate_total_price(self):
#         return self.price * self.quantity
#     # Need the attributes once to be passed then can use self for the rest
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
    
#     @classmethod
#     #  for intantiating instances from some structure data that we own 
#     def instantiate_from_csv(cls):
#         with open("D:/Python OOP/items.csv", 'r') as file: # cls is the class itself
#             # 'r' is the mode of the file is reading the file only
#             reader = csv.DictReader(file)
#             # DictReader is a class that reads the file and returns a dictionary
#             items = list(reader)
#         for item in items:
#             # instantiate our instantces
#             Item(
#                 name=item.get('name'),
#                 price =float(item.get('price')),
#                 quantity =float(item.get('quantity')),
#             )
    
#     @staticmethod
#     def is_integer(num):
#         # We will count out the floats that are point zero
#         # For i.e. 5.0, 10.0
#         if isinstance(num, float):
#             # Count out the floats that are point zero
#             return num.is_integer()
#         elif isinstance(num, int):
#             return True
#         else:
#             return False
        
#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"
    

# # Access class method
# Item.instantiate_from_csv()

# # Access static method
# print(Item.is_integer(5.0))

# # item1 = Item("Phone", 100, 1)
# # item2 = Item("Laptop", 1000, 3)
# # item3 = Item("Cable", 10, 5)
# # item4 = Item("Mouse", 50, 5)
# # item5 = Item("Keyboard", 75, 5)

# # print(Item.all)
# # Print all the items
# # for instance in Item.all:
# #     print(instance.name)

# # Example 6
# # Inheritance
# import csv

# class Item:
#     pay_rate = 0.8 # Class Attribute and the pay rate after 20% discount
#     all = []
#     def __init__(self, name: str, price: float, quantity: float):
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
#     # This above assert checks to see if we giev positive numbers to ensure that we don't get negative numbers as inputs

#     # Assign the received arguments to the attributes
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)
        
#     def calculate_total_price(self):
#         return self.price * self.quantity
#     # Need the attributes once to be passed then can use self for the rest
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
    
#     @classmethod
#     #  for intantiating instances from some structure data that we own 
#     def instantiate_from_csv(cls):
#         with open("D:/Python OOP/items.csv", 'r') as file: # cls is the class itself
#             # 'r' is the mode of the file is reading the file only
#             reader = csv.DictReader(file)
#             # DictReader is a class that reads the file and returns a dictionary
#             items = list(reader)
#         for item in items:
#             # instantiate our instantces
#             Item(
#                 name=item.get('name'),
#                 price =float(item.get('price')),
#                 quantity =float(item.get('quantity')),
#             )
    
#     @staticmethod
#     def is_integer(num):
#         # We will count out the floats that are point zero
#         # For i.e. 5.0, 10.0
#         if isinstance(num, float):
#             # Count out the floats that are point zero
#             return num.is_integer()
#         elif isinstance(num, int):
#             return True
#         else:
#             return False
        
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


# # Since class item doesn't have broken phone attributes
# # Inheritance
# class Phone(Item):
#     #  super functions will be enable us to access the attributes from parent class
#     def __init__(self, name: str, price: float, quantity: float, broken_phones=0):
#         #  Call to super function to access the attributes/methods from parent class
#         super().__init__(
#             name, price, quantity
#         )
#         assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than or equal to zero!"
#     # This above assert checks to see if we giev positive numbers to ensure that we don't get negative numbers as inputs

#     # Assign the received arguments to the attributes
#         self.broken_phones = broken_phones

# phone1 = Phone("Phone1", 500, 5, 1)
# # Method
# # print(phone1.calculate_total_price())
# # phone1.broken_phones = 1
# # phone2 = Phone("Phone2", 700, 5, 1)
# # phone2.broken_phones = 1
# print(Item.all)
# print(Phone.all)






