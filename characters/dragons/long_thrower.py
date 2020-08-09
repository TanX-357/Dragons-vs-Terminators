from .thrower_dragon import ThrowerDragon


class LongThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at least 5 places away."""

    name = 'Long'
    food_cost=2
    implemented = True
    def __init__(self):
        super(ThrowerDragon,self).__init__()
        self.min_range=5
        self.max_range=float('inf')
    def min_range(self,f):
        self.min_range=f
    def max_range(self,ff):
        self.max_range=ff
