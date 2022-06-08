extends HTTPRequest

func _ready() -> void:
	self.set_use_threads(true)
	self.connect("request_completed", self, "_on_HTTPRequest_request_completed")

	# sector_size
	# sector_margin_proportion
	# sector_axis_count
	# planet_generation_area_threshold
	# moon_generation_chance
	# max_moon_count
	# planet_base_size
	# asteroid_generation_chance"
	# max_asteroid_count
	
	self.request("https://dokem.herokuapp.com/sectors/10000.0/0.1/500/5000.0/0.367/5/96/0.75/100")


func _on_HTTPRequest_request_completed( result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())

