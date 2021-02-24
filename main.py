from decorator import validate_point


class TaekwondoFight:
    def __init__(self, color_protector):
        self.color_protector = color_protector
        self.total_score = 0

    def __str__(self):
        return f"{self.color_protector} : {self.total_score} points"

    def update_score(self, point):
        self.total_score += point

    def get_score(self):
        return self.total_score


@validate_point
def mark_point(fighter, type_point):
    if type_point == 'head':
        fighter.update_score(3)
        return "Total points: {}".format(fighter.get_score())
    elif type_point == 'middle part':
        fighter.update_score(2)
        return "Total points: {}".format(fighter.get_score())
    else:
        return "Total points: {}".format(fighter.get_score())


fighter1 = TaekwondoFight('Red')

mark_point(fighter1, 'head')
mark_point(fighter1, 'middle part')
mark_point(fighter1, 'middle part', [True, True, False])
mark_point(fighter1, 'head', [True, False, False])

print(fighter1)
