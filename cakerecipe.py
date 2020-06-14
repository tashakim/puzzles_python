def cakerecipe(recipe, available):
	"""Purpose: Helps Pete find how many cakes ze can bake 
	considering his recipes.
	Note: If ingredient in recipe is not available, return 0.
	"""
	min_n = float("inf")
	for item in recipe:
		if(item not in available):
			print("Ingredient: ", item, " is not available.")
			return 0
		if(available[item]//recipe[item] < min_n):
			min_n = available[item]//recipe[item]
	print("Pete can bake ", min_n, " many cakes.")

	return min_n

def better_sol(recipe, available):
	return min(available.get(item,0)//recipe[item] for item in recipe)
	# get function in python has two (2) parameters:
	# first param: key. second param: value returned when not found.


if __name__ == "__main__":
	recipe = {"flour": 500, "sugar": 200, "eggs": 1}
	available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
	assert(cakerecipe(recipe, available) == 2), "Wrong answer."
	assert(cakerecipe(recipe, available) == better_sol(recipe, available)), "Wrong answer."


	recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
	available = {"sugar": 500, "flour": 2000, "milk": 2000}
	assert(cakerecipe(recipe, available) == 0), "Wrong answer."
	assert(cakerecipe(recipe, available) == better_sol(recipe, available)), "Wrong answer."

	print("\nAll tests passed!")