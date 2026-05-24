from IRRIGAR import irrigar

#abobora TESTE VSCODE
def coletar_abobora():
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			
			harvest()
			
			if get_ground_type() != Grounds.Soil:
				till()
			irrigar()
			plant(Entities.Pumpkin)
				
			while True:
				if get_entity_type() == Entities.Dead_Pumpkin:
					irrigar()
					plant(Entities.Pumpkin)
				if can_harvest():
					use_item(Items.Fertilizer)
					break

			move(East)
		move(North)
	