def do_plus(var1, var2):
    """return a value which two parament add"""

    try:
        if type(var1) == type(var2) and isinstance(var1, int) or isinstance(var1, str):
            return var1 + var2
    except TypeError as err:
        print("Error %s" % str(err))
