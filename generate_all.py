from generate_seeds import _generate_seeds_at
from generate_planets import _generate_planets_at
from generate_moons import _generate_moons_at
from generate_travel_lanes import _generate_travel_lanes_at
from generate_asteroids import _generate_asteroids_at
import time
from typing import Tuple

LAYERS = {
    "seeds": [],
    "planet": {},
    "moons": [],
    "travel_lanes": [],
    "asteroids": [],
}


def generate(sectors, _current_sector: Tuple[int, int], _half_sector_count=5):
    start_time = time.time()
    index = -1
    for layer in LAYERS:
        index += 1
        for x in range(
                int(_current_sector[0] - _half_sector_count + index),
                int(_current_sector[0] + _half_sector_count - index)
        ):
            for y in range(
                    int(_current_sector[1] - _half_sector_count + index),
                    int(_current_sector[1] + _half_sector_count - index)
            ):
                sector = (x, y)
                if layer == "seeds":
                    if sector not in sectors:
                        sectors.update({str(sector): {}})
                    _generate_seeds_at(sector=sector, sectors=sectors)
                if layer == "planet":
                    _generate_planets_at(sector=sector, sectors=sectors)
                if layer == "moons":
                    _generate_moons_at(sector=sector, sectors=sectors)
                if layer == "travel_lanes":
                    _generate_travel_lanes_at(sector=sector, sectors=sectors)
                if layer == "asteroids":
                    _generate_asteroids_at(sector=sector, sectors=sectors)
    end_time = time.time()
    print((end_time - start_time))


# Test code
if __name__ == "__main__":
    sectors = {}
    _current_sector = (0.0, 0.0)
    generate(sectors=sectors, _current_sector=_current_sector)
    print(sectors)
