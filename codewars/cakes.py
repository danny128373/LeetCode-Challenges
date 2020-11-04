def cakes(recipe, available):
    num_cakes = 0
    cake_dict = dict()
    for k, v in recipe.items():
        try:
            if available[k]:
                cake_dict[k] = available[k]/recipe[k]
        except:
            return 0
    for key, value in cake_dict.items():
        if num_cakes == 0:
            num_cakes = cake_dict[key]
        elif num_cakes > cake_dict[key]:
            num_cakes = cake_dict[key]
    return int(num_cakes)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
