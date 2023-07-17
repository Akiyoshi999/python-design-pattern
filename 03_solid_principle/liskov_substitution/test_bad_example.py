import unittest
from bad_example import f, Rectangle, Square


class RectangleTest(unittest.TestCase):
    def test_rectangle_get_area(self):
        r = Rectangle()
        self.assertEqual(f(r, 3, 4), 12)

    def test_square_get_area(self):
        r = Square()
        self.assertEqual(f(r, 3, 4), 12)


unittest.main()
