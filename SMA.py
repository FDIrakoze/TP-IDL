from Environnement import Environnement
from Agent import Agent
from Fish import Fish
from Shark import Shark
import random
class SMA:
    
   
    def __init__(self, taille, torique, nbfish, fishBreedTime, nbShark, sharkBreedTime, sharkStarveTime):
        tab = self.init_tab(taille) 
        self.environnement = Environnement(tab, torique)
        self.taille=taille
        self.fish = []
        self.shark = []
        self.agents = []
        self.init_agent(nbfish,fishBreedTime, nbShark,sharkBreedTime, sharkStarveTime, taille)
        

        self.data = {"fish":[0], 'shark':[0], "newshark":[0],"newfish":[0], "deathShark":[0], "deathFish":[0]}

        
        

    def init_agent(self,nbfish,fishBreedTime, nbShark,sharkBreedTime, sharkStarveTime, taille):
        list_ij = []
        for i in range(taille) : 
            for j in range(taille) :
                list_ij.append((i,j))

        while nbfish > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))
               
            #if(self.environnement.instance.espace[i][j] == None) : 
            fish= Fish(i,j, self.environnement, fishBreedTime)
            self.agents.append(fish)
            self.environnement.instance.espace[i][j] = fish        
            nbfish-=1
        while nbShark > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))
               
            #if(self.environnement.instance.espace[i][j] == None) : 
            shark= Shark(i,j, self.environnement, sharkBreedTime, sharkStarveTime)
            self.agents.append(shark)
            self.environnement.instance.espace[i][j] = shark        
            nbShark-=1

    def init_tab(self,taille):
        tab=[[None for j in range(taille)] for i in range(taille)]
        return tab

    def updateAgents(self) : 
        self.agents=[]
        fish = 0
        shark=0
        for i in range(self.taille) : 
            for j in range(self.taille):
                
                agent = self.environnement.instance.espace[i][j]
                if(agent !=None and agent.alive and isinstance(agent,Fish)):
                    fish+=1
                elif(agent !=None and agent.alive and isinstance(agent,Shark)):
                    shark+=1
                if(agent != None and not agent.alive) : 
                    self.environnement.instance.espace[i][j] = None 
                    continue
                if(agent != None):
                    self.agents.append(agent)
        self.data['fish'].append(fish)
        self.data['shark'].append(shark)

    def runOnce(self):
        newFish = 0
        newShark = 0
        deathShark =0
        deathFish=0
        self.updateAgents()
        for a in self.agents :
            prev_color = a.color
            new,death = a.decide(self.taille)
            if(isinstance(a, Fish)): 
                newFish += new
                deathFish += death
            if(isinstance(a, Shark)): 
                newShark += new
                deathShark += death
        self.data['newshark'].append(newShark)
        self.data['newfish'].append(newFish)
        self.data['deathShark'].append(deathShark)
        self.data['deathFish'].append(deathFish)
           



    

