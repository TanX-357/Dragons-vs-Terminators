from .dragon import Dragon
from ..fighter import Fighter


class ContainerDragon(Dragon):
    def __init__(self, *args, **kwargs):
        Dragon.__init__(self, *args, **kwargs)
        self.contained_dragon = None
        self.is_container=True

    def can_contain(self, other):
        if other.is_container is False and self.contained_dragon is None:
            return True
        return False

    def contain_dragon(self, dragon):
        self.contain_dragon=dragon

    def remove_dragon(self, dragon):
        if self.contained_dragon is not dragon:
            assert False, "{} does not contain {}".format(self, dragon)
        self.contained_dragon = None

    def remove_from(self, place):
        # Special handling for container dragons
        if place.dragon is self:
            # Container was removed. Contained dragon should remain in the game
            place.dragon = place.dragon.contained_dragon
            Fighter.remove_from(self, place)
        else:
            # default to normal behavior
            Dragon.remove_from(self, place)

    def action(self, colony):
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)
