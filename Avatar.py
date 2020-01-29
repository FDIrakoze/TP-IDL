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
        self.visite = [[None for i in range(taille)] for j in range(taille)]
        
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
            self.visite[self.posX][self.posY] = 0
            self.environnement.instance.espace[self.posX][self.posY]=self
            self.dijkstra(taille,[(self.posX, self.posY)])
            
        return (0,0)
    

    def dijkstra(self, taille, points) :
        
        next_points = []
        if(len(points)>0): 
            for p in points : 
                x,y = p
                position = [(x-1, y+1),(x, y+1),(x+1, y+1),(x-1, y),(x+1, y),(x-1, y-1),(x, y-1),(x+1, y-1)]
                for i in position :
                    x1,y1 = i
                    if((x1>=0 and x1<taille) and (y1>=0 and y1<taille)):
                        if(self.visite[x1][y1]==None):
                            self.visite[x1][y1] = self.visite[x][y] + 1
                            next_points.append(i)
        if(len(next_points) >0) : 
            self.dijkstra(taille, next_points)
    

    def printDijkstra(self): 
        for i in self.visite : 
            print(i)


    def setNextDirection(self) : 
        if(len(self.nextDirection) > 0) : 
            self.movement = self.nextDirection.pop(0)

    def saveDirection(self, direction ) : 
        if(direction != self.movement) : 
            self.nextDirection.append(direction)
