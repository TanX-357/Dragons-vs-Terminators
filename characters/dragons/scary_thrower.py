from .thrower_dragon import ThrowerDragon
from utils import apply_effect, make_scare

class ScaryThrower(ThrowerDragon):
    """ThrowerDragon that intimidates Terminators, making them back away instead of advancing."""

    name = 'Scary'
    implemented = True 
    food_cost=6

    def throw_at(self, target):
        "*** YOUR CODE HERE ***"
        if target:
            apply_effect(make_scare, target, 2)
