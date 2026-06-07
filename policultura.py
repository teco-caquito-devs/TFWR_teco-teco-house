import rastrear
ord_p = []
while True:
	world_size = get_world_size() * get_world_size()
	check_plant = 0
	while not check_plant == world_size:
		company = get_companion()
		ord_p.append((get_pos_x() , get_pos_y()))
		tp = company[0]
		ps = company[1]
		pos_x = ps[0]
		pos_y = ps[1]
		rastrear.rastrear(pos_x, pos_y)
		harvest()
		if tp == Entities.Carrot:
			if get_ground_type() == Grounds.Grassland:
				till()
		else:
			if get_ground_type() == Grounds.Soil:
				till()
		plant(tp)
		check_plant = check_plant + 1
	for t in range(check_plant):
		pfx2 = ord_p[t][0]
		pfy2 = ord_p[t][1]
		rastrear.rastrear(pfx2, pfy2)
		harvest()
	ord_p = []
	
		
		

	