import random 
from Core.Agent import Agent
class Brick(Agent):
    def __init__(self,  posX, posY, env):
        
        self.color = "brown"
        super(Brick, self).__init__(posX, posY, env)

    def decide(self, taille) : 
       return 0,0
