#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
item.py defines the item class
Dani van Enk, 11823526
"""

class Item(object):
    """
    the item class defines an item
    """

    def __init__(self, name, description):
        """
        initizializes an item

        parameters:
        name - name of the item;
        description - description of the item
        """
        
        self.name = name
        self.description = description
    
    def __str__(self):
        """
        define the format string for when the class is printed
        """

        return f"{self.name}: {self.description}"