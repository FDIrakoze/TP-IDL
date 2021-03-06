import random 
from Core.Agent import Agent
class Fish(Agent):
    def __init__(self,  posX, posY, env, breedTime, maturite):
        super(Fish, self).__init__(posX, posY, env)
        if(maturite>0) : 
            self.color="yellow"
        else : 
            self.color = "green"
        self.breedTime = breedTime
        self.initialBreedTime = breedTime
        self.alive = True
        self.maturite = maturite
        

    def decide(self, taille) : 
        newFish = 0
        deathFish=0
        tmp = 0
        if(self.maturite > 0) : 
            self.maturite -= 1
        else :
            self.color = "green"
        if(self.alive):
            voisins = self.voisin(taille)
            deplacement  = voisins['deplacement']
            fish = None
            if(self.breedTime <= 0 and len(deplacement) > 0): 
                fish =  Fish(self.posX, self.posY, self.environnement,self.initialBreedTime ,2)
                self.breedTime = self.initialBreedTime
                newFish=1
            else :
                self.breedTime -=1
            
            if(len(deplacement)>0):
                x,y = deplacement[random.randint(0,len(deplacement)-1)]
                self.environnement.getInstance().espace[self.posX][self.posY] = fish
                self.environnement.getInstance().espace[x][y] = self
                self.posX = x
                self.posY = y
            
        else :
            deathFish=1
        #self.environnement.getInstance().espace[self.posX][self.posY] = self

        return (newFish,deathFish, tmp)
