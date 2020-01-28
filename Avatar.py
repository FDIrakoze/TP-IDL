import random 
from Agent import Agent
from Brick import Brick 

class Avatar(Agent):
    def __init__(self,  posX, posY, env):
        
        self.color = "green"
        self.movement = None
        self.nextDirection =[]
        self.dijkstra_status=[]
        
        super(Avatar, self).__init__(posX, posY, env)

    def decide(self, taille) : 
        self.setNextDirection()
        self.dijkstra(taille)
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
        return (0,0)
    

    def dijkstra(self, taille) : 
        visite = []
        inc = 1
        visite = [[0 for i in range(taille)] for j in range(taille)]
        visite[self.posX][self.posY]= None
        for i in range(0, taille) :
            for j in range(0, i) : 
                # (x,y); (-x, y); (-x,-y); (x, -y)
                # (y, x); (-y, x); (y, -x); (-y,-x)
                x1 = self.posX - i
                x2 = self.posX + i
                y1 = self.posY - j
                y2 = self.posY + j
                
                if((x1 >= 0 and x1 <  taille) and (y1 >= 0 and y1 <taille)): 
                    visite[x1][y1] = inc
                    visite[y1][x1] = inc

                if((x2 >= 0 and x2 <  taille) and (y2 >= 0 and y2<taille)): 
                    visite[x2][y2] = inc
                    visite[y2][x2] = inc

                if((x1 >= 0 and x1 <  taille) and (y2 >= 0 and y2 <taille)): 
                    visite[x1][y2] = inc
                    visite[y2][x1] = inc
                
                if((x2 >= 0 and x2 <  taille) and (y1 >= 0 and y1 <taille)): 
                    visite[x2][y1] = inc
                    visite[y1][x2] = inc

            inc += 1
        
        self.dijkstra_status = visite
        self.printDijkstra()
        
    
    def printDijkstra(self) : 
        for i in self.dijkstra_status : 
           print(i) 
    def setNextDirection(self) : 
        if(len(self.nextDirection) > 0) : 
            self.movement = self.nextDirection.pop(0)

    def saveDirection(self, direction ) : 
        if(direction != self.movement) : 
            self.nextDirection.append(direction)
