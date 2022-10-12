#!/usr/bin/env python3
# -*- coding: utf-8 -*

from item import Item


if __name__ == "__main__":
    print(f'{__name__} script running.')

    item1 = Item('Freedom', 1, 1)
    item1.name = 'Texas'


    print(item1.name)


    # Item.instantiate_some_examples()

    # print(Item.is_integer(7.0))
    #
    # print(Item.all)
