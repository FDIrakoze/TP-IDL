from Environnement import Environnement
from Agent import Agent
from Avatar import Avatar
from Hunter import Hunter
from Brick import Brick
import random
class SMA:
    
   



    def __init__(self, taille, torique,nbHunter, nbObstacles, v_avatar, v_hunter, time_delay):
        tab = self.init_tab(taille) 
        self.environnement = Environnement(tab, torique)
        self.taille=taille
        self.avatar = None
        
        self.agents = []
        self.init_agent(nbHunter,nbObstacles,  taille)
        self.visite=None
        self.tick_speed = time_delay
        self.avatar_speed = v_avatar
        self.hunter_speed = v_hunter
        self.tour = 0


        
        

    def init_agent(self, nbHunter,nbObstacles, taille):
        list_ij = []
        for i in range(taille) : 
            for j in range(taille) :
                list_ij.append((i,j))

        while nbHunter > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))
               
            #if(self.environnement.instance.espace[i][j] == None) : 
            hunter= Hunter(i,j, self.environnement)
            self.agents.append(hunter)
            self.environnement.instance.espace[i][j] = hunter        
            nbHunter-=1

        while nbObstacles > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))
               
            #if(self.environnement.instance.espace[i][j] == None) : 
            brick= Brick(i,j, self.environnement)
            self.agents.append(brick)
            self.environnement.instance.espace[i][j] = brick        
            nbObstacles-=1

        x,y = list_ij.pop(random.randint(0,len(list_ij)-1))
        self.avatar = Avatar(x, y, self.environnement)
        self.agents.append(self.avatar)
        self.environnement.instance.espace[x][y] = self.avatar

    def init_tab(self,taille):
        tab=[[None for j in range(taille)] for i in range(taille)]
        return tab

    def updateAgents(self) : 
        self.agents=[]
        avatar = 0
        hunter=0
        for i in range(self.taille) : 
            for j in range(self.taille):
                
                agent = self.environnement.instance.espace[i][j]
                if(agent != None):
                    self.agents.append(agent)

    def runOnce(self):
        self.updateAgents()
        self.visite = [[None for i in range(self.taille)] for j in range(self.taille)]
        self.visite[self.avatar.posX][self.avatar.posY] = 0
        self.dijkstra([(self.avatar.posX,self.avatar.posY)])
        
        for a in self.agents :                
            if(isinstance(a, Hunter) and ((self.tour*self.tick_speed) % self.hunter_speed) ==0): 
                isFinish = a.decide(self.taille, self.visite)
                if isFinish : 
                    return True
            elif(isinstance(a, Avatar) and ((self.tour*self.tick_speed) % self.avatar_speed) ==0) :
                 a.decide(self.taille)
                
        self.tour += 1
            
        
           



    
    def sendNextDirection(self, direction): 
        if(self.avatar != None) : 
            self.avatar.saveDirection(direction)

    def dijkstra(self,points) :
        
        next_points = []
        if(len(points)>0): 
            for p in points : 
                x,y = p
                position = [(x-1, y+1),(x, y+1),(x+1, y+1),(x-1, y),(x+1, y),(x-1, y-1),(x, y-1),(x+1, y-1)]
                for i in position :
                    x1,y1 = i
                    if((x1>=0 and x1<self.taille) and (y1>=0 and y1<self.taille)):
                        if(self.visite[x1][y1]==None):
                            self.visite[x1][y1] = self.visite[x][y] + 1
                            next_points.append(i)
        if(len(next_points) >0) : 
            self.dijkstra(next_points)
    

    def printDijkstra(self): 
        for i in self.visite : 
            print(i)
