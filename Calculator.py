# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:55:01 2021

@author: davis
"""

import math
import tkinter
from tkinter import *
from tkinter import messagebox


root = Tk(className = 'Calculator')
root.geometry('250x400+300+300')

root.resizable(False, False)

data= StringVar()
lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
    bg="#7B7C7C",
    relief=SOLID
)
lbl.pack(expand=True,fill="both",)

val =""
A = 0
operator = ""

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
   global val
   val =val + "2"
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
   
def add_btn_clicked():
    global val
    global operator
    global A
    if type(val)==int():
        A = int(val)
    A = float(val)
    operator = "+"
    val =val + "+"
    data.set(val)
    
def sub_btn_clicked():
    global val
    global operator
    global A
    if type(val)==int():
        A = int(val)
    A = float(val)
    operator = "-"
    val =val + "-"
    data.set(val)
    
def mult_btn_clicked():
    global val
    global operator
    global A
    if type(val)==int():
        A = int(val)
    A = float(val)
    operator = "*"
    val += "*"
    data.set(val)
    
def div_btn_clicked():
    global val
    global operator
    global A
    if type(val)==int():
        A = int(val)
    A = float(val)
    operator = "/"
    val += "/"
    data.set(val)
    
def pow_btn_clicked():
    global val
    global operator
    global A
    if type(val)==int():
        A = int(val)
    A = float(val)
    operator = "^"
    val += "^"
    data.set(val)
    
def pi_btn_clicked():
     global val
     pi = round(math.pi,4)
     val =val + str(pi)
     data.set(val)
     
def decimal_btn_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "."
    val += "."
    data.set(val)

    
def c_btn_clicked():
    global val
    global operator
    global A
    val=""
    A = ""
    operator = ""
    data.set(val)
    

    
def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x=int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val=str(c)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val=str(c)
    elif operator == "*":
        x=float((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val=str(c)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.show("Error","Division by 0 Not Allowed")
            A==""
            val=""
            data.set(val)
        c = round(A / x,3)
        data.set(c)
        val=str(c)
    elif operator == "^":
            x=int((val2.split("^")[1]))
            c = math.pow(A,x)
            data.set(c)
            val=str(c)  
    else:
            c=int(float(A)/x)
            data.set(c)
            val=str(c)

    
    

btn_row1 = Frame(root)
btn_row1.pack(expand=True, fill='both')

btn_row2 = Frame(root)
btn_row2.pack(expand=True, fill="both")

btn_row3 = Frame(root)
btn_row3.pack(expand=True, fill="both")

btn_row4 = Frame(root)
btn_row4.pack(expand=True, fill="both")

btn_row5 = Frame(root)
btn_row5.pack(expand=True, fill="both")



add_btn = Button(
    btn_row1,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text="+",
    font = 200,
    relief=RAISED,
    command = add_btn_clicked
    
    )
add_btn.pack(side=LEFT, expand=True, fill="both")


minus_btn = Button(
    btn_row2,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text="-",
    font = 200,
    relief=RAISED,
    command = sub_btn_clicked
    )

minus_btn.pack(side=LEFT, expand=True, fill="both")

multiply_btn = Button(
    btn_row3,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text="x",
    font = 200,
    relief=RAISED,
    command = mult_btn_clicked
    )
multiply_btn.pack(side=LEFT, expand=True, fill="both")

division_btn = Button(
    btn_row4,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text="/",
    font = 200,
    relief=RAISED,
    command = div_btn_clicked
    )
division_btn.pack(side=LEFT, expand=True, fill="both")

equals_btn = Button(
    btn_row4,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text="=",
    font = 200,
    relief=RAISED,
    command = result
    )
equals_btn.pack(side=LEFT, expand=True, fill="both")

one_btn = Button(
    btn_row1,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="1",
    font = 200,
    relief=RAISED,
    command = btn_1_isclicked
    )
one_btn.pack(side=LEFT, expand=True, fill="both")

two_btn = Button(
    btn_row1,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="2",
    font = 200,
    relief=RAISED,
    command = btn_2_isclicked
    )
two_btn.pack(side=LEFT, expand=True, fill="both")


three_btn = Button(
    btn_row1,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="3",
    font = 200,
    relief=RAISED,
    command = btn_3_isclicked
    )

three_btn.pack(side=LEFT, expand=True, fill="both")


four_btn = Button(
    btn_row2,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="4",
    font = 200,
    relief=RAISED,
    command = btn_4_isclicked
    )
four_btn.pack(side=LEFT, expand=True, fill="both")


five_btn = Button(
    btn_row2,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="5",
    font = 200,
    relief=RAISED,
    command = btn_5_isclicked
    )
five_btn.pack(side=LEFT, expand=True, fill="both")


six_btn = Button(
    btn_row2,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="6",
    font = 200,
    relief=RAISED,
    command = btn_6_isclicked
    )
six_btn.pack(side=LEFT, expand=True, fill="both")


seven_btn = Button(
    btn_row3,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="7",
    font = 200,
    relief=RAISED,
    command = btn_7_isclicked
    )

seven_btn.pack(side=LEFT, expand=True, fill="both")


eight_btn = Button(
    btn_row3,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="8",
    font = 200,
    relief=RAISED,
    command = btn_8_isclicked
    )

eight_btn.pack(side=LEFT, expand=True, fill="both")


nine_btn = Button(
    btn_row3,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="9",
    font = 200,
    relief=RAISED,
    command = btn_9_isclicked
    )
nine_btn.pack(side=LEFT, expand=True, fill="both")


zero_btn = Button(
    btn_row4,
    width = 5,
    height = 2,
    bg = "#567392",
    fg = "white",
    text="0",
    font = 200,
    relief=RAISED,
    command = btn_0_isclicked
    )
zero_btn.pack(side=LEFT, expand=True, fill="both")

c_btn = Button(
    btn_row4,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text = "C",
    font = 200,
    relief=RAISED,
    command = c_btn_clicked
    )
c_btn.pack(side=LEFT,expand=True, fill="both")

pow_btn = Button(
    btn_row5,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text="^",
    font = 200,
    relief=RAISED,
    command = pow_btn_clicked
    )
pow_btn.pack(side=LEFT,expand=True, fill="both")
pi_btn = Button(
    btn_row5,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text="pi",
    font = 200,
    relief=RAISED,
    command = pi_btn_clicked
    )
pi_btn.pack(side=LEFT,expand=True, fill="both")


decimal_btn = Button(
    btn_row5,
    width = 5,
    height = 2,
    bg = "#69A7E9",
    fg = "white",
    text=".",
    font = 200,
    relief=RAISED,
    command = decimal_btn_clicked
    )
decimal_btn.pack(side=LEFT,expand=True, fill="both")
















root.mainloop()


def add(num1,*args):
    total = num1
    for num in args:
        total += num
    return total

def minus(num1, *args):
    sub = num1
    for num in args:
        sub -= num
    return sub


def multp(num1, *args):
    times = num1
    for num in args:
        times *= num
    return times

def division(num1, *args):
    div = num1
    for num in args:
        div /= num
    return div




    