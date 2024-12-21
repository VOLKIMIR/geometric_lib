def area(side_a, side_b, side_c):
    assert all(x > 0 for x in [side_a, side_b, side_c]), "Side lengths >0"

    semi_per = (side_a + side_b + side_c) / 2
    return (
        semi_per * (semi_per - side_a) * (semi_per - side_b) * (semi_per - side_c)
    ) ** 0.5


def perimeter(side_a, side_b, side_c):
    assert all(x > 0 for x in [side_a, side_b, side_c]), "Side lengths >0"
    return side_a + side_b + side_c
