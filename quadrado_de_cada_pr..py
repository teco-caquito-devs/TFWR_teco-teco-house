import CENOURA
import FENO
import ABOBORA
import MADEIRA
import GIRA_SOL
import CACTO
import rastrear
rastrear.rastrear(0, 0)

while True:
	feno = num_items(Items.Hay)
	madeira = num_items(Items.wood)
	abobora = num_items(Items.Pumpkin)
	cenoura = num_items(Items.Carrot)
	cacto = num_items(Items.Cactus)
	gira_sol = num_items(Items.Power)
	
	FENO.coletar_feno()
	FENO.coletar_feno()
	MADEIRA.coletar_madeira()
	MADEIRA.coletar_madeira()
	if cenoura < madeira and cenoura < feno:
		CENOURA.coletar_cenoura()
	if cenoura < madeira and cenoura < feno:
		CENOURA.coletar_cenoura()
	if abobora < cenoura:
		ABOBORA.coletar_abobora()
	if abobora < cenoura:
		ABOBORA.coletar_abobora()
	CACTO.coletar_cacto()
	CACTO.coletar_cacto()
	if gira_sol < cenoura:
		GIRA_SOL.coletar_gira_sol()
	if gira_sol < cenoura:
		GIRA_SOL.coletar_gira_sol()