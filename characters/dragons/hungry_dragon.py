from .dragon import Dragon
import random

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    time_to_digest=3
    food_cost =4
    implemented = True

    def __init__(self, armor=1):
        self.armor=armor
        self.digesting=0

    def eat_terminator(self, terminator):
        terminator.reduce_armor(terminator.armor)

    def action(self, colony):
        if self.digesting%(self.time_to_digest+1)==0:
            if len(self.place.terminators)>0:
                self.eat_terminator(random.choice(self.place.terminators))
                self.digesting=1
        else:
            self.digesting+=1
