import random 
from Agent import Agent
from Avatar import Avatar
class Hunter(Agent):
    def __init__(self, posX, posY, env):
        self.color = "red"
        super(Hunter, self).__init__(posX, posY, env)

    

    def decide(self, taille) : 
        

        return (0,0)