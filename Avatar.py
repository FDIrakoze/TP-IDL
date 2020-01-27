import random 
from Agent import Agent
class Avatar(Agent):
    def __init__(self,  posX, posY, env):
        
        self.color = "green"
        
        super(Avatar, self).__init__(posX, posY, env)

    def decide(self, taille) : 
        

        return (0,0)