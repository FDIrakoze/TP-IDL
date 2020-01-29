import random 
from Agent import Agent
from Avatar import Avatar
from Brick import Brick 
class Hunter(Agent):
    def __init__(self, posX, posY, env):
        self.color = "red"
        super(Hunter, self).__init__(posX, posY, env)

    

    def decide(self, taille, visite) : 
        position = [(self.posX-1, self.posY+1),(self.posX, self.posY+1),(self.posX+1, self.posY+1),(self.posX-1, self.posY),(self.posX+1, self.posY),(self.posX-1, self.posY-1),(self.posX, self.posY-1),(self.posX+1, self.posY-1)]
        min_pos = []
        for i in position :
            x,y = i
            if((x>=0 and x< taille) and (y>=0 and y< taille)):
                item = self.environnement.instance.espace[x][y]
                if (not (isinstance(item , Brick)) and not isinstance(item, Hunter)):
                    if(isinstance(item , Avatar)): 
                        return True
                    else : 
                        min_pos.append((x,y,visite[x][y]))
        
        nextX = self.posX
        nextY = self.posY
        if(len(min_pos)>0):
            _ , _, m = min(min_pos, key = lambda t : t[2])
            min_pos =  [a for a in min_pos if a[2] == m]
            nextX, nextY, _ = min_pos[random.randint(0, len(min_pos)-1)]

        self.environnement.instance.espace[self.posX][self.posY] = None
        self.posX = nextX
        self.posY = nextY
        self.environnement.instance.espace[self.posX][self.posY] = self
        return False