import concertar
import rastrear
def ap():
	size = 22
	rastrear.rastrear(0, 0)
	harvest()
	for i in range(size):
		for i in range(size):
			if get_ground_type() != Grounds.Soil:
				till()
			harvest()
			plant(Entities.Pumpkin)
			move(North)
		for i in range(size):
			move(South)
		move(East)
		check_pumpkin = 0
	while not check_pumpkin == 484:
		check_pumpkin = 0
		rastrear.rastrear(0, 0)
		check_pumpkin = concertar.concertar_aboboras(size, check_pumpkin)
	harvest()
	rastrear.rastrear(0, 0)

		
		