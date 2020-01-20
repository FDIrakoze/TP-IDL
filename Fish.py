import random 
from Agent import Agent
class Fish(Agent):
    def __init__(self, posX, posY, env, breedTime):
        pas = [-1,1]
        self.posX = posX
        self.posY = posY
        self.pasX = pas[random.randint(0,1)]
        self.pasY = pas[random.randint(0,1)]
        self.color = "black"
        self.environnement = env
        self.breedTime = breedTime
        self.initialBreedTime = breedTime
        self.alive = True

    def decide(self, taille) : 
        collision = 0
        self.environnement.instance.espace[self.posX][self.posY] = None 
        nextX = self.posX + self.pasX
        nextY = self.posY + self.pasY
        nextX, nextY = self.next_step(nextX=nextX, nextY=nextY,taille=taille)
        if(self.environnement.instance.espace[nextX][nextY] != None):
            agent2 = self.environnement.instance.espace[nextX][nextY]
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
        
        
        
        old_posX = self.posX
        old_posY = self.posY    
        self.posX = nextX
        self.posY = nextY
        if(self.breedTime == 0): 
            self.environnement.instance.espace[old_posX][old_posY] = Fish(old_posX, old_posY, self.environnement,self.breedTime )
            self.breedTime = self.initialBreedTime
        else :
            self.breedTime -=1

        self.environnement.instance.espace[self.posX][self.posY] = self

        return collision