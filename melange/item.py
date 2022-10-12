#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Item:
    pay_rate = 0.8  # global (class) variable for all instances
    all = []  # facultative argument to gather all instances

    def __init__(self, name: str, price: float = 0.0, quantity: int = 0):
        # validate arguments
        assert price >= 0, f'__price {price} is not greater or equal to 0'
        assert quantity >= 0, f'__price {quantity} is not greater or equal to 0'

        # Assign values to the instance attributes (different for each instance of a class)
        self.__name = name
        self.quantity = quantity
        self.__price = price

        # Actions to make
        Item.all.append(self)  # collect every instance the moment it was created

    # @property decorator - read only attribute. It allows, like getter to read the value of the attribute
    # @property is the getter!
    @property
    def name(self):
        return self.__name

    # setter as usuall
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name too long.")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        print('lets see if it is called when initialization')
        self.__price = value



    def __repr__(self) -> str:  # this is useful when you want to print the instance(e.g. print(Item.all))
        return f'{self.__class__.__name__} ({self.name},{self.quantity},{self.__price})'

    # class method are to be used, when you want to perform an action and don't have any instances yet
    # for example, when you want to read instances from csv file (here I will simply put them manually)
    @classmethod
    # since there is no instance yet, the first argument is the pointer like 'self' but it is pointing the class
    # that is why it is called cls to avoid confusion
    def instantiate_some_examples(cls):
        # those examples will be conserved in the global class argument 'all'

        Item("phone", 2, 4)
        Item("NorthCarolina", 1000, 3)
        Item("McDo", 1, 1000)
        Item("Seven", 7, 7)

    # static method is simply a normal function (not a method). When you define smh like this, it should
    # be connected somehow to the class (like when you need to do some basic math operations,
    # or verify if something is an int or not). Note that there is no more need for 'self'
    # this is something that should not be unique per instance !!!!!!
    @staticmethod
    # remember that you can call @class method or @staticmethod methods from Item. or from the lvl of instances item1.
    def is_integer(num):
        if isinstance(num, float):
            return False
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_price(self) -> float:
        # remember that instance can have its own copy of a global attribute, that is why you don't call Item.pay_rate
        new_price = self.__price * self.pay_rate
        print(f'New price: {new_price}')
        return new_price

if __name__ == "__main__":
    print(f'{__name__} script running.')
