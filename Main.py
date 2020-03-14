import tkinter as tk    
from tkinter.ttk import *
from PIL import Image, ImageTk

#for employee evaluation
from Evaluate import *
from Rank import *
from Data import*
from important_vars import *


class StartingFrame():
    def __init__(self, top):
        self.top=top
        self.top.geometry(frame_size)
        self.top.configure(background = 'SkyBlue1')

        self.top.title("Child Assessment Tool")

        self.frame=tk.Frame(self.top, bg = 'SkyBlue1')
        self.frame.pack()

        lbl = tk.Label(self.frame, text="Welcome to CATS", font=("Arial Bold", 15), bg='SkyBlue1')
        lbl.pack()

        select = tk.Label(self.frame, text="Hello, my name is Puddles, what is your name?", font=("Comic Sans MS", 15), bg = 'SkyBlue1')
        select.pack()

        txt = tk.Entry(self.frame, width = 10)
        txt.pack()

        #define a function to respond when an option is selected
        def clicked():
            select = tk.Label(self.frame, text="It's nice to meet you " + str(txt.get()), font=("Comic Sans MS", 15), bg = 'SkyBlue1')
            select.pack(side = BOTTOM)

            canvas = Canvas(self.frame, width = 300, height = 300)
            img = Image.open(file = 'CAT.png')
            render = ImageTk.PhotoImage(img)

            image = Label(self, image = render)
            image.pack()
            # canvas.pack()
            
        btn = tk.Button(self.frame, text="Enter", command=clicked)
        btn.pack()
                

    def go2eval(self):
        self.frame.destroy()
        EvaluateEmployeeStartScreen(root)

    def go2rank(self):
        self.frame.destroy()
        RankEmployees(root)
        

#main function
root=tk.Tk()
DT=StartingFrame(root)
root.mainloop()