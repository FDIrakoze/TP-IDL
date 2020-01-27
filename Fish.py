import random 
from Agent import Agent
class Fish(Agent):
    def __init__(self,  posX, posY, env, breedTime, maturite):
        
        self.color = "green"
        self.breedTime = breedTime
        self.initialBreedTime = breedTime
        self.alive = True
        self.maturite = maturite
        super(Fish, self).__init__(posX, posY, env)

    def decide(self, taille) : 
        newFish = 0
        deathFish=0
        if(self.maturite > 0) : 
            self.color = "yellow"
            self.maturite -= 1
        else :
            self.color = "green"
        if(self.alive):
            voisins = self.voisin(taille)
            deplacement  = voisins['deplacement']
            fish = None
            if(self.breedTime == 0): 
                fish =  Fish(self.posX, self.posY, self.environnement,self.initialBreedTime ,2)
                self.breedTime = self.initialBreedTime
                newFish=1
            else :
                self.breedTime -=1
            
            if(len(deplacement)>0):
                x,y = deplacement[random.randint(0,len(deplacement)-1)]
                self.environnement.instance.espace[self.posX][self.posY] = fish
                self.environnement.instance.espace[x][y] = self
                self.posX = x
                self.posY = y
            
        else :
            deathFish=1
        #self.environnement.instance.espace[self.posX][self.posY] = self

        return (newFish,deathFish)