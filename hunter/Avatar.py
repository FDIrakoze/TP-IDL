import random 
from Core.Agent import Agent
from Brick import Brick 

from Defender import Defender
from Winner import Winner 
class Avatar(Agent):
    def __init__(self,  posX, posY, env, invincible):
        super(Avatar, self).__init__(posX, posY, env)
        self.color = "green"
        self.movement = None
        self.nextDirection =[]
        self.dijkstra_status=[]
        self.visite=None
        self.defender_eat= 0
        self.invincible = 0
        self.initial_invincible = invincible
        
        

    def decide(self, taille) : 
        self.setNextDirection()
        
        isWin=False
        if(self.movement != None): 
            
            nextX = self.posX
            nextY = self.posY
            if(self.movement == "right"): 
                nextX += 1                
            elif(self.movement == "left"): 
                nextX -= 1
            elif(self.movement == "up"): 
                nextY -= 1
            elif(self.movement == "down"): 
                nextY += 1
            
            if(nextX < 0 or nextX >= taille) : 
                nextX = self.posX
            if(nextY < 0 or nextY >= taille) : 
                nextY = self.posY
            item  = self.environnement.getInstance().espace[nextX][nextY]
           
            if(isinstance(item, Defender)):
                defender = item
                defender.isEat = True 
                self.defender_eat += 1
                self.invincible = self.initial_invincible
            elif(isinstance(self.environnement.getInstance().espace[nextX][nextY], Winner)):
                isWin= True
            elif(item != None) : 
                nextX = self.posX
                nextY = self.posY
            self.environnement.getInstance().espace[self.posX][self.posY]=None
            self.posX = nextX
            self.posY = nextY
            if(self.invincible> 0) : 
                self.invincible -= 1
            self.environnement.getInstance().espace[self.posX][self.posY]=self
            
            
        return isWin

    


    def setNextDirection(self) : 
        if(len(self.nextDirection) > 0) : 
            self.movement = self.nextDirection.pop(0)

    def saveDirection(self, direction ) : 
        if(direction != self.movement) : 
            self.nextDirection.append(direction)
