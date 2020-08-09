from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    food_cost=5
    implemented = True
    blocks_path=False

    def action(self, colony):
        if len(self.place.terminators)>0:
            er=self.place.terminators
            re=er.copy()
            for i in range(len(re)):
                re[i].reduce_armor(self.damage)
