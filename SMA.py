from Environnement import Environnement
from Agent import Agent
import random
class SMA:
    
   
    def __init__(self, taille, torique, nbagent):
        tab = self.init_tab(taille) 
        self.environnement = Environnement(tab, torique)
        self.taille=taille
        self.agents = []
        self.init_agent(nbagent,taille)
        self.all_collisions = []
        
        

    def init_agent(self,nbagent, taille):
        while nbagent > 0 : 
            i = random.randint(0,taille-1)
            j = random.randint(0,taille-1)
            if(self.environnement.instance.espace[i][j] == None) : 
                agent= Agent(i,j, self.environnement)
                self.agents.append(agent)
                self.environnement.instance.espace[i][j] = agent        
                nbagent-=1

    def init_tab(self,taille):
        tab=[[None for j in range(taille)] for i in range(taille)]
        return tab
    def runOnce(self):
        collision = 0
        for a in self.agents :
            prev_color = a.color
            c = a.decide(self.taille) 
            if(prev_color == "black" and a.color=="red"):
                collision += c
            
        self.all_collisions.append(collision)



    

