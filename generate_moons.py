import math
import random

PI = 3.141593


def _generate_moons_at(sector: (float, float),
                       sectors={},
                       start_seed="world generation",
                       moon_generation_chance=1.1 / 3.0,
                       max_moon_count=5,
                       planet_base_size=96):
    if str(sector) in sectors:
        if "moons" in sectors[str(sector)]:
            return

        planet = sectors[str(sector)]["planet"]
        if not planet:
            return

        random.seed(make_seed_for(sector[0], sector[1], start_seed, "moons"))
        moon_count = 0
        while random.uniform(0.0, 1.0) < moon_generation_chance or moon_count == max_moon_count:
            random_rotated = rotate_random((0.0, 1.0))
            scale = planet["scale"]
            random_offset = (random_rotated[0] * scale * planet_base_size * 3.0,
                             random_rotated[1] * scale * planet_base_size * 3.0)
            moon_count += 1
            if "moons" in sectors[str(sector)]:
                sectors[str(sector)]["moons"].append(
                    {"position": (planet["position"][0] + random_offset[0], planet["position"][1] + random_offset[1]),
                     "scale": planet["scale"] / 3.0})
            else:
                sectors[str(sector)].update({
                    "moons": {"position": (planet["position"][0] + random_offset[0],
                                           planet["position"][1] + random_offset[1]),
                              "scale": planet["scale"] / 3.0}
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

# uncomment to test
# _generate_moons_at(sector=(-160.0, -160.0), sectors={"(-160.0, -160.0)": {"planet": {"position": (328923.2, 3829.1), "scale": 1.0}}})
