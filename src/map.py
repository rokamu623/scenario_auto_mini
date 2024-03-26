class Map:
    def __init__(self, map_filepath: str):
        map_data = open(map_filepath, 'r')
        self._map_str = map_data.read()
        map_data = open(map_filepath, 'r')
        self._map = [[_ for _ in r.replace('\n', '')] for r in map_data.readlines()]

    def search_crossroad(self) -> tuple[int, int]:
        try:
            y = ['x' in r for r in self._map].index(True)
            x = self._map[y].index('x')
        except:
            raise ValueError('crossroad not found.')

        return x, y

    def display(self):
        print(self._map_str)