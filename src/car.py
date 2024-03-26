class Car:
    def __init__(self):
        self._pos: tuple[int, int] = (0, 0)
        self._velocity: tuple[float, float] = (0, 0)

    @property
    def pos(self) -> tuple[int, int]:
        return self._pos

    @pos.setter
    def pos(self, p: tuple[int, int]):
        self._pos = p

    @property
    def velocity(self) -> tuple[float, float]:
        return self._velocity

    @velocity.setter
    def velocity(self, direction: tuple[int, int]):
        square: float = (direction[0]**2 + direction[1]**2)
        self._velocity = (self.SPEED * direction[0] / square, self.SPEED * direction[1] / square)

    @property
    def SPEED(self) -> float:
        return 2.0