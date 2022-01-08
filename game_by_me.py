#import modules
from tkinter import*
import random
from tkinter import messagebox
#Initialising score ,patterns,grid,font_size(p),button_colour,timeleft
score = 0
patterns = [1,2,3,4,5,6]
grid = []
arrows = ['→','←','↑','↓']
for i  in range(5):
    for j in range(5):
        grid.append([i,j])
p = 10
left_key="←"
right_key="→"
up_key="↑"
down_key="↓"
button_colour="darkgrey"
colour = "powderblue"
timeleft = 30
#Defining function to change the difficulty (easy,medium,hard)
def left(event):
    global score
    global timeleft    
    if left_key==arrows[0]:
        score+=1
        if timeleft>0:
            startgame(1)
    else:
        if timeleft>0:
            startgame(1)
def right(event):
    global score
    global timeleft    
    if right_key==arrows[0]:
        score+=1
        if timeleft>0:
            startgame(1)
    else:
        if timeleft>0:
            startgame(1)
def up(event):
    global score
    global timeleft    
    if up_key==arrows[0]:
        score+=1
        if timeleft>0:
            startgame(1)
    else:
        if timeleft>0:
            startgame(1)
def down(event):
    global score
    global timeleft    
    if down_key==arrows[0]:
        score+=1
        if timeleft>0:
            startgame(1)
    else:
        if timeleft>0:
            startgame(1)
    
def change_difficulty(r):
    global patterns
    global grid
    diff_label = Label(root,text = "Difficulty :" +r,bg = colour,padx = 20,font = ('helvetica',14)).grid(row = 0,column = 0,columnspan = 9)
    if r == "Easy":
        patterns = [1]
        grid = [(2,2)]
    if r == "Medium":
        patterns = [1,5,6]
        grid = []
        for i  in range(1,4):
            for j in range(1,4):
              grid.append([i,j])
    if r == "Hard":
        patterns = [1,2,3,4,5,6]
        grid = []
        for i  in range(5):
            for j in range(5):
                grid.append([i,j])
    #settings()
#Defing function to display buttons of difficulty on screen
def difficulty():
    for i  in range(9):
        for j in range(9):
            b1 = Label(root,text = " ",padx = 21,pady = 21,bg = colour).grid(row = i,column = j)
    diff_label = Label(root,text = "Difficulty :Hard",bg = colour,padx = 20,font = ('helvetica',14)).grid(row = 0,column = 0,columnspan = 9)
    b1 = Button(root,text = "Easy",padx = 20,pady = 14,bg = "black",fg = "white",borderwidth = 5,command = lambda : change_difficulty('Easy')).grid(row = 1,column = 0,columnspan = 9)
    b2 = Button(root,text = "Medium",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,command = lambda : change_difficulty('Medium')).grid(row = 2,column = 0,columnspan = 9)
    b3 = Button(root,text = "Hard",padx = 20,pady = 14,bg = "black",fg = "white",borderwidth = 5,command = lambda : change_difficulty('Hard')).grid(row = 3,column = 0,columnspan = 9)
    b10 = Button(root,text = "Back to settings",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,font = ('Helvetica', p),command = settings).grid(row = 5,column = 0,columnspan = 9) 
#Defning the home page

def home_page():
    for i  in range(9):
        for j in range(9):
            b1 = Label(root,text = " ",padx = 21,pady = 21,bg = colour).grid(row = i,column = j)
    l1 = Label(root,text = "LOST IN MIGRATION",bg = colour,font = ('Helvetica', 14))
    l1.grid(row = 0,column = 0,columnspan = 9)
    l2 = Label(root,text = "Each arrow represents a bird .A group of 5 birds are migrating,",bg = colour,font = ('Helvetica', 10))
    l2.grid(row = 1,column = 0,columnspan = 9)
    l3 = Label(root,text = " and unfortunately all the birds except the middle one loses their direction.",bg = colour,font = ('Helvetica', 10))
    l3.grid(row = 2,column = 0,columnspan = 9)
    l4 = Label(root,text = " Help those birds by pointing the direction of middle bird",bg = colour,font = ('Helvetica', 10))
    l4.grid(row = 3,column = 0,columnspan = 9)
    l5 = Label(root,text = " You can provide direction using buttons provided or through keyboard",bg = colour,font = ('Helvetica', 10))
    l5.grid(row = 4,column = 0,columnspan = 9)
    b2 = Button(root,text = "Settings",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,font = ('Helvetica', p),command = settings).grid(row = 5,column = 0,columnspan = 9)
    l = Label(root,text = "Press Enter to start game ",bg = colour,font = ('Helvetica', 14))
    l.grid(row = 6,column = 0,columnspan = 9)
    scoreLabel = Label(root,bg = colour) 
    scoreLabel.grid(row = 7,column = 4,columnspan = 9)

#Defning functin to change background colour
def change_colour(bg):
    global colour
    colour = bg
    
    scoreLabel = Label(root,bg=colour) 
    scoreLabel.grid(row = 7,column = 4,columnspan = 9)
    root.configure(bg = colour)
    for i  in range(9):
        for j in range(9):
            b1 = Label(root,text = " ",padx = 21,pady = 21,bg = colour).grid(row = i,column = j)
    backgroundcolour()

#Display diffrent colours to chose one clour from it
def backgroundcolour():
    for i  in range(9):
        for j in range(9):
            b1 = Label(root,text = " ",padx = 21,pady = 21,bg = colour).grid(row = i,column = j)
    l2 = Label(root,text = "change background colour",padx = 10,pady = 14,bg = colour,borderwidth = 5,font = ('Helvetica', 14)).grid(row = 1,column = 0,columnspan = 9) 
    b1 = Button(root,padx = 10,pady = 14,bg = "red",borderwidth = 5,command = lambda : change_colour("red")).grid(row=3,column=3)
    b2 = Button(root,padx = 10,pady = 14,bg = '#00ffff',borderwidth = 5,command = lambda : change_colour('#00ffff')).grid(row = 3,column = 4)
    b3 = Button(root,padx = 10,pady=14,bg = '#8fff74',borderwidth = 5,command = lambda : change_colour('#8fff74')).grid(row = 3,column = 5)
    b4 = Button(root,padx = 10,pady = 14,bg = '#fff700',borderwidth = 5,command = lambda : change_colour('#fff700')).grid(row = 4,column = 3)
    b5 = Button(root,padx = 10,pady = 14,bg = 'powderblue',borderwidth = 5,command = lambda : change_colour('powderblue')).grid(row = 4,column = 4)
    b6 = Button(root,padx = 10,pady = 14,bg = '#ffe728',borderwidth = 5,command = lambda : change_colour('#ffe728')).grid(row = 4,column = 5)
    b7 = Button(root,padx = 10,pady = 14,bg = '#ffad00',borderwidth = 5,command = lambda : change_colour('#ffad00')).grid(row = 5,column = 3)
    b8 = Button(root,padx = 10,pady = 14,bg = 'White',borderwidth = 5,command = lambda : change_colour('White')).grid(row = 5,column = 4)
    b9 = Button(root,padx = 10,pady = 14,bg = '#35ffb7',borderwidth = 5,command = lambda : change_colour('#35ffb7')).grid(row = 5,column = 5)
    b10 = Button(root,text = "Back to settings",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,font = ('Helvetica', p),command = settings).grid(row = 6,column = 0,columnspan = 9)
#Defing settings button which contain change background colour and  change Difficulty
def settings():
    for i  in range(9):
        for j in range(9):
            b1 = Label(root,text = " ",padx = 21,pady = 21,bg = colour).grid(row = i,column = j)
    b2 = Button(root,text = "change background colour",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,font = ('Helvetica', p),command = backgroundcolour).grid(row = 1,column = 0,columnspan = 9)
    b3 = Button(root,text = "Back to home page",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,font = ('Helvetica', p),command = home_page).grid(row = 5,column = 0,columnspan = 9)
    b4 = Button(root,text = "Difficulty",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,font = ('Helvetica', p),command = difficulty).grid(row = 3,column = 0,columnspan = 9)

#Defining function to grid_shuffle
def grid_shuffle():
    q=random.choice(grid)
    nextpattern(q[0],q[1]) 

#Defining function to compute score
def result(a):
    global score
    global timeleft
    if str(a) == str(arrows[0]):
        score += 1
        if timeleft > 0:
            startgame(1)
    elif str(a)=="x":
        response=messagebox.askyesno("lost in migration","Do you want to play again?")
        if response==1:
            score =0
            timeleft=31
            startgame(1)
        if response ==0:
            root.destroy()
    else:
        if timeleft > 0:
            startgame(1)
#Defining start game function
def startgame(event):
    #To create a blank 9x9 grid
    for i  in range(9):
        for j in range(9):
            b1  = Label(root,text = " ",padx = 21,pady = 21,bg = colour).grid(row = i,column = j)
    global arrows
    arrows = ['→','←','↑','↓']
    random.shuffle(arrows)
    scorcelabel = Label(root,text = "score :"+str(score),bg = colour,font = ('Helvetica', 14)).grid(row = 9,column = 3,columnspan = 3)
    grid_shuffle()
    if timeleft == 30:
        scorcelabel=Label(root,text="score :"+str(score),bg = colour,font = ('Helvetica', 14)).grid(row=9,column=3,columnspan=3)
        b_up=Button(root,text = "↑",padx = 11,pady = 10,bg = button_colour,fg = "white",font = ('Helvetica', 14),command = lambda: result("↑")).grid(row = 11,column = 4)
        b_right = Button(root,text = "→",padx = 7,pady = 10,bg = button_colour,fg = "white",font = ('Helvetica', 14),command = lambda: result("→")).grid(row = 12,column = 5)
        b_centre = Button(root,text = "x",padx = 12,pady = 10,bg = button_colour,fg = "white",font = ('Helvetica', 15),command = lambda: result("x")).grid(row = 12,column = 4)
        b_left = Button(root,text = "←",padx = 7,pady = 10,bg = button_colour,fg = "white",font = ('Helvetica', 14),command = lambda: result("←")).grid(row = 12,column = 3)
        b_down = Button(root,text = "↓",padx = 11,pady = 10,bg = button_colour,fg = "white",font = ('Helvetica', 14),command = lambda: result("↓")).grid(row = 13,column = 4)
    #Call countdown function if timeleft is 30
    if timeleft == 30:
        countdown()
       
#Function to call next pattern on 9x9 grid 
def nextpattern(m,n):
    #Shuffling the patterns to choose the patterns randomly
    b=random.choice(patterns)
    #b = patterns[0]
    #Slant pattern(right slant and left slant)
    if b == 1:
        c = [1,2]
        d = random.choice(c)
        if d == 1:
            for i in range(5):
                for j in range(5):
                    if i == j:
                        if i == 2:
                            b1 = Label(root,text = arrows[0],padx = 10,pady = 10,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+j)
                        else:
                            b1 = Label(root,text = arrows[1],padx = 10,pady = 10,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+j)
        if d == 2:
            for i in range(5):
                for j in range(5):
                    if i == 2:
                        b1 = Label(root,text = arrows[0],padx = 10,pady = 10,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+4-i)
                    else:
                        b1 = Label(root,text = arrows[1],padx = 10,pady = 10,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+4-i)
    #Row pattern
    if b == 2:
        #To randomly choose any row in 5x5 grid
        rows = [0,1,2,3,4]
        random.shuffle(rows)
        for i in range(rows[0],rows[0]+1):
            for j in range(5):
                if j == 2:
                    b1 = Label(root,text = arrows[0],padx = 10,pady = 10 ,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+j)
                else:
                    b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+j)
    #column pattern
    if b == 3:
        #To randomly choose any column in 5x5 grid
        columns = [0,1,2,3,4]
        random.shuffle(columns)
        for i in range(5):
            for j in range(columns[0],columns[0]+1):
                if i == 2:
                     b1 = Label(root ,text = arrows[0],padx = 10,pady = 10,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+j)
                else:
                    b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+i,column = n+j)
    #Triangular pattern
    if b == 4:
        c = [1,2,3,4]
        d = random.choice(c)
        if d == 1:
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+0,column = n+0)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+0,column = n+4)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+1,column = n+1)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+1,column = n+3)
            b1 = Label(root,text = arrows[0],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+2,column = n+2)
        if d == 2:
            b1 = Label(root,text = arrows[0],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+2,column = n+2)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+3,column = n+1)       
            b1 = Label(root,text =arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+3,column = n+3)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+4,column = n+0)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+4,column = n+4)
        if d == 3:
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+0,column = n+0)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+1,column = n+1)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+3,column = n+1)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+4,column = n+0)
            b1 = Label(root,text = arrows[0],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+2,column = n+2)
        if d == 4:
            b1 = Label(root,text = arrows[0],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+2,column = n+2)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+0,column = n+4)       
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+1,column = n+3)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+3,column = n+3)
            b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = m+4,column = n+4)
    #cross(multiplication sign) pattern
    if b == 5:
        r = []
        for i in range(3):
            for j in range(3):
                r.append([i,j])
        s=random.choice(r)
        for x in range(3):
            for y in range(3):
                if x == 1 & y == 1:
                    b1 = Label(root,text = arrows[0],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = s[0]+m+1,column = s[1]+n+1)
                if (x+y)%2 !=0: 
                    b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = s[0]+m+x,column = s[1]+n+y)
    #Cross(Addition sign) pattern
    if b == 6:
        r = []
        for i in range(3):
            for j in range(3):
                r.append([i,j])
        s = random.choice(r)
        for x in range(3):
            for y in range(3):
                if (x + y) % 2 == 0:
                    if x == 1:
                        b1 = Label(root,text = arrows[0],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = s[0]+m+1,column = s[1]+n+1)
                    else:
                        b1 = Label(root,text = arrows[1],padx = 10,pady = 20,bg = colour,font = ('Helvetica', p)).grid(row = s[0]+m+x,column = s[1]+n+y)
# Function to run the timmer
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        c.config(text = "Time left: " + str(timeleft),bg = colour,font = ('Helvetica', 14))
        c.grid(row = 10,column = 3,columnspan = 3)                 
        c.after(1000, countdown)
#To create window
root=Tk()
for i  in range(9):
    for j in range(9):
        b1 = Label(root,text = " ",padx = 21,pady = 21,bg = colour).grid(row = i,column = j)
root.title("Lost In Migration")
root.geometry("442x780")
root.configure(bg = colour)
l1 = Label(root,text = "LOST IN MIGRATION",bg = colour,font = ('Helvetica', 14))
l1.grid(row = 0,column = 0,columnspan = 9)
l2 = Label(root,text = "Each arrow represents a bird .A group of 5 birds are migrating,"
           ,bg = colour,font = ('Helvetica', 10))
l2.grid(row = 1,column = 0,columnspan = 9)
l3 = Label(root,text = " and unfortunately all the birds except the middle one loses their direction.",bg = colour,font = ('Helvetica', 10))
l3.grid(row = 2,column = 0,columnspan = 9)
l4 = Label(root,text = " Help those birds by pointing the direction of middle bird",bg = colour,font = ('Helvetica', 10))
l4.grid(row = 3,column = 0,columnspan = 9)
l5 = Label(root,text = " You can provide direction using buttons provided or through keyboard",bg = colour,font = ('Helvetica', 10))
l5.grid(row = 4,column = 0,columnspan = 9)
b2 = Button(root,text = "Settings",padx = 10,pady = 14,bg = "black",fg = "white",borderwidth = 5,font = ('Helvetica', p),command = settings).grid(row = 5,column = 0,columnspan = 9)
l = Label(root,text = "Press Enter to start game ",bg = colour,font = ('Helvetica', 14))
l.grid(row = 6,column = 0,columnspan = 9)
scoreLabel = Label(root,bg = colour) 
c = Label(root,bg = colour)

root.bind('<Return>', startgame)
root.bind('<Left>',left)
root.bind('<Right>',right)
root.bind('<Up>',up)
root.bind('<Down>',down)
root.mainloop()
