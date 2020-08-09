from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    food_cost=6
    implemented = True


    def action(self, colony):
        super().action(colony)
        s=self.place.terminators.copy()
        for i in range(len(s)):
            s[i].reduce_armor(self.damage)
