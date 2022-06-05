import math
import random

PI = 3.141593


def _generate_asteroids_at(sector: (float, float),
                           sectors={},
                           start_seed="world generation",
                           asteroid_generation_chance=3.0 / 4.0,
                           max_asteroid_count=10,
                           planet_base_size=96):
    if str(sector) in sectors:
        if "asteroids" in sectors[str(sector)]:
            return

        if "planet" in sectors[str(sector)]:
            planet = sectors[str(sector)]["planet"]
            if not planet or "moons" not in sectors[str(sector)] or "travel_lanes" not in sectors[str(sector)]:
                return

            random.seed(make_seed_for(sector[0], sector[1], start_seed, "asteroids"))
            count = 0
            while random.uniform(0.0, 1.0) < asteroid_generation_chance and count < max_asteroid_count:
                count += 1
                random_rotated = rotate_random((0.0, 1.0))
                scale = planet["scale"]
                random_offset = (random_rotated[0] * scale * planet_base_size * random.uniform(3.0, 4.0),
                                 random_rotated[1] * scale * planet_base_size * random.uniform(3.0, 4.0))
                if "asteroids" in sectors[str(sector)]:
                    sectors[str(sector)]["asteroids"].append(
                        {"position": (planet["position"][0] + random_offset[0],
                                      planet["position"][1] + random_offset[1]),
                         "scale": planet["scale"] / 5.0})
                else:
                    sectors[str(sector)].update({
                        "asteroids": [{"position": (planet["position"][0] + random_offset[0],
                                                    planet["position"][1] + random_offset[1]),
                                       "scale": planet["scale"] / 5.0}]
                    })


def rotate_random(vec: (float, float)):
    angle = random.uniform(-PI, PI)
    return (vec[0] * math.cos(angle) - vec[1] * math.sin(angle),
            vec[0] * math.sin(angle) + vec[1] * math.cos(angle))


def make_seed_for(_x_id: int, _y_id: int, start_seed, custom_data=""):
    new_seed = start_seed + str(_x_id) + str(_y_id)
    if custom_data != "":
        new_seed = new_seed + custom_data
    return new_seed.__hash__()


# Test code
if __name__ == "__main__":
    sectors = {"(-160.0, -160.0)": {"planet": {"position": (328923.2, 3829.1), "scale": 1.0},
                                    "travel_lanes": [{"source": (328923.2, 3829.1),
                                                      "destination": (43824.5, 12.0)}],
                                    "moons": [{"position": (473892, 58932),
                                               "scale": 1.0}
                                              ]}}
    _generate_asteroids_at(sector=(-160.0, -160.0), sectors=sectors)
    print(sectors)
