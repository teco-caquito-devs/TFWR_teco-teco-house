

#FENO
def coletar_feno():
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Grassland:
				till()
			move(East)
		move(North)