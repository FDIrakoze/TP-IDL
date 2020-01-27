from Environnement import Environnement
from Agent import Agent
from Avatar import Avatar
from Hunter import Hunter
import random
class SMA:
    
   
    def __init__(self, taille, torique, nbavatar, avatarBreedTime, nbHunter, hunterBreedTime, hunterStarveTime):
        tab = self.init_tab(taille) 
        self.environnement = Environnement(tab, torique)
        self.taille=taille
        self.avatar = []
        self.hunter = []
        self.agents = []
        self.init_agent(nbavatar,avatarBreedTime, nbHunter,hunterBreedTime, hunterStarveTime, taille)
        

        self.data = {"avatar":[0], 'hunter':[0], "newhunter":[0],"newavatar":[0], "deathHunter":[0], "deathAvatar":[0]}

        
        

    def init_agent(self,nbavatar,avatarBreedTime, nbHunter,hunterBreedTime, hunterStarveTime, taille):
        list_ij = []
        for i in range(taille) : 
            for j in range(taille) :
                list_ij.append((i,j))

        while nbavatar > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))
               
            #if(self.environnement.instance.espace[i][j] == None) : 
            avatar= Avatar(i,j, self.environnement, avatarBreedTime,0)
            self.agents.append(avatar)
            self.environnement.instance.espace[i][j] = avatar        
            nbavatar-=1
        while nbHunter > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))
               
            #if(self.environnement.instance.espace[i][j] == None) : 
            hunter= Hunter(i,j, self.environnement, hunterBreedTime, hunterStarveTime,0)
            self.agents.append(hunter)
            self.environnement.instance.espace[i][j] = hunter        
            nbHunter-=1

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
                if(agent !=None and agent.alive and isinstance(agent,Avatar)):
                    avatar+=1
                elif(agent !=None and agent.alive and isinstance(agent,Hunter)):
                    hunter+=1
                if(agent != None and not agent.alive) : 
                    self.environnement.instance.espace[i][j] = None 
                    continue
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
            prev_color = a.color
            new,death = a.decide(self.taille)
            if(isinstance(a, Avatar)): 
                newAvatar += new
                deathAvatar += death
            if(isinstance(a, Hunter)): 
                newHunter += new
                deathHunter += death
        self.data['newhunter'].append(newHunter)
        self.data['newavatar'].append(newAvatar)
        self.data['deathHunter'].append(deathHunter)
        self.data['deathAvatar'].append(deathAvatar)
           



    

