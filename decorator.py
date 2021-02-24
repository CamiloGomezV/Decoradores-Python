def validate_point(function):
    def wrapper(fighter, type_point, score_desicion=[]):
        if len(score_desicion) == 0:
            return function(fighter, type_point)
        elif score_desicion.count(True) < 2:
            print("Invalid point")
        else:
            return function(fighter, type_point)
    return wrapper
