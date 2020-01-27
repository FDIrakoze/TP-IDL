import random 
from Agent import Agent
from Avatar import Avatar
class Hunter(Agent):
    def __init__(self, posX, posY, env, breedTime, starveTime, maturite):
        self.color = "red"
        self.breedTime = breedTime
        self.initialBreedTime = breedTime
        self.starveTime = starveTime
        self.initialstarveTime = starveTime
        self.maturite = maturite
        self.alive = True
        super(Hunter, self).__init__(posX, posY, env)

    def canEat(self,voisins):
        avatar = []
        for pos in voisins : 
            x,y =pos
            if(isinstance(self.environnement.instance.espace[x][y], Avatar)) : 
                avatar.append(pos)
        return avatar 

    def decide(self, taille) : 
        newHunter = 0
        deathHunter=0
        if(self.maturite > 0) : 
            self.color = "#ff6781"
            self.maturite -= 1
        else :
            self.color = "red"
        if(self.starveTime == 0):
            self.alive = False
            deathHunter=1
        if(self.alive):
            voisins = self.voisin(taille)
            deplacement  = voisins['deplacement']
            avatar = self.canEat(voisins['agent'])
            
            hunter = None
            
            if((self.starveTime > 0 and self.breedTime > 0 and len(avatar)>0) or (self.breedTime <= 0 and self.starveTime > 1 and len(deplacement)==0 and len(avatar)>0 ) ) :
                self.starveTime = self.initialstarveTime
                x,y = avatar[random.randint(0,len(avatar)-1)]
                AvatarToEat = self.environnement.instance.espace[x][y]
                self.breedTime -=1
                AvatarToEat.alive=False
                self.environnement.instance.espace[x][y] = self
                self.environnement.instance.espace[self.posX][self.posY] = None
                self.posX = x
                self.posY = y 
            
            elif(self.breedTime <= 0 and self.starveTime > 1 and len(deplacement)>0): 
                x,y = deplacement[random.randint(0,len(deplacement)-1)]
                hunter =  Hunter(self.posX, self.posY, self.environnement,self.initialBreedTime,self.initialstarveTime,3)
                self.environnement.instance.espace[self.posX][self.posY] = hunter
                self.environnement.instance.espace[x][y] = self
                self.breedTime = self.initialBreedTime
                self.starveTime -= 1
                newHunter = 1

            elif(len(deplacement)>0):
                x,y = deplacement[random.randint(0,len(deplacement)-1)]
                self.environnement.instance.espace[self.posX][self.posY] = hunter
                self.environnement.instance.espace[x][y] = self
                self.posX = x
                self.posY = y
                self.breedTime -=1
                self.starveTime -= 1
            
        
        #self.environnement.instance.espace[self.posX][self.posY] = self

        return (newHunter,deathHunter)