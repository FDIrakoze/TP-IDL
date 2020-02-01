from tkinter import *
from tkinter import messagebox, IntVar, Checkbutton
from Brick import Brick
from time import sleep
from SMA import SMA
import random 
sma = None
Affich = dict()
nbTours = 0
nbCase = 0
tab = 1
running = False
def init():
    global sma
    global Affich
    global nbTours
    global nbCase
    global time_delay
    global infinite
    global tab
    global taille_canvas
    global stop_state 

    try:
        infinite = False
        stop_state = False
        nbCase = int(case.get())
        isTorique = int(vTorique.get())
        tab = int(vTab.get())
        time_delay = int(delay.get())
        nbTours = int(tours.get())
        hunter = int(nbHunter.get())
        obstacles = int(nbObstacles.get())
        v_avatar = int(V_avatar.get())
        v_hunter = int(V_hunter.get())

        defenderNb = int(defender_number.get())
        defenderTTL = int(defender_time_to_live.get())
        if(nbTours == 0):
            infinite = True
            nbTours=1
        sma= SMA(nbCase, isTorique, hunter,obstacles, v_avatar, v_hunter, time_delay , defenderNb, defenderTTL)
        dir=["right", "left", "up", "down"]
        sma.sendNextDirection(dir[random.randint(0, len(dir)-1)])
        taille_canvas =(700 + 700%nbCase)
        Can.config(width=taille_canvas, height=taille_canvas)
        Can.focus_set()
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
                if isinstance(sma.environnement.instance.espace[r][c], Brick):
                    Affich[(r, c)]= Can.create_rectangle(x-((taille_canvas//2)//nbCase),y-((taille_canvas//2)//nbCase),x+((taille_canvas//2)//nbCase),y+((taille_canvas//2)//nbCase),fill=sma.environnement.instance.espace[r][c].color)
                else:
                    Affich[(r, c)]= Can.create_oval(x-((taille_canvas//2)//nbCase),y-((taille_canvas//2)//nbCase),x+((taille_canvas//2)//nbCase),y+((taille_canvas//2)//nbCase),fill=sma.environnement.instance.espace[r][c].color)
            else:
                Affich[(r, c)] = Can.create_text(x, y, text='')  

def runOnce(): 
    global sma
    global nbTours
    global infinite
    global time_delay
    global running 

    isFinish = False
    isWin=False
    if not (stop_state) : 
        isFinish = sma.runOnce()
        isWin = sma.isWin
        update_grille()
    
    if nbTours > 0 and not isFinish:
        if not (infinite):
            nbTours-=1
        fenetre.after(time_delay,runOnce)
    if(isFinish): 
        answer  = messagebox.showinfo(title="Looser Window", message="You Damn Looser")
        if(answer == "ok"):
            init()
            running = False
            return
    if(isWin): 
        answer  = messagebox.showinfo(title="Winner", message="You Win !!!")
        
        if(answer == "ok"):
            init()
            running = False
            return

def run():
    global stop_state
    global running
    stop_state = False
    
    fenetre.bind("<KeyPress>", eventKey)
    if not running : 
        running = True
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

def eventKey(event) : 
    global sma 
    key = event.keysym
    if(key == "a") : 
        sma.sendSpeedHunter(0)
        # acceleration Hunter
    elif(key == "z") : 
        sma.sendSpeedHunter(1)
        #decceleration Hunter
    elif(key =="o") :
        sma.sendSpeedAvatar(0)
        # acceleration Avatar
    elif(key =='p') :
        sma.sendSpeedAvatar(1)
        # decceleration Avatar

def stop_process() : 
    global stop_state
    stop_state = True
       

fenetre = Tk()
fenetre.title("TP1")
frame1=Frame()
vTab= IntVar ()
vTorique= IntVar()
Checkbutton (frame1, text="tableau", variable = vTab).grid(row=6,column=1)
Checkbutton (frame1, text="Torique", variable = vTorique).grid(row=6,column=0)
valeur=Button(frame1,text="valider",command=init)
stop_button=Button(frame1,text="Stop",command=stop_process)
runButton=Button(frame1,text="Run",command=run)
Label(frame1,text= "Veuillez entrer le nombre de hunter").grid(row=0,column=0)
Label (frame1, text="Veuillez entrer la vitesse du hunter").grid(row=0, column=2)
Label(frame1,text= "Veuillez entrer le nombre d'obsatcles").grid(row=1,column=0)
Label (frame1, text="Veuillez entrer la vitesse de l'avatar").grid(row=1, column=2)

Label(frame1,text= "Veuillez entrer la taille de la grille").grid(row=2,column=0)

Label(frame1,text= "Veuillez entrer le nombre de defenders ").grid(row=3,column=0)
Label(frame1,text= "Veuillez entrer la durée de vie des defenders").grid(row=3,column=2)
Label(frame1,text= "Veuillez entrer le nombre de tours").grid(row=4,column=0)
Label(frame1,text= "Veuillez entrer le delay entre chaque tours (ms)").grid(row=5,column=0)
 
nbHunter=Entry(frame1)
nbObstacles = Entry(frame1)
V_hunter = Entry(frame1)
V_avatar = Entry(frame1)

case=Entry(frame1)
torique=Entry(frame1)
delay=Entry(frame1)
tours=Entry(frame1)
defender_time_to_live=Entry(frame1)
defender_number=Entry(frame1)


nbHunter.grid(row=0,column=1)
nbObstacles.grid(row= 1, column=1)
V_hunter.grid(row= 0, column=3)
V_avatar.grid(row= 1, column=3)

case.grid(row=2, column=1)
defender_number.grid(row=3, column=1)
defender_time_to_live.grid(row=3, column=3)
tours.grid(row=4, column=1)
delay.grid(row=5,column=1)
valeur.grid(row=7,column=0)
runButton.grid(row= 7, column= 1)
stop_button.grid(row=7, column=2)


Can=Canvas(fenetre,height=700,width=700,bg="white")

fenetre.bind("<Right>", rightKey)
fenetre.bind("<Left>", leftKey)
fenetre.bind("<Up>", upKey)
fenetre.bind("<Down>", downKey)





frame1.pack()
Can.pack()
fenetre.resizable(True, True)
fenetre.mainloop()
