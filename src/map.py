class Map:
    def __init__(self, map_file_path: str):
        map_data = open(map_file_path, 'r')
        self._map_str = map_data.read()
        self._map = [[_ for _ in r.replace('\n', '')] for r in map_data.readlines()]

    def display(self):
        print(self._map_str)