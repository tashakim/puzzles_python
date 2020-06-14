def cakerecipe(recipe, available):
	"""Purpose: Helps Pete find how many cakes ze can bake 
	considering his recipes.
	Note: If ingredient in recipe is not available, return 0.
	"""
	min_n = float("inf")
	for item in recipe:
		if(item not in available):
			print("Ingredient is not available.")
			return 0
		if(available[item]//recipe[item] < min_n):
			min_n = available[item]//recipe[item]
	return min_n
