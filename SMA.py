from Environnement import Environnement
from Agent import Agent
from Fish import Fish
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
        self.all_collisions = [0]
        self.nb_color = {'red' : [0] , 'black': [0]}
        
        

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
            agent= Agent(i,j, self.environnement)
            self.agents.append(agent)
            self.environnement.instance.espace[i][j] = agent        
            nbShark-=1

    def init_tab(self,taille):
        tab=[[None for j in range(taille)] for i in range(taille)]
        return tab

    def updateAgents(self) : 
        self.agents=[]
        for i in range(self.taille) : 
            for j in range(self.taille):
                agent = self.environnement.instance.espace[i][j]
                if(agent != None):
                    self.agents.append(agent)

    def runOnce(self):
        collision = 0
        red = 0
        black = 0
        self.updateAgents()
        for a in self.agents :
            prev_color = a.color
            c = a.decide(self.taille) 
            #if(prev_color == "black" and a.color=="red"):
            if(prev_color=="black"):
                black+=1
            elif(prev_color=="red"):
                red+=1

            collision += c
        self.nb_color['black'].append(black)
        self.nb_color['red'].append(red)
        self.all_collisions.append(collision)



    

