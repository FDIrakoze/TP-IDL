import random 
class Agent:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.pasX = random.randint(-1,1)
        self.pasY = random.randint(-1,1)
    
    def decide(self):
        #TODO
        pass