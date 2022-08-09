#!/usr/bin/python3
"""Degining class Rectangle"""
from models.Base import Base


class Rectangle(Base):
    """docstring for Rectangle.Base  def __init__(self, arg):
        super(Rectangle,Base.__init__(self, width, height, x=0, )
        self.arg = arg"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """docstring for Initialize new Rectangle

        Args:

        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle
        x (int): The x coordinate of the new Rectangle
        y (int): The y coordinate of the new Rectangle
        id (int): the id if the new Rectangle

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """docstring set/get the width of the new Rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise valueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """docstring set/get the value of new Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise valueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """docstring set/get the x coordinate of the new Rectangle"""

        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise valueError("x must be greater than 0")
        self.__x = value

    @property
    def y(self):
        """docstring set/get the  y coordinate of the new Rectangle"""

        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise valueError("y must be greater than 0")
        self.__y = value
