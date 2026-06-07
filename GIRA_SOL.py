def coletar_gira_sol():
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				harvest()
				till()
			if measure() == 15: 
				harvest()
			while measure() != 15:
				harvest()
				plant(Entities.Sunflower)
			move(East)
		move(North)
		