from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost=3
    min_range=0
    max_range=float('inf')
    def nearest_terminator(self, skynet):
        """Returns the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        s=self.place
        c=0
        while c<self.min_range and s!=skynet:
            c+=1
            s=s.entrance

        k=c
        while k<=self.max_range and s != skynet:
            k+=1
            if len(s.terminators)>0:
                return random_or_none(s.terminators)
                break
            else:
                s=s.entrance
        return None

    def throw_at(self, target):
        """Throwing a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)



    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
