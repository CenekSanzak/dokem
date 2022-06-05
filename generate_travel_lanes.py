def _generate_travel_lanes_at(sector: (float, float),
                              sectors={}):
    neighbors = [(1, 0),
                 (1, 1),
                 (0, 1),
                 (-1, 1),
                 (-1, 0),
                 (-1, -1),
                 (0, -1),
                 (1, -1)]

    if str(sector) in sectors:
        if "travel_lanes" in sectors[str(sector)]:
            return

        planet = sectors[str(sector)]["planet"]
        if not planet:
            return

        for neighbor in neighbors:
            neighboring_sector_key = str((sector[0] + neighbor[0],
                                          sector[1] + neighbor[1]))
            if neighboring_sector_key in sectors:
                neighboring_sector = sectors[neighboring_sector_key]
                if neighboring_sector:
                    if "planet" not in neighboring_sector:
                        continue
                else:
                    continue

                neighbor_position = neighboring_sector["planet"]["position"]
                if "travel_lanes" in sectors[str(sector)]:
                    sectors[str(sector)]["travel_lanes"].append({"source": (planet["position"][0],
                                                                            planet["position"][1]),
                                                                 "destination": (neighbor_position[0],
                                                                                 neighbor_position[1])})
                else:
                    sectors[str(sector)].update({"travel_lanes": [
                        {"source": (planet["position"][0], planet["position"][1]),
                         "destination": (neighbor_position[0], neighbor_position[1])}]})


# uncomment to test

if __name__ == "__main__":
    sectors={"(-160.0, -160.0)": {"planet": {"position": (328923.2, 3829.1), "scale": 1.0}},
                                    "(-160.0, -159.0)": {"planet": {"position": (43824.5, 12.0), "scale": 0.5}}}
    _generate_travel_lanes_at(sector=(-160.0, -160.0),
                            sectors=sectors)
    print(sectors)