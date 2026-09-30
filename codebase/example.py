"""Geometric calculation utility module for the sandbox project.

This module provides basic formulas to compute the area and perimeter
of various geometric shapes using native reStructuredText formatting.
"""

import math

class Circle:
    """Represents a geometric circle.

    :ivar radius: The distance from the center to the edge of the circle.
    :type radius: float
    """

    def __init__(self, radius: float):
        """Initializes the Circle with a given radius.

        :param radius: Must be a positive number.
        :type radius: float
        """
        self.radius = radius

    def get_area(self) -> float:
        """Calculates the total area of the circle.

        :returns: The area calculated using :math:`\\pi r^2`.
        :rtype: float
        """
        return math.pi * (self.radius ** 2)


class Rectangle:
    """Represents a geometric rectangle.

    :ivar width: The horizontal length.
    :type width: float
    :ivar height: The vertical length.
    :type height: float
    """

    def __init__(self, width: float, height: float):
        """Initializes the Rectangle.

        :param width: The horizontal length.
        :type width: float
        :param height: The vertical length.
        :type height: float
        """
        self.width = width
        self.height = height

    def get_area(self) -> float:
        """Calculates the total area of the rectangle.

        :returns: The width multiplied by the height.
        :rtype: float
        """
        return self.width * self.height
