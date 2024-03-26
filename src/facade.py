from src.map import Map
from src.ego import Ego
from src.npc import Npc_Car
from src.yaml_exporter import YamlExporter

class Facade:
    @staticmethod
    def crossroad_scenario(map_filepath: str, yaml_filepath: str='./sample.yaml'):
        m: Map = Map(map_filepath)

        pos: tuple[int, int] = m.search_crossroad()

        ego: Ego = Ego()
        ego.pos = tuple([x + y for x, y in zip(pos, (0, 1))])
        ego.velocity = (0, -1)

        npcs: list[Npc_Car] = []
        npc: Npc_Car = Npc_Car()
        npc.pos = tuple([x + y for x, y in zip(pos, (1, 0))])
        npc.velocity = (-1, 0)
        npcs.append(npc)
        npc: Npc_Car = Npc_Car()
        npc.pos = tuple([x + y for x, y in zip(pos, (-1, -1))])
        npc.velocity = (1, 1)
        npcs.append(npc)

        YamlExporter.export(map_filepath, ego, npcs, yaml_filepath)