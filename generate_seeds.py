import random


def _generate_seeds_at(sector: (float, float),
                       sectors={},
                       start_seed="world generation",
                       sector_size=1000.0,
                       sector_margin_proportion=0.1):
    _half_sector_size = sector_size / 2
    _sector_margin = sector_size * sector_margin_proportion

    if str(sector) in sectors:
        if "seeds" in sector:
            return

    random.seed(make_seed_for(sector[0], sector[1], start_seed, "seeds"))

    half_size = (_half_sector_size, _half_sector_size)
    margin = (_sector_margin, _sector_margin)

    top_left = (sector[0] * sector_size - half_size[0] + margin[0],
                sector[1] * sector_size - half_size[1] + margin[1])
    bottom_right = (sector[0] * sector_size + half_size[0] - margin[0],
                    sector[1] * sector_size + half_size[1] - margin[1])

    seeds = []
    for i in range(3):
        seed_position = (random.uniform(top_left[0], bottom_right[0]),
                         random.uniform(top_left[1], bottom_right[1]))
    seeds.append(seed_position)
    sectors.update({str(sector): {"seeds": seeds}})
    print(sectors)


def make_seed_for(_x_id: int, _y_id: int, start_seed, custom_data=""):
    new_seed = start_seed + str(_x_id) + str(_y_id)
    if custom_data != "":
        new_seed = new_seed + custom_data
    return new_seed.__hash__()

# uncomment to test
# _generate_seeds_at(sector=(-160.0, -160.0))
