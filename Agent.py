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
    
    def voisin(self, taille): 
        #retourne une liste de tuple avec les pos x,y vide 
        """
        [-1][1] |[0][1]   |[1][1]
        [-1][0] |  [A]    |[1][0]
        [-1][-1]| [0][-1]|[1][-1]
        """
        possible = [(self.posX-1, self.posY+1),(self.posX, self.posY+1),(self.posX+1, self.posY+1),(self.posX-1, self.posY),(self.posX+1, self.posY),(self.posX-1, self.posY-1),(self.posX, self.posY-1),(self.posX+1, self.posY-1)]
        voisins = {'deplacement': [], 'agent' : []}
        
        for i in possible :
            x,y = i
            if((x>=0 and x<taille) and (y>=0 and y<taille)):
                if(self.environnement.instance.espace[x][y]==None):
                    voisins['deplacement'].append((x,y))
                else : 
                    voisins['agent'].append((x,y))
        return voisins
  