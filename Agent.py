import random 

class Agent:
    def __init__(self, posX, posY, env):
        pas = [-1,1]
        self.posX = posX
        self.posY = posY
        self.pasX = pas[random.randint(0,1)]
        self.pasY = pas[random.randint(0,1)]
        self.environnement = env
    
    def voisin(self, taille): 
        #retourne une liste de tuple avec les pos x,y vide 
        """
        [-1][1] |[0][1]   |[1][1]
        [-1][0] |  [A]    |[1][0]
        [-1][-1]| [0][-1]|[1][-1]
        """
        
        possible = []
        voisins = {'deplacement': [], 'agent' : []}
        if not self.environnement.instance.torique:
            possible = [(self.posX-1, self.posY+1),(self.posX, self.posY+1),(self.posX+1, self.posY+1),(self.posX-1, self.posY),(self.posX+1, self.posY),(self.posX-1, self.posY-1),(self.posX, self.posY-1),(self.posX+1, self.posY-1)]
        else:
            
            var = self.posX -1
            var_1 = self.posX + 1
            var_2 = self.posY - 1
            var_3 = self.posY + 1
            if self.posX-1 < 0:
                var = taille - 1
            if self.posX+1 > taille-1:
                var_1 = 0
            if self.posY -1 < 0:
                var_2 = taille - 1
            if self.posY + 1 > taille -1:
                var_3 = 0
            else:
                pass
            
            possible = [(var, var_3),(self.posX, var_3),(var_1, var_3),(var, self.posY),(var_1, self.posY),(var, var_2),(self.posX, var_2),(var_1, var_2)]
        for i in possible :
            x,y = i
            if((x>=0 and x<taille) and (y>=0 and y<taille)):
                if(self.environnement.instance.espace[x][y]==None ):
                    voisins['deplacement'].append((x,y))
                else : 
                    voisins['agent'].append((x,y))
        return voisins
  