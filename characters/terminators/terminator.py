from ..fighter import Fighter

class Terminator(Fighter):
    """A Terminator moves from place to place, following exits and stinging dragons."""

    name = 'Terminator'
    damage = 1
    is_watersafe=True
    no_of_times_scared=0
    is_scared=False
    has_been_scared=False

    def sting(self, dragon):
        """Attack a Dragon, reducing its armor by 1."""
        dragon.reduce_armor(self.damage)

    def move_to(self, place):
        """Move from the Terminator's current Place to a new PLACE."""
        if place.name=='Skynet':
            return
        self.place.remove_fighter(self)
        place.add_fighter(self)

    def blocked(self):
        """Return True if this Terminator cannot advance to the next Place."""

        if self.place.dragon is None:
            return False
        else:
            s=self.place.dragon
            if s.blocks_path is True:
                return True
            return False


    def action(self, colony):
        """A Terminator's action stings the Dragon that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The DragonColony, used to access game state information.
        """

        if(self.is_scared is False) or self.has_been_scared :
            destination = self.place.exit
        else:
            destination=self.place.entrance
            self.no_of_times_scared+=1
            if self.no_of_times_scared ==2:
                self.has_been_scared=True
        if self.blocked():
            self.sting(self.place.dragon)
        elif self.armor > 0 and destination is not None and destination.name != 'Skynet':
            self.move_to(destination)
