
class Fridge:
    def __init__(self, items={}):
        if type(items) != type({}):
            raise TypeError("Fridge request a dictionary but was given %s" %
                            type(items))
        self.items = items
        return


    def __add_multi(self, food_name, quantity):
        if (not food_name in self.items):
            self.items[food_name] = 0

        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self, food_name):
        if type(food_name) != type(""):
            raise TypeError("add_one requires a string, given a %s" % type(food_name))
        else:
            self.__add_multi(food_name, 1)

        return True

    def add_many(self, food_dict):
        if type(food_dict) != type({}):
            raise TypeError("add_many requires a dict, given a %s" % type(food_dict))
        else:
            for item in food_dict.keys():
                self.__add_multi(item, food_dict[item])

    def has(self, food_name, quantity=1):
        
        
