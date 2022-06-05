def _generate_planets_at(_sectors, sector: tuple(int, int), planet_generation_area_threshold):
	if _sectors[sector].planet:
		return

	# Calculate the area created by the 3 seeded points.
	vertices = _sectors[sector].seeds
	area = _calculate_triangle_area(vertices[0], vertices[1], vertices[2])

	# If the area is less than the generation threshold, create a planet appropriate
	# to the seeds' area.
	if area < planet_generation_area_threshold:
		_sectors[sector].planet = {
			"position": _calculate_triangle_epicenter(vertices[0], vertices[1], vertices[2]),
			"scale": 0.5 + area / (planet_generation_area_threshold / 2.0)
		}




## Returns the area of a triangle.
def _calculate_triangle_area(a: tuple(int, int), b: tuple(int, int), c: tuple(int, int)) -> float:
	return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0



def _calculate_triangle_epicenter(a: tuple(int, int), b: tuple(int, int), c: tuple(int, int)) -> tuple(int, int):
	return (a[0] + b[0] + c[0]) / 3.0, (a[1] + b[1] + c[1]) / 3.0
