import random 
class Agent:
    def __init__(self, posX, posY, env):
        pas = [-1,1]
        self.posX = posX
        self.posY = posY
        self.pasX = random.randint(-1,1)
        self.pasY = random.randint(-1,1)
        self.color = "black"
        self.environnement = env
    
    def decide(self, taille):
        self.environnement.instance.espace[self.posX][self.posY] = None 
        nextX = self.posX + self.pasX
        nextY = self.posY + self.pasY
        if(nextX == taille or nextX < 0 and not self.environnement.instance.torique) : 
            self.pasX = - self.pasX
            nextX = self.posX + self.pasX
        
        if(nextY == taille or nextY < 0 and not self.environnement.instance.torique) : 
            self.pasY = - self.pasY
            nextY = self.posY + self.pasY
        
        if(self.environnement.instance.espace[nextX][nextY] != None):
            self.color = "red"
            agent2 = self.environnement.instance.espace[nextX][nextY]
            agent2.color="red"
            oldX = self.pasX
            oldY = self.pasY

            self.pasX = agent2.pasX
            self.pasY = agent2.pasY


            agent2.pasX = oldX
            agent2.pasY = oldY
        else : 
            
            self.posX += self.pasX
            self.posY += self.pasY
        
        self.environnement.instance.espace[self.posX][self.posY] = self
        pass