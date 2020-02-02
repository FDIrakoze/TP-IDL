import random 
from Core.Agent import Agent
class Defender(Agent):
    def __init__(self,  posX, posY, env, ttl):
        
        self.color = "blue"
        self.time_to_live = ttl
        self.isEat = False 
        super(Defender, self).__init__(posX, posY, env)

    def decide(self) : 
       if(self.time_to_live <= 0 ): 
           self.environnement.instance.espace[self.posX][self.posY]= None

       elif(self.isEat == False) : 
           self.time_to_live -= 1
