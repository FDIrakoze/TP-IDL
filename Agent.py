import random 


class Agent:
    def __init__(self, posX, posY, env):
        pas = [-1,1]
        self.posX = posX
        self.posY = posY
        self.pasX = pas[random.randint(0,1)]
        self.pasY = pas[random.randint(0,1)]
        self.color = "black"
        self.environnement = env
    
    def next_step(self, nextX, nextY, taille):
        if(nextX == taille or nextX < 0 and not self.environnement.instance.torique) : 
                self.pasX = - self.pasX
                nextX = self.posX + self.pasX
        
        if(nextY == taille or nextY < 0 and not self.environnement.instance.torique) : 
            self.pasY = - self.pasY
            nextY = self.posY + self.pasY
        if (nextY == taille and self.environnement.instance.torique):
            nextY = nextY % taille
        if(nextY < 0 and self.environnement.instance.torique ):
            nextY = taille - 1
        if (nextX == taille and self.environnement.instance.torique):
            nextX = nextX % taille
        if(nextX < 0 and self.environnement.instance.torique ):
            nextX = taille - 1
        return nextX, nextY

    def voisin(self, taille): 
        #retourne une liste de tuple avec les pos x,y vide 
        """
        [-1][1] |[0][1]   |[1][1]
        [-1][0] |  [A]    |[1][0]
        [-1][-1]| [0][-1]|[1][-1]
        """
        possible = [(self.posX-1, self.posY+1),(self.posX, self.posY+1),(self.posX+1, self.posY+1),(self.posX-1, self.posY),(self.posX+1, self.posY),(self.posX-1, self.posY-1),(self.posX, self.posY-1),(self.posX+1, self.posY-1)]
        voisins = []
        for i in possible :
            x,y = i
            if((x>=0 and x<taille) and (y>=0 and y<taille)):
                if(self.environnement[x][y]):
                    voisins.append((x,y))
        return voisins
    def decide(self, taille):
        collision = 0
        self.environnement.instance.espace[self.posX][self.posY] = None 
        nextX = self.posX + self.pasX
        nextY = self.posY + self.pasY
        nextX, nextY = self.next_step(nextX=nextX, nextY=nextY,taille=taille)
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
            nextX = self.posX + self.pasX
            nextY = self.posY + self.pasY
            nextX, nextY = self.next_step(nextX=nextX, nextY=nextY,taille=taille)
            collision = 1
            
        
            
        self.posX = nextX
        self.posY = nextY
        
        self.environnement.instance.espace[self.posX][self.posY] = self
        return collision
        