def coletar_cacto():
	for i in range(get_world_size()):
		for i in range(get_world_size()):	
			if can_harvest():
				harvest()
				
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			move(East)
		move(North)