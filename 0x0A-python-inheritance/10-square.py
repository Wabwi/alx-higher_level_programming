#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023

@author: Wabwi Ibrahim
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class shape, inheirts from Rectangle and BaseGeometry
    """

    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
