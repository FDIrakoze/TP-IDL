import random 
from Agent import Agent
from Brick import Brick 

class Avatar(Agent):
    def __init__(self,  posX, posY, env):
        
        self.color = "green"
        self.movement = None
        self.nextDirection =[]
        self.dijkstra_status=[]
        self.visite=None
        
        super(Avatar, self).__init__(posX, posY, env)

    def decide(self, taille) : 
        self.setNextDirection()
        
        
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
            if(isinstance( self.environnement.instance.espace[nextX][nextY], Brick)) : 
                nextX = self.posX
                nextY = self.posY
            self.environnement.instance.espace[self.posX][self.posY]=None
            self.posX = nextX
            self.posY = nextY
           
            self.environnement.instance.espace[self.posX][self.posY]=self
            
            
    

    


    def setNextDirection(self) : 
        if(len(self.nextDirection) > 0) : 
            self.movement = self.nextDirection.pop(0)

    def saveDirection(self, direction ) : 
        if(direction != self.movement) : 
            self.nextDirection.append(direction)
