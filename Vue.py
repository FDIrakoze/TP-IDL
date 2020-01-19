from tkinter import *
from tkinter import messagebox
from SMA import SMA
from time import sleep
def init():
    global sma
    global Affich
    global nbTours
    global nbCase
    stop()
    Affich =dict()
    try:
        nbAgent = int(agent.get())
        nbCase = int(case.get())
        isTorique = int(torique.get())
        nbTours = int(tours.get())
        sma= SMA(nbCase, isTorique, nbAgent)
        update_grille()
    except ValueError:
        messagebox.showinfo("Erreur","Les valeurs saisies contiennent des erreurs")

    
def update_grille():
   
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
                agent =  sma.environnement.instance.espace[r][c]
                color = agent.color
                Affich[(r, c)]= Can.create_oval(x-(250//nbCase),y-(250//nbCase),x+(250//nbCase),y+(250//nbCase),fill=color)
            else:
                Affich[(r, c)] = Can.create_text(x, y, text='')  


def stop ():
    global Arret
    Arret=True

def runOnce(): 
    global Arret
    global nbTours
    sma.runOnce()
    update_grille()
    if nbTours > 0:
        if(Arret):
            return
        nbTours-=1
        fenetre.after(100,runOnce)
        

def run():
    global Arret 
    Arret = False
    runOnce()
    
   
    
       


fenetre = Tk()
fenetre.title("TP1")
frame1=Frame()


valeur=Button(frame1,text="valider",command=init)
runButton=Button(frame1,text="Run",command=run)
Label(frame1,text= "Veuillez entrer le nombre d'agents").grid(row=0,column=0)
Label(frame1,text= "Veuillez entrer la taille de la grille").grid(row=1,column=0)
Label(frame1,text= "Veuillez entrer 0 pour non trorique et 1 pour torique").grid(row=2,column=0)
Label(frame1,text= "Veuillez entrer le nombre de tours").grid(row=3,column=0)
agent=Entry(frame1)
case=Entry(frame1)
torique=Entry(frame1)
tours=Entry(frame1)
agent.grid(row=0,column=1)
case.grid(row=1, column=1)
torique.grid(row=2, column=1)
tours.grid(row=3, column=1)
valeur.grid(row=4,column=1)
runButton.grid(row= 5, column= 1)
Can=Canvas(fenetre,height=650,width=650,bg="white")


frame1.pack()
Can.pack()
fenetre.mainloop()