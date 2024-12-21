def area(a, b, c):
    assert all(x > 0 for x in [a, b, c]), "Side lengths >0"

    p = (side_a + side_b + side_c) / 2
    return (
        p * (p - a) * (p - b) * (p - c)
    ) ** 0.5


def perimeter(a, b, c):
    assert all(x > 0 for x in [a, b, c]), "Side lengths >0"
    return a + b + c
