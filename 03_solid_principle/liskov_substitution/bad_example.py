# スーパータイプ
class Rectangle:
    def __init__(self):
        self._width = 0
        self._height = 0

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height

    def get_area(self) -> int:
        return self._width * self._height


# サブタイプ
class Square(Rectangle):
    @property
    def width(self) -> int:
        return super().width

    @width.setter
    def width(self, width: int):
        self._width = width
        self._height = width

    @property
    def height(self) -> int:
        return super().height

    @height.setter
    def height(self, height: int):
        self._width = height
        self._height = height


def f(r: Rectangle, width: int, height: int) -> int:
    r.width = width
    r.height = height
    return r.get_area()


if __name__ == "__main__":
    r1 = Rectangle()
    r2 = Square()

    print(f(r1, 3, 4))
    print(f(r2, 3, 4))
