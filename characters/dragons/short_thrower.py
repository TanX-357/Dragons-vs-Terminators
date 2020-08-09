from .thrower_dragon import ThrowerDragon


class ShortThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at most 3 places away."""

    name = 'Short'
    implemented = True
    food_cost=2

    def __init__(self):
        super(ThrowerDragon,self).__init__()
        self.min_range=0
        self.max_range=3
    def min_range(f):
        self.min_range=f
    def max_range(ff):
        self.max_range=ff
