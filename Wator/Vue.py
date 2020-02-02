from tkinter import *
from tkinter import messagebox, IntVar, Checkbutton
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
tab = 1
def init():
    global sma
    global Affich
    global nbTours
    global nbCase
    global time_delay
    global infinite
    global tab
    global taille_canvas
    try:
        infinite = False
        fish = int(nbFish.get())
        nbCase = int(case.get())
        isTorique = int(vTorique.get())
        tab = int(vTab.get())
        time_delay = int(delay.get())
        nbTours = int(tours.get())
        fbreedTime = int(fishBreedTime.get())
        shark = int(nbShark.get())
        sbreedTime = int(sharkBreedTime.get())
        sstarveTime = int(sharkStarveTime.get())
        if(nbTours == 0):
            infinite = True
            nbTours=1
        sma= SMA(nbCase, isTorique, fish, fbreedTime, shark,sbreedTime,sstarveTime)
        taille_canvas =(700 + 700%nbCase)
        Can.config(width=taille_canvas, height=taille_canvas)
        update_grille()
    except ValueError as e:
        print(e)
        messagebox.showinfo("Erreur","Les valeurs saisies contiennent des erreurs")

    
def update_grille():
    global sma
    global taille_canvas
    Can.delete(ALL)
    x0,y0=0//nbCase,0//nbCase
    Case=taille_canvas//nbCase
    if tab:
        for i in range(nbCase+1):
            Can.create_line(x0+Case*i, y0,x0+Case*i,y0 + nbCase*Case)
            Can.create_line(x0, y0+Case*i,x0+nbCase*Case ,y0+Case*i)
    for r in range(nbCase):
        x = x0 + Case * r + Case // 2
        for c in range(nbCase):
            y = y0 + Case * c + Case // 2   
            if sma.environnement.instance.espace[r][c]!=None:
                Affich[(r, c)]= Can.create_oval(x-((taille_canvas//2)//nbCase),y-((taille_canvas//2)//nbCase),x+((taille_canvas//2)//nbCase),y+((taille_canvas//2)//nbCase),fill=sma.environnement.instance.espace[r][c].color)
            else:
                Affich[(r, c)] = Can.create_text(x, y, text='')  

def runOnce(): 
    global sma
    global nbTours
    global infinite
    global time_delay
    global nShark
    global nFish
    sma.runOnce()
    update_grille()
    nShark.set(str(sma.data["shark"][-1]))

    nFish.set(str(sma.data["fish"][-1]))
    if nbTours > 0:
        if not (infinite):
            nbTours-=1
        fenetre.after(time_delay,runOnce)
        

def run():
    runOnce()

def showGraph():
    

    fig, axs = plt.subplots(3 )
    fig.suptitle('fish : green / shark : red')
    axs[0].plot(sma.data["deathFish"], color="green")
    axs[0].plot(sma.data["deathShark"], color="red")
    
   
    axs[0].set_title("Death")

    axs[1].plot(sma.data["newfish"], color="green")
    axs[1].plot(sma.data["newshark"], color="red")
    axs[1].set_title('New')

    axs[2].plot(sma.data["fish"], color="green")
    axs[2].plot(sma.data["shark"], color="red")
    axs[2].set_title('Population')
    plt.xlabel('tick')
    plt.show()
    
    
   
    
       


fenetre = Tk()
fenetre.title("TP1")
frame1=Frame()

frame2=Frame()

vTab= IntVar ()
vTorique= IntVar()
Checkbutton (frame1, text="tableau", variable = vTab).grid(row=5,column=1)
Checkbutton (frame1, text="Torique", variable = vTorique).grid(row=5,column=0)
valeur=Button(frame1,text="valider",command=init)
runButton=Button(frame1,text="Run",command=run)
graph=Button(frame1,text="Show Graph",command=showGraph)
Label(frame1,text= "Veuillez entrer le nombre de fish").grid(row=0,column=0)
Label(frame1,text= "Veuillez entrer le breedTime des fish").grid(row=0,column=2)

Label(frame1,text= "Veuillez entrer le nombre de shark").grid(row=1,column=0)
Label(frame1,text= "Veuillez entrer le breedTime des shark").grid(row=1,column=2)
Label(frame1,text= "Veuillez entrer le starve time des shark").grid(row=1,column=4)

Label(frame1,text= "Veuillez entrer la taille de la grille").grid(row=2,column=0)
Label(frame1,text= "Veuillez entrer le nombre de tours").grid(row=3,column=0)
Label(frame1,text= "Veuillez entrer le delay entre chaque tours (ms)").grid(row=4,column=0)
nbFish=Entry(frame1) 
nbShark=Entry(frame1)
sharkBreedTime=Entry(frame1)
sharkStarveTime=Entry(frame1)
fishBreedTime=Entry(frame1)
case=Entry(frame1)
torique=Entry(frame1)
delay=Entry(frame1)
tours=Entry(frame1)
nbFish.grid(row=0,column=1)
fishBreedTime.grid(row=0, column=3)

nbShark.grid(row=1,column=1)
sharkBreedTime.grid(row=1,column=3)
sharkStarveTime.grid(row=1,column=5)

case.grid(row=2, column=1)
tours.grid(row=3, column=1)
delay.grid(row=4,column=1)
valeur.grid(row=6,column=0)
runButton.grid(row= 6, column= 1)
graph.grid(row= 6, column= 2)



Can=Canvas(fenetre,height=700,width=700,bg="cyan")

Label(frame2,text= "Fish : ").grid(row=0,column=0)
Label(frame2,text= "Shark : ").grid(row=1,column=0)

nShark = StringVar(frame2)
nFish = StringVar(frame2)
Label(frame2,textvariable=nFish).grid(row=0,column=1)
Label(frame2,textvariable=nShark).grid(row=1,column=1)




frame1.pack()
Can.pack()
frame2.pack()
fenetre.resizable(True, True)
fenetre.mainloop()
