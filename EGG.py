from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

canvas_width = 800
canvas_height = 400

root =Tk()

root.title("Smash the Egg")

c = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           background="deep sky blue")
c.create_rectangle(-5,canvas_height-100, canvas_width+5, 
                   canvas_height+5, fill="Sea Green", width=0)
c.create_oval(-80,-80, 120, 120, fill='orange', width=0)
c.pack()

color_cycle = cycle(["light blue","light", "light pink", "light yellow", "light cyan"])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty = 0.95
catches_color = "blue"
catcher_height = 100
catcher_width = 100
catcher_startx = canvas_width /2 -catcher_width/2
catcher_starty = canvas_height-catcher_height-20
catcher_startx2 = catcher_startx+catcher_width
catcher_starty2 = catcher_starty+catcher_height
catcher=c.create_ar(catcher_startx, catcher_starty, 
                     catcher_startx2, catcher_starty2,
                     start = 200, extent = 140, style="arc", outline=catcher_color, width = 3)
game_font = font.namefont("TkFixedFont")
game_font.config(size=18)

score = 0
score_text=c.create_create_text(10, 10, anchor="nw",font=game_font,
                                fill="darkblue",text="Score:"+str(score))
live_remaining=3
lives_text=c.create_text(canvas_width-10,10,anchore="ne", font=game_font,fill="darkblue", text="Lives:"+str(live_remaining))

eggs=[]
def create_egg():
  x = randrange(10, 740)
  y = 40
  new_egg=c.create_oval(x, y,x+egg_width, y+egg_height, fil=next(color_cycle),width=-0)
