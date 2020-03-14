import tkinter as tk    
from tkinter.ttk import *
from PIL import Image, ImageTk

#holding all the global variables
from Data import*
global img
from urllib.request import urlopen
import io
import base64




class StartingFrame():
    def __init__(self, top):
        self.top=top
        self.top.geometry(frame_size)
        self.top.configure(background = 'SkyBlue1')
        self.top.title("Child Assessment Tool")
        self.frame=tk.Frame(self.top, bg = 'SkyBlue1')
        self.frame.pack()

        lbl = tk.Label(self.frame, text="Welcome Puddle-verse", font=("Arial Bold", 15), bg='SkyBlue1')
        lbl.pack()

        select = tk.Label(self.frame, text="Hello, my name is 'Puddles', what is your name?", font=("Comic Sans MS", 15), bg = 'SkyBlue1')
        select.pack(pady = 20)

        txt = tk.Entry(self.frame, width = 10)
        txt.pack()

        self.name = None
        
        #define a function to respond when an option is selected
        def clicked():

            self.name = txt.get()
            select = tk.Label(self.frame, text="It's nice to meet you, " + str(txt.get()) + '!', font=("Comic Sans MS", 12), bg = 'SkyBlue1')
            select.pack()

            friend = tk.Label(self.frame, text="Will you be friends with me?", font=("Comic Sans MS", 15), bg = 'SkyBlue1')
            friend.pack(pady = 10)

            yes = tk.Button(self.frame, text="YES", font = ('Comic Sans MS', 10), command=Play_Yes, bg = 'White')
            yes.pack(side= tk.TOP) 

            no = tk.Button(self.frame, text="NO", font = ('Comic Sans MS', 10), command=Play_No, bg = 'White')
            no.pack(side = tk.TOP, pady = 5) 

        btn = tk.Button(self.frame, text="Enter", font = ('Comic Sans MS', 10), command=clicked, bg = 'White')
        btn.pack(pady = 5)  


        def Play_Yes():
            self.frame.destroy()
            response = True
            Start_Playing(root, response)

        def Play_No():
            self.frame.destroy()
            response = False
            Start_Playing(root, response)

########################################YES##################################################################
class Start_Playing():
    def __init__(self, top, response):
        self.top=top
        self.top.geometry(frame_size)
        self.top.configure(background = 'SkyBlue2')
        self.top.title("Child Trauma Assessment Tool")
        self.frame=tk.Frame(self.top, bg = 'SkyBlue2')
        self.frame.pack()
        self.response = response
        self.family = ['Mother', 'Father', 'Sister', 'Brother']

        #functions defined 
        def play_game():
            lbl = tk.Label(self.frame, text="I live in a house with my mother and father, \nI have three siblings: Christina, Sally, and Fumi", font=("Comic Sans MS", 15), bg='SkyBlue1')
            lbl.pack(pady = 10)

            #display images:
            lbl_1 = tk.Label(self.frame, text = "Who do you live with?", font=("Comic Sans MS", 15), bg='SkyBlue2')
            lbl_1.pack(pady = 5)


            i = 0
            self.checked = []        
            for mem in self.family:
                    check_state = tk.IntVar()
                    check_state.set(0)
                    self.checked.append(check_state)
                    l = tk.Checkbutton(self.frame, text=str(mem), variable=self.checked[i], bg = 'SkyBlue1')
                    i = i+1
                    l.pack()
            speak_btn = tk.Button(self.frame, text="Tell Puddles!", command= nextpage, bg = 'White')
            speak_btn.pack()

        def nextpage():
            lbl = tk.Label(self.frame, text="My favorite food to eat is fish and chips, what is your favorite food?", font=("Comic Sans MS", 15), bg='SkyBlue1')
            lbl.pack(pady = 10)

            #display images:
            lbl_1 = tk.Label(self.frame, text = "What kind of food do you eat at home?", font=("Comic Sans MS", 15), bg='SkyBlue2')
            lbl_1.pack(pady = 5)

        if not (response):
            lbl = tk.Label(self.frame, text="That's okay, sometimes it's scary for me to meet new people,\n what if we got to know each other a bit better?", font=("Comic Sans MS", 15), bg='SkyBlue2')
            lbl.pack(pady = 10)
            btn = tk.Button(self.frame, text = 'Ok', font = ('Comic Sans MS', 10), command=play_game, bg = 'White')
            btn.pack(pady=5)

        else:
            lbl = tk.Label(self.frame, text="I'm glad that we can be friends, would you like to play with me?", font=("Comic Sans MS", 15), bg='SkyBlue2')
            lbl.pack(pady=10)
            btn = tk.Button(self.frame, text = 'Lets go!', font = ('Comic Sans MS', 10), command=play_game, bg = 'White')
            btn.pack(pady=5)

    
#main function
root=tk.Tk()
DT=StartingFrame(root)
root.mainloop()