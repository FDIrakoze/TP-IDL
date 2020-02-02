from Core.Environnement import Environnement
from Core.Agent import Agent
from Avatar import Avatar
from Hunter import Hunter
from Brick import Brick
from Defender import Defender
from Winner import Winner
import random
class SMA:
    
   



    def __init__(self, taille, torique,nbHunter, nbObstacles, v_avatar, v_hunter, time_delay, nbDefender, defenderTTL,a_invincible):
        tab = self.init_tab(taille) 
        self.environnement = Environnement(tab, torique)
        self.taille=taille
        self.avatar = None
        
        self.agents = []
        
        self.nbDefender=nbDefender
        self.defenderTTL = defenderTTL
        self.isWin = False 
        self.winnerSpawn = False
        self.init_agent(nbHunter,nbObstacles, nbDefender,  taille, a_invincible)
        self.visite=None
        self.tick_speed = time_delay
        self.avatar_speed = v_avatar
        self.hunter_speed = v_hunter
        self.tour = 0
        self.avatar_incincible = False
        

        
        

    def init_agent(self, nbHunter,nbObstacles, nbDefender, taille,a_invincible):
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
        self.avatar = Avatar(x, y, self.environnement,a_invincible)
        self.agents.append(self.avatar)
        self.environnement.instance.espace[x][y] = self.avatar


        while  nbDefender > 0 :
            if(len(list_ij) == 1 and len(list_ij)==1): 
                i,j = list_ij.pop(0)
            else : 
                i,j= list_ij.pop(random.randint(0,len(list_ij)-1))

            defender= Defender(i,j, self.environnement, self.defenderTTL)
            self.agents.append(defender)
            self.environnement.instance.espace[i][j] = defender        
            nbDefender-=1


    def init_tab(self,taille):
        tab=[[None for j in range(taille)] for i in range(taille)]
        return tab

    def updateAgents(self) : 
        self.agents=[]
        freeSpace=[]
        avatar = 0
        hunter=0
        defender = 0
        spawn_winner = False
        for i in range(self.taille) : 
            for j in range(self.taille):
                agent = self.environnement.instance.espace[i][j]
                if(agent != None):
                    if(isinstance(agent, Defender)):
                        defender += 1
                    if(isinstance(agent, Avatar)) : 
                        spawn_winner = agent.defender_eat == 4
                    self.agents.append(agent)
                else : 
                    freeSpace.append((i,j))
        if(defender == 0) :
            for n in range(self.nbDefender) : 
                x,y = freeSpace.pop(random.randint(0, len(freeSpace)-1))
                new_defender = Defender(x, y, self.environnement, self.defenderTTL)
                self.environnement.instance.espace[x][y] = new_defender
                self.agents.append(new_defender)
        if(spawn_winner == True and not self.winnerSpawn): 
            self.winnerSpawn=True
            x,y = freeSpace.pop(random.randint(0, len(freeSpace)-1))
            winner = Winner(x,y, self.environnement)
            self.environnement.instance.espace[x][y] = winner
            self.agents.append(winner)


    def runOnce(self):
        self.updateAgents()
        self.visite = [[None for i in range(self.taille)] for j in range(self.taille)]
        self.visite[self.avatar.posX][self.avatar.posY] = 0
        self.dijkstra([(self.avatar.posX,self.avatar.posY)])
        
        
        for a in self.agents :             
            if(isinstance(a, Hunter) and ((self.tour) % self.hunter_speed) ==0): 
                isFinish = a.decide(self.taille, self.visite, self.avatar_incincible)
                if isFinish : 
                    return True
            elif(isinstance(a, Avatar) and ((self.tour) % self.avatar_speed) ==0) :
                 self.isWin = a.decide(self.taille)
                 self.avatar_incincible = a.invincible > 0
            elif(isinstance(a, Defender)):
                a.decide()
                
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

    def sendSpeedHunter(self,speed) : 
        if(speed ==  0 and self.hunter_speed > 1) : 
            self.hunter_speed -= 1
        elif(speed == 1) : 
            self.hunter_speed += 1

    def sendSpeedAvatar(self,speed) : 
        if(speed ==  0 and self.avatar_speed > 1) : 
            self.avatar_speed -= 1
        elif(speed == 1) : 
            self.avatar_speed += 1
