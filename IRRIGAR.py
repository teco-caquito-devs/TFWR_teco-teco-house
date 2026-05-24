def irrigar():
	while get_water() < 0.80:
		use_item(Items.Water)
	