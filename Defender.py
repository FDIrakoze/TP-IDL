import random 
from Agent import Agent
class Defender(Agent):
    def __init__(self,  posX, posY, env):
        
        self.color = "brown"
        self.time_to_live = 0
        super(Defender, self).__init__(posX, posY, env)

    def decide(self, taille) : 
       return 0,0