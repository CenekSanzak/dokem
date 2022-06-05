def _generate_planets_at(sector: (int, int)=(0,0), sectors={}, planet_generation_area_threshold=5000.0):
	if "planet" in sectors[str(sector)]:
		return

	# Calculate the area created by the 3 seeded points.
	vertices = sectors[str(sector)]["seeds"]
	area = _calculate_triangle_area(vertices[0], vertices[1], vertices[2])

	# If the area is less than the generation threshold, create a planet appropriate
	# to the seeds' area.
	if area < planet_generation_area_threshold:
		sectors[str(sector)]["planet"] = {
			"position": _calculate_triangle_epicenter(vertices[0], vertices[1], vertices[2]),
			"scale": 0.5 + area / (planet_generation_area_threshold / 2.0)
		}




## Returns the area of a triangle.
def _calculate_triangle_area(a: (int, int), b: (int, int), c: (int, int)) -> float:
	return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0



def _calculate_triangle_epicenter(a: (int, int), b: (int, int), c: (int, int)) -> (int, int):
	return (a[0] + b[0] + c[0]) / 3.0, (a[1] + b[1] + c[1]) / 3.0


# Test code
if __name__ == "__main__":
    sectors={"(-160.0, -160.0)": {"seeds": [(328923.2, 3829.1), (328923.2, 3829.1), (328923.2, 3829.1)]}}
    _generate_planets_at(sector=(-160.0, -160.0), sectors=sectors)
    print(sectors)
