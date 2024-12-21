def area(side_a, side_b, side_c):
    assert all(x > 0 for x in [side_a, side_b, side_c]), "Side lengths >0"

    p = (side_a + side_b + side_c) / 2
    return (
        p * (p - side_a) * (p - side_b) * (p - side_c)
    ) ** 0.5


def perimeter(side_a, side_b, side_c):
    assert all(x > 0 for x in [side_a, side_b, side_c]), "Side lengths >0"
    return side_a + side_b + side_c
