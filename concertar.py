def concertar_aboboras(s, check_pumpkin):
	import rastrear
	
	rastrear.rastrear(0, 0)
	for i in range(s):
		for i in range(s):
			if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
				plant(Entities.Pumpkin)
			elif get_entity_type() == Entities.Pumpkin:
				check_pumpkin = check_pumpkin + 1
			move(North)
		for i in range(s):
			move(South)
		move(East)
	return check_pumpkin