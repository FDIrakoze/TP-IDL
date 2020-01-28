from Environnement import Environnement
from Agent import Agent
from Avatar import Avatar
from Hunter import Hunter
from Brick import Brick
import random
class SMA:
    
   
    def __init__(self, taille, torique,nbHunter, nbObstacles):
        tab = self.init_tab(taille) 
        self.environnement = Environnement(tab, torique)
        self.taille=taille
        self.avatar = None
        self.hunter = []
        self.agents = []
        self.init_agent(nbHunter,nbObstacles,  taille)
        

        self.data = {"avatar":[0], 'hunter':[0], "newhunter":[0],"newavatar":[0], "deathHunter":[0], "deathAvatar":[0]}

        
        

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
            self.agents.append(hunter)
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
        self.data['avatar'].append(avatar)
        self.data['hunter'].append(hunter)

    def runOnce(self):
        newAvatar = 0
        newHunter = 0
        deathHunter =0
        deathAvatar=0
        self.updateAgents()
        for a in self.agents :
            new,death = a.decide(self.taille)
            
        self.data['newhunter'].append(0)
        self.data['newavatar'].append(0)
        self.data['deathHunter'].append(0)
        self.data['deathAvatar'].append(0)
           



    
    def sendNextDirection(self, direction): 
        if(self.avatar != None) : 
            self.avatar.saveDirection(direction)
