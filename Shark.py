import random 
from Agent import Agent
from Fish import Fish
class Shark(Agent):
    def __init__(self, posX, posY, env, breedTime, starveTime, maturite):
        pas = [-1,1]
        self.posX = posX
        self.posY = posY
        self.pasX = pas[random.randint(0,1)]
        self.pasY = pas[random.randint(0,1)]
        self.color = "red"
        self.environnement = env
        self.breedTime = breedTime
        self.initialBreedTime = breedTime
        self.starveTime = starveTime
        self.initialstarveTime = starveTime
        self.maturite = maturite
        self.alive = True

    def canEat(self,voisins):
        fish = []
        for pos in voisins : 
            x,y =pos
            if(isinstance(self.environnement.instance.espace[x][y], Fish)) : 
                fish.append(pos)
        return fish 

    def decide(self, taille) : 
        newShark = 0
        deathShark=0
        if(self.maturite > 0) : 
            self.color = "#ff6781"
            self.maturite -= 1
        else :
            self.color = "red"
        if(self.starveTime == 0):
            self.alive = False
            deathShark=1
        if(self.alive):
            voisins = self.voisin(taille)
            deplacement  = voisins['deplacement']
            fish = self.canEat(voisins['agent'])
            
            shark = None
            
            if((self.starveTime > 0 and self.breedTime > 0 and len(fish)>0) or (self.breedTime <= 0 and self.starveTime > 1 and len(deplacement)==0 and len(fish)>0 ) ) :
                self.starveTime = self.initialstarveTime
                x,y = fish[random.randint(0,len(fish)-1)]
                FishToEat = self.environnement.instance.espace[x][y]
                self.breedTime -=1
                FishToEat.alive=False
                self.environnement.instance.espace[x][y] = self
                self.environnement.instance.espace[self.posX][self.posY] = None
                self.posX = x
                self.posY = y 
            
            elif(self.breedTime <= 0 and self.starveTime > 1 and len(deplacement)>0): 
                x,y = deplacement[random.randint(0,len(deplacement)-1)]
                shark =  Shark(self.posX, self.posY, self.environnement,self.initialBreedTime,self.initialstarveTime,3)
                self.environnement.instance.espace[self.posX][self.posY] = shark
                self.environnement.instance.espace[x][y] = self
                self.breedTime = self.initialBreedTime
                self.starveTime -= 1
                newShark = 1

            elif(len(deplacement)>0):
                x,y = deplacement[random.randint(0,len(deplacement)-1)]
                self.environnement.instance.espace[self.posX][self.posY] = shark
                self.environnement.instance.espace[x][y] = self
                self.posX = x
                self.posY = y
                self.breedTime -=1
                self.starveTime -= 1
            
        
        #self.environnement.instance.espace[self.posX][self.posY] = self

        return (newShark,deathShark)