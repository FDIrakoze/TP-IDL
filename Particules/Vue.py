from tkinter import *
from tkinter import messagebox
from time import sleep
import matplotlib.pyplot as plt
import sys
from os.path import dirname, abspath, normpath, join
sys.path.insert(0, normpath(abspath(join(dirname(__file__), ".."))))
from SMA import SMA
sma = None
Affich = dict()
nbTours = 0
nbCase = 0
def init():
    global sma
    global Affich
    global nbTours
    global nbCase
    global time_delay
    global infinite
    try:
        infinite = False
        nbAgent = int(agent.get())
        nbCase = int(case.get())
        isTorique = int(torique.get())
        time_delay = int(delay.get())
        nbTours = int(tours.get())
        if(nbTours == 0):
            infinite = True
            nbTours=1
        sma= SMA(nbCase, isTorique, nbAgent)
        update_grille()
    except ValueError as e:
        messagebox.showinfo("Erreur","Les valeurs saisies contiennent des erreurs")

    
def update_grille():
    global sma
    Can.delete(ALL)
    x0,y0=300//nbCase,300//nbCase
    Case=600//nbCase
    for i in range(nbCase+1):
        Can.create_line(x0+Case*i, y0,x0+Case*i,y0 + nbCase*Case)
        Can.create_line(x0, y0+Case*i,x0+nbCase*Case ,y0+Case*i)
    for r in range(nbCase):
        x = x0 + Case * r + Case // 2
        for c in range(nbCase):
            y = y0 + Case * c + Case // 2   
            if sma.environnement.instance.espace[r][c]!=None:
                Affich[(r, c)]= Can.create_oval(x-(250//nbCase),y-(250//nbCase),x+(250//nbCase),y+(250//nbCase),fill=sma.environnement.instance.espace[r][c].color)
            else:
                Affich[(r, c)] = Can.create_text(x, y, text='')  

def runOnce(): 
    global sma
    global nbTours
    global infinite
    global time_delay
    sma.runOnce()
    update_grille()
    if nbTours > 0:
        if not (infinite):
            nbTours-=1
        fenetre.after(time_delay,runOnce)
        

def run():
    runOnce()

def showGraph():
    plt.subplot(211)
    plt.plot(sma.all_collisions)
    plt.xlabel('tick')
    plt.ylabel('collisions')
    
    plt.subplot(212)
    plt.plot(sma.nb_color["black"], color="black")
    plt.plot(sma.nb_color["red"], color="red")
    plt.xlabel('tick')
    plt.ylabel('nb couleurs')
    plt.show()
   
    
       


fenetre = Tk()
fenetre.title("TP1")
frame1=Frame()



valeur=Button(frame1,text="valider",command=init)
runButton=Button(frame1,text="Run",command=run)
graph=Button(frame1,text="Show Graph",command=showGraph)
Label(frame1,text= "Veuillez entrer le nombre d'agents").grid(row=0,column=0)
Label(frame1,text= "Veuillez entrer la taille de la grille").grid(row=1,column=0)
Label(frame1,text= "Veuillez entrer 0 pour non trorique et 1 pour torique").grid(row=2,column=0)
Label(frame1,text= "Veuillez entrer le nombre de tours").grid(row=3,column=0)
Label(frame1,text= "Veuillez entrer le delay entre chaque tours (ms)").grid(row=4,column=0)
agent=Entry(frame1)
case=Entry(frame1)
torique=Entry(frame1)
delay=Entry(frame1)
tours=Entry(frame1)
agent.grid(row=0,column=1)
case.grid(row=1, column=1)
torique.grid(row=2, column=1)
tours.grid(row=3, column=1)
delay.grid(row=4,column=1)
valeur.grid(row=5,column=0)
runButton.grid(row= 5, column= 1)
graph.grid(row= 5, column= 2)
Can=Canvas(fenetre,height=700,width=700,bg="white")


frame1.pack()
Can.pack()
fenetre.resizable(True, True)
fenetre.mainloop()
