from . import Place


class Water(Place):
    """Water is a place that can only hold watersafe fighters."""

    def add_fighter(self, fighter):
        """Adding a Fighter to this place. If the fighter is not watersafe,
        its armor gonna be reduced to 0."""
        super().add_fighter(fighter)
        if not fighter.is_watersafe:
            fighter.reduce_armor(fighter.armor)
