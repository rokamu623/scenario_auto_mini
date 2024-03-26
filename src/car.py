class Car:
    def __init__(self):
        self._pos: tuple[int, int] = (0, 0)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, p):
        self._pos = p