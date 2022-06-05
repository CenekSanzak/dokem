from generate_seeds import _generate_seeds_at
from generate_planets import _generate_planets_at
from generate_moons import _generate_moons_at
from generate_travel_lanes import _generate_travel_lanes_at
import time

LAYERS = {
	"seeds": [],
	"planet": {},
	"moons": [],
	"travel_lanes": [],
	"asteroids": [],
}

def generate(sectors, _current_sector: tuple[int, int], _half_sector_count=5):
    start_time = time.time()
    index = -1
    for layer in LAYERS:
        index += 1
        for x in range(
            _current_sector.x - _half_sector_count + index,
            _current_sector.x + _half_sector_count - index
        ):
            for y in range(
                _current_sector.y - _half_sector_count + index,
                _current_sector.y + _half_sector_count - index
            ):
                sector = Vector2(x, y)
                match layer:
                    case "seeds":
                        # Initialize the sector's data at the start.
                        if sector not in    sectors:
                            sectors[sector] = LAYERS.duplicate(true)
                        _generate_seeds_at(sector)
                    case "planet":
                        _generate_planets_at(sector)
                    case "moons":
                        _generate_moons_at(sector)
                    case "travel_lanes":
                        _generate_travel_lanes_at(sector)
                    #case "asteroids":
                    #	_generate_asteroids_at(sector)
    end_time = time.time()
    print((end_time - start_time))
#update()
