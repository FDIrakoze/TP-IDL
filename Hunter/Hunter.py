import random 
from Core.Agent import Agent
from Avatar import Avatar
from Brick import Brick 
from Defender import Defender
from Winner import Winner
class Hunter(Agent):
    def __init__(self, posX, posY, env):
        self.color = "red"
        super(Hunter, self).__init__(posX, posY, env)

    

    def decide(self, taille, visite, avatar_invincible) : 
        position = [(self.posX-1, self.posY+1),(self.posX, self.posY+1),(self.posX+1, self.posY+1),(self.posX-1, self.posY),(self.posX+1, self.posY),(self.posX-1, self.posY-1),(self.posX, self.posY-1),(self.posX+1, self.posY-1)]
        min_pos = []
        invincible = False 
        for i in position :
            x,y = i
            if((x>=0 and x< taille) and (y>=0 and y< taille)):
                item = self.environnement.instance.espace[x][y]
                if (not (isinstance(item , Brick)) and not isinstance(item, Hunter)and not isinstance(item, Defender)and not isinstance(item, Winner)):
                    if(isinstance(item , Avatar)): 
                        invincible = item.invincible > 0
                        if not (invincible):
                            return True
                    else : 
                        min_pos.append((x,y,visite[x][y]))
        
        nextX = self.posX
        nextY = self.posY
        if((avatar_invincible or invincible) and len(min_pos)>0) : 
            _ , _, m = max(min_pos, key = lambda t : t[2])
            min_pos =  [a for a in min_pos if a[2] == m]
            nextX, nextY, _ = min_pos[random.randint(0, len(min_pos)-1)]
        elif(not avatar_invincible and len(min_pos)>0):
            _ , _, m = min(min_pos, key = lambda t : t[2])
            min_pos =  [a for a in min_pos if a[2] == m]
            nextX, nextY, _ = min_pos[random.randint(0, len(min_pos)-1)]
        
        self.environnement.instance.espace[self.posX][self.posY] = None
        self.posX = nextX
        self.posY = nextY
        self.environnement.instance.espace[self.posX][self.posY] = self
        return False
    
