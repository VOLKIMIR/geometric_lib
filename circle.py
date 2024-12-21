import math


def calculate_area(radius):
    assert radius >= 0, "Radius cannot be negative"
    return math.pi * radius * radius


def calculate_perimeter(radius):
    assert radius >= 0, "Radius cannot be negative"
    return 2 * math.pi * radius
