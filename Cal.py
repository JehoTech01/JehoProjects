import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("450x500+200+200")
root.resizable(0, 0)
root.title("04.05💓Calculator")

val = ""
A = 0
operator = ""

def display_click_click():
    data.set("I miss you, po")

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_dot_isclicked():
    global val
    val = val + "."
    data.set(val)

def btn_plus_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_exp_clicked():
    global A
    global operator, val
    A = float(val)
    operator = "^"
    val = val + "^"
    data.set(val)

def btn_c_pressed():
    global A, operator, val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def btn_x_pressed():
    global A, operator, val
    val = val[:-1]
    data.set(val)

def result():
    display_click_click()

data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
)
lbl.pack(expand=True, fill="both")

btnrow0 = Frame(root)
btnrow0.pack(expand=True, fill="both")

btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

buttons = [
    ("C", btnrow0, btn_c_pressed),
    ("Del", btnrow0, btn_x_pressed),
    ("EXP", btnrow0, btn_exp_clicked),
    ("Sq", btnrow0, result),
    ("1", btnrow1, btn_1_isclicked),
    ("2", btnrow1, btn_2_isclicked),
    ("3", btnrow1, btn_3_isclicked),
    ("+", btnrow1, btn_plus_clicked),
    ("4", btnrow2, btn_4_isclicked),
    ("5", btnrow2, btn_5_isclicked),
    ("6", btnrow2, btn_6_isclicked),
    ("-", btnrow2, btn_minus_clicked),
    ("7", btnrow3, btn_7_isclicked),
    ("8", btnrow3, btn_8_isclicked),
    ("9", btnrow3, btn_9_isclicked),
    ("*", btnrow3, btn_mult_clicked),
    (".", btnrow4, btn_dot_isclicked),
    ("0", btnrow4, btn_0_isclicked),
    ("=", btnrow4, result),
    ("/", btnrow4, btn_div_clicked),
]

for (text, frame, command) in buttons:
    btn = Button(
        frame,
        text=text,
        font=("Verdana", 22),
        bg="#b9ebfa",
        relief=GROOVE,
        border=0,
        command=command,
    )
    btn.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
