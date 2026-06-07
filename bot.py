import CENOURA
import FENO
import ABOBORA
import MADEIRA
import GIRA_SOL
import CACTO
set_world_size(10)
while True:
	feno = num_items(Items.Hay)
	madeira = num_items(Items.wood)
	abobora = num_items(Items.Pumpkin)
	cenoura = num_items(Items.Carrot)
	cacto = num_items(Items.Cactus)
	gira_sol = num_items(Items.Power)
	
	if cenoura < feno or cenoura < madeira:
		CENOURA.coletar_cenoura()
	elif abobora < cenoura:
		ABOBORA.coletar_abobora()	
	elif cacto < abobora:
		CACTO.coletar_cacto()
	else:			
		if feno < madeira:
			FENO.coletar_feno()
		elif feno > madeira:
			MADEIRA.coletar_madeira()
		elif gira_sol < cenoura:
			GIRA_SOL.coletar_gira_sol()