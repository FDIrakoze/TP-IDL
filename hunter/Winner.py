import random 
from Core.Agent import Agent
class Winner(Agent):
    def __init__(self,  posX, posY, env):
        super(Winner, self).__init__(posX, posY, env)
        self.color = "yellow"
        

    def decide(self) : 
        pass
