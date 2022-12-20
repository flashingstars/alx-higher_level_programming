#!/usr/bin/python3
"""A module that defines square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing the square class
        Argument is size. It represents the size of the square defined
        Raises:
        - TypeError if size is not an integer
        - ValueError if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
