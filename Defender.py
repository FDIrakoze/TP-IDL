import random 
from Agent import Agent
class Defender(Agent):
    def __init__(self,  posX, posY, env):
        
        self.color = "blue"
        self.time_to_live = 0
        super(Defender, self).__init__(posX, posY, env)

    def decide(self, taille) : 
       self.time_to_live -= 1