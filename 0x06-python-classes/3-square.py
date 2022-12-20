#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """Represents a square class"""

    def __init__(self, size=0):
        """Initializing the square class
        Arguments is size. It represents the size of the square class
        Raises:
        - TypeError if size is not an integer
        - ValueError if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculates area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
