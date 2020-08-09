from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    food_cost =5
    implemented = True

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Also if the fire_dragon dies, it causes an extra damage on its death
        """
        copy_of_list_of_terminators=self.place.terminators.copy()
        for i in range(len(copy_of_list_of_terminators)):
            copy_of_list_of_terminators[i].reduce_armor(amount)
        self.armor -= amount
        if self.armor <= 0:
            copy_of_list_of_terminators=self.place.terminators.copy()
            for i in range(len(copy_of_list_of_terminators)):
                copy_of_list_of_terminators[i].reduce_armor(amount)
            self.place.remove_fighter(self)
            self.death_callback()
