from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):

    name = 'Laser'
    food_cost=10
    implemented = True

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0
        self.damage=2

    def fighters_in_front(self, skynet):
        d={}
        place=self.place
        distance=0
        while(place!=skynet):
            if(place.dragon is not None):
                if isinstance(place.dragon,LaserDragon):
                    pass
                else:
                    d[place.dragon]=distance
            for i in range(len(place.terminators)):
                d[place.terminators[i]]=distance
            distance+=1
            place=place.entrance
        return d

    def calculate_damage(self, distance):
        damage=self.damage-0.2*distance
        self.damage-=0.05
        if(damage<=0):
            return 0
        return damage

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
