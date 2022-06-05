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


def generate(sectors,
             _current_sector: Tuple[int, int],
             sector_size=1000.0,
             sector_margin_proportion=0.1,
             sector_axis_count=10,
             start_seed="world generation",
             planet_generation_area_threshold=5000.0,
             moon_generation_chance=1.1 / 3.0,
             max_moon_count=5,
             planet_base_size=96,
             asteroid_generation_chance=3.0 / 4.0,
             max_asteroid_count=10):
    _half_sector_count = int(sector_axis_count / 2.0)
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
                    _generate_seeds_at(sector=sector,
                                       sectors=sectors,
                                       start_seed=start_seed,
                                       sector_size=sector_size,
                                       sector_margin_proportion=sector_margin_proportion)
                if layer == "planet":
                    _generate_planets_at(sector=sector,
                                         sectors=sectors,
                                         planet_generation_area_threshold=planet_generation_area_threshold)
                if layer == "moons":
                    _generate_moons_at(sector=sector,
                                       sectors=sectors,
                                       start_seed=start_seed,
                                       moon_generation_chance=moon_generation_chance,
                                       max_moon_count=max_moon_count,
                                       planet_base_size=planet_base_size)
                if layer == "travel_lanes":
                    _generate_travel_lanes_at(sector=sector,
                                              sectors=sectors)
                if layer == "asteroids":
                    _generate_asteroids_at(sector=sector,
                                           sectors=sectors,
                                           start_seed=start_seed,
                                           asteroid_generation_chance=asteroid_generation_chance,
                                           max_asteroid_count=max_asteroid_count,
                                           planet_base_size=planet_base_size)

    end_time = time.time()
    print((end_time - start_time))


# Test code
if __name__ == "__main__":
    sectors = {}
    _current_sector = (0.0, 0.0)
    generate(sectors=sectors, _current_sector=_current_sector)
    print(sectors)
