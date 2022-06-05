from flask import Flask
from generate_all import generate
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# a flask route that defines an empty dictionary called sectors, calls generate function with sectors and returns sectors
@app.route("/sectors/<float:sector_size>/<float:sector_margin_proportion>/<int:sector_axis_count>/<float:planet_generation_area_threshold>/<float:moon_generation_chance>/<int:max_moon_count>/<int:planet_base_size>/<float:asteroid_generation_chance>/<int:max_asteroid_count>")
def sectors(sector_size, sector_margin_proportion, sector_axis_count, planet_generation_area_threshold, moon_generation_chance, max_moon_count, planet_base_size, asteroid_generation_chance, max_asteroid_count):
    sectors = {}
    _current_sector = (0.0, 0.0)
    generate(sectors=sectors, 
        _current_sector=_current_sector,
        sector_size=sector_size,
        sector_margin_proportion=sector_margin_proportion,
        sector_axis_count=sector_axis_count,
        planet_generation_area_threshold=planet_generation_area_threshold,
        moon_generation_chance=moon_generation_chance,
        max_moon_count=max_moon_count,
        planet_base_size=planet_base_size,
        asteroid_generation_chance=asteroid_generation_chance,
        max_asteroid_count=max_asteroid_count)
    return sectors
    
# a flask route that defines an empty dictionary called sectors, calls generate function with sectors and returns sectors
@app.route("/sectors")
def sectors2():
    sectors = {}
    _current_sector = (0.0, 0.0)
    generate(sectors=sectors, _current_sector=_current_sector)
    return sectors
    