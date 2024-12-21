def area(side_a, side_b, side_c):
    assert all(x > 0 for x in [side_a, side_b, side_c]), "Side lengths must be positive"

    semi_perimeter = (side_a + side_b + side_c) / 2
    return (
        semi_perimeter
        * (semi_perimeter - side_a)
        * (semi_perimeter - side_b)
        * (semi_perimeter - side_c)
    ) ** 0.5


def perimeter(side_a, side_b, side_c):
    assert all(x > 0 for x in [side_a, side_b, side_c]), "Side lengths must be positive"
    return side_a + side_b + side_c
