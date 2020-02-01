import random 
from Agent import Agent
class Winner(Agent):
    def __init__(self,  posX, posY, env):
        
        self.color = "yellow"
        super(Winner, self).__init__(posX, posY, env)

    def decide(self) : 
        pass