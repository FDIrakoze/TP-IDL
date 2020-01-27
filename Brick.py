import random 
from Agent import Agent
class Brick(Agent):
    def __init__(self,  posX, posY, env, breedTime, maturite):
        
        self.color = "brown"
        super(Brick, self).__init__(posX, posY, env)

    def decide(self, taille) : 
       pass