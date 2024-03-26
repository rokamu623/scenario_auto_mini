from yaml import safe_dump

from src.ego import Ego
from src.npc import Npc_Car

class YamlExporter:
    @staticmethod
    def export(map_filepath: str, ego: Ego, npcs: list[Npc_Car], yaml_filepath: str):
        output_dict = {
            'map': map_filepath,
            'ego': {
                'pos': {
                    'x': ego.pos[0],
                    'y': ego.pos[1]
                },
                'velocity': {
                    'x': ego.velocity[0],
                    'y': ego.velocity[1]
                }
            },
            'npc': []
        }

        for npc in npcs:
            output_dict['npc'].append({
                'pos': {
                    'x': npc.pos[0],
                    'y': npc.pos[1]
                },
                'velocity': {
                    'x': npc.velocity[0],
                    'y': npc.velocity[1]
                }
            })

        try:
            safe_dump(output_dict, open(yaml_filepath, 'w'))
        except:
            raise FileNotFoundError(f'{yaml_filepath} not found')