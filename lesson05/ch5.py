def in_fridge(wanted_food):
    """This is a function to see if the fridege has a food.
    fridge has to be a dictionary defined outside of the function.
    the food to be searched for is in the string wanted_food"""
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count

def make_omelet(omelet_type):
    """blablabla"""
    if type(omelet_type) == type({}):
        print("omelet_type is a dictionary with ingredients")
        return make_food(omelet_type, "omelet")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print("I don't think I can make this kind of omelet: %s" %omelet_type)

def make_food(ingredients_needed, food_name):
    """make_food(ingredients_needed, food_name)
    Takes the ingredients from ingredients_needed and makes food_name"""
    for ingredient in ingredients_needed.keys():
        print("Adding %d of %s to make a %s"%
              (ingredients_needed[ingredient],ingredient, food_name))
    print("Made %s" % food_name)
    return food_name


def get_omelet_ingredients(omelet_name):
    """THis contains a dictionary of omelet names that can be produced,
    and there ingredients"""
    # All of our omelets need eggs and milk
    ingredients = {"eggs":2, "milk":1}
    if omelet_name == "cheese":
        ingredients["cheddar"] = 2
    elif omelet_name == 'western':
        ingredients['jack_cheese'] = 2
        ingredients['ham'] = 1
        ingredients['pepper'] = 1
        ingredients['onion'] = 1
    elif omelet_name == 'greek':
        ingredients['feta_cheese'] = 2
        ingredients['spinach'] = 2
    else:
        print("That's not on the menu, sorry!")
        return None
    return ingredients
                    
