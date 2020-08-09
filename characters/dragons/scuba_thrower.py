from .thrower_dragon import ThrowerDragon
class ScubaThrower(ThrowerDragon):
    implemented = True
    is_watersafe=True
    food_cost=6
    def reduce_armor(self,amount):
        if self.place is not water:
            self.reduce_armor(amount)
