# Example 7
# Getters and Setters
from item import Item
from phone import Phone
from keyboard import Keyboard

# Item.instantiate_from_csv()
# print(Item.all)



item1 = Item("MyItem", 750, 6)

# Setting the Attribute
# item1.name = "OtherItemhkj"
# item1.apply_increment(0.2)

# Getting the Attribute
# print(item1.price)

# item1.send_email()

item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount()

print(item1.price)