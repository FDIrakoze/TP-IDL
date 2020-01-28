from tkinter import *
from tkinter import messagebox, IntVar, Checkbutton
from time import sleep
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
        nbCase = int(case.get())
        isTorique = int(vTorique.get())
        tab = int(vTab.get())
        time_delay = int(delay.get())
        nbTours = int(tours.get())
        hunter = int(nbHunter.get())
        obstacles = int(nbObstacles.get())
        if(nbTours == 0):
            infinite = True
            nbTours=1
        sma= SMA(nbCase, isTorique, hunter,obstacles)
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
    global nHunter
    global nAvatar
    sma.runOnce()
    update_grille()
    if nbTours > 0:
        if not (infinite):
            nbTours-=1
        fenetre.after(time_delay,runOnce)
        

def run():
    runOnce()
    
def leftKey(event) : 
    global sma 
    sma.sendNextDirection("left")
    #print("Left pressed")

def rightKey(event) : 
    global sma 
    sma.sendNextDirection("right")
    #print("Right pressed")

def downKey(event) : 
    global sma 
    sma.sendNextDirection("down")
    #print("Down pressed")

def upKey(event) : 
    global sma 
    sma.sendNextDirection("up")
    #print("Up pressed")
   
    
       


fenetre = Tk()
fenetre.title("TP1")
frame1=Frame()
vTab= IntVar ()
vTorique= IntVar()
Checkbutton (frame1, text="tableau", variable = vTab).grid(row=5,column=1)
Checkbutton (frame1, text="Torique", variable = vTorique).grid(row=5,column=0)
valeur=Button(frame1,text="valider",command=init)
runButton=Button(frame1,text="Run",command=run)
Label(frame1,text= "Veuillez entrer le nombre de hunter").grid(row=0,column=0)
Label(frame1,text= "Veuillez entrer le nombre d'obsatcles").grid(row=1,column=0)

Label(frame1,text= "Veuillez entrer la taille de la grille").grid(row=2,column=0)
Label(frame1,text= "Veuillez entrer le nombre de tours").grid(row=3,column=0)
Label(frame1,text= "Veuillez entrer le delay entre chaque tours (ms)").grid(row=4,column=0)
 
nbHunter=Entry(frame1)
nbObstacles = Entry(frame1)

case=Entry(frame1)
torique=Entry(frame1)
delay=Entry(frame1)
tours=Entry(frame1)

nbHunter.grid(row=0,column=1)
nbObstacles.grid(row= 1, column=1)

case.grid(row=2, column=1)
tours.grid(row=3, column=1)
delay.grid(row=4,column=1)
valeur.grid(row=6,column=0)
runButton.grid(row= 6, column= 1)



Can=Canvas(fenetre,height=700,width=700,bg="cyan")

fenetre.bind("<Right>", rightKey)
fenetre.bind("<Left>", leftKey)
fenetre.bind("<Up>", upKey)
fenetre.bind("<Down>", downKey)




frame1.pack()
Can.pack()
fenetre.resizable(True, True)
fenetre.mainloop()
