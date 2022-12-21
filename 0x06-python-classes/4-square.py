#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """Represents a square class"""

    def __init__(self, size=0):
        """Initializing the square class
        Arguments is size. It represents the size of the square class
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves size of a square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size
        Raises:
        - TypeError if size is not an integer
        - ValueError if size is less than 0
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates area of the square
        Returns: The area of the square
        """

        return (self.__size ** 2)
