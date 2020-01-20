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
        self.all_collisions = [0]
        self.nb_color = {'red' : [0] , 'black': [0]}
        
        

    def init_agent(self,nbagent, taille):
        list_ij = []
        for i in range(taille) : 
            for j in range(taille) :
                list_ij.append((i,j))

        while nbagent > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))
               
            #if(self.environnement.instance.espace[i][j] == None) : 
            agent= Agent(i,j, self.environnement)
            self.agents.append(agent)
            self.environnement.instance.espace[i][j] = agent        
            nbagent-=1

    def init_tab(self,taille):
        tab=[[None for j in range(taille)] for i in range(taille)]
        return tab
    def runOnce(self):
        collision = 0
        red = 0
        black = 0
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



    

