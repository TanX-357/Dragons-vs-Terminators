from .dragon import Dragon
from .scuba_thrower import ScubaThrower
from .container_dragon import ContainerDragon
from utils import terminators_win
class DragonKing(ScubaThrower):
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    food_cost=7
    d={} #dictionary to keep track of dragons whose damage has been already doubled by the king

    implemented = False
    instantiated=False
    def __init__(self, armor=1):
        super().__init__()
        if self.implemented is False:
            DragonKing.set_class_implemented()
            self.instantiated=False



    @classmethod
    def set_class_implemented(cls):
        if cls.implemented is False:
            cls.implemented=True
            cls.instantiated=True





    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        if self.instantiated is False:
            super().action(colony)
            s=self.place.exit
            while s is not None:
                if s.dragon is not None:
                    if isinstance(s.dragon,ContainerDragon):
                        if s.dragon not in self.d:
                            if s.dragon.contained_dragon is not None:
                                if s.dragon.contained_dragon not in self.d:
                                    s.dragon.contained_dragon.damage*=2
                                    self.d[s.dragon.contained_dragon]=1
                            s.dragon.damage*=2
                            self.d[s.dragon]=1
                        else:
                            if s.dragon.contained_dragon is not None:
                                if s.dragon.contained_dragon not in self.d:
                                    s.dragon.contained_dragon.damage*=2
                                    self.d[s.dragon.contained_dragon]=1
                    else:
                        if s.dragon not in self.d:
                            s.dragon.damage*=2
                            self.d[s.dragon]=1
                s=s.exit
        else:
            self.reduce_armor(self.armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        self.armor -= amount
        if self.armor <= 0:
            self.place.remove_fighter(self)
            if self.instantiated is False:
                terminators_win()

            self.death_callback()
