from Environnement import Environnement
from Agent import Agent
import random
class SMA:
    def __init__(self, taille, torique, nbagent):
        tab = self.init_tab(taille) 
        self.environnement = Environnement(tab, torique)
        self.agents = []
        self.init_agent(nbagent,taille)
        

    def init_agent(self,nbagent, taille):
        while nbagent > 0 : 
            i = random.randint(0,taille-1)
            j = random.randint(0,taille-1)
            if(self.environnement.instance.espace[i][j] == None) : 
                agent= Agent(i,j)
                self.agents.append(agent)
                self.environnement.instance.espace[i][j] = agent        
                nbagent-=1

    def init_tab(self,taille):
        tab=[[None for j in range(taille)] for i in range(taille)]
        return tab
    def runOnce(self):
        #TODO
        pass



    

