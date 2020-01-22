import random 
from Agent import Agent
class Fish(Agent):
    def __init__(self, posX, posY, env, breedTime):
        pas = [-1,1]
        self.posX = posX
        self.posY = posY
        self.pasX = pas[random.randint(0,1)]
        self.pasY = pas[random.randint(0,1)]
        self.color = "green"
        self.environnement = env
        self.breedTime = breedTime
        self.initialBreedTime = breedTime
        self.alive = True

    def decide(self, taille) : 
        if(self.alive):
            voisins = self.voisin(taille)
            deplacement  = voisins['deplacement']
            fish = None
            if(self.breedTime == 0): 
                fish =  Fish(self.posX, self.posY, self.environnement,self.initialBreedTime )
                self.breedTime = self.initialBreedTime
            else :
                self.breedTime -=1
            
            if(len(deplacement)>0):
                x,y = deplacement[random.randint(0,len(deplacement)-1)]
                self.environnement.instance.espace[self.posX][self.posY] = fish
                self.environnement.instance.espace[x][y] = self
                self.posX = x
                self.posY = y
            else : 
                return 0 
        
        #self.environnement.instance.espace[self.posX][self.posY] = self

        return 0