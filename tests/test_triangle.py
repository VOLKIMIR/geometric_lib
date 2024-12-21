import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area_with_valid_sides(self):
        # Arrange
        side_a, side_b, side_c = 3, 4, 5

        # Act
        result = area(side_a, side_b, side_c)

        # Assert
        self.assertAlmostEqual(result, 6.0, places=5)

    def test_area_with_invalid_sides_raises_assertion_error(self):
        # Arrange
        side_a, side_b, side_c = 1, 2, 10

        # Act & Assert
        with self.assertRaises(AssertionError):
            area(side_a, side_b, side_c)

    def test_perimeter_with_valid_sides(self):
        # Arrange
        side_a, side_b, side_c = 3, 4, 5

        # Act
        result = perimeter(side_a, side_b, side_c)

        # Assert
        self.assertEqual(result, 12)

    def test_perimeter_with_negative_sides_raises_assertion_error(self):
        # Arrange
        side_a, side_b, side_c = -1, 4, 5

        # Act & Assert
        with self.assertRaises(AssertionError):
            perimeter(side_a, side_b, side_c)


if __name__ == "__main__":
    unittest.main()
