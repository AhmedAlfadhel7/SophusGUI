from tkinter import *
from tkinter import ttk

def create_gui_app():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    window.mainloop()

def gui_button():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = ttk.Button()
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Danger():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='red', text="Danger", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Ocean():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='blue', text="Ocean", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Sky():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='skyblue', text="Sky", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Emerald():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='green', text="Emerald", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Rose():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='pink', text="Rose", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Orchid():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='purple', text="Orchid", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Gold():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='gold', text="Gold", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiButton_Tiger():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    button = Button(bg='orange', text="Tiger", foreground='white')
    button.pack(ipadx=5,ipady=5,expand=True)
    window.mainloop()

def guiBg_Red():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="red")
    window.mainloop()

def guiBg_Blue():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="blue")
    window.mainloop()

def guiBg_Yellow():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="yellow")
    window.mainloop()

def guiBg_Green():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="green")
    window.mainloop()

def guiBg_Orange():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="orange")
    window.mainloop()

def guiBg_Pink():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="pink")
    window.mainloop()

def guiBg_Purple():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="purple")
    window.mainloop()

def guiBg_Blank():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="white")
    window.mainloop()

def guiBg_Black():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="black")
    window.mainloop()

def guiBg_Normal():
    window=Tk()
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    window.mainloop()

def guiTitle_Application():
    window=Tk()
    window.title("Application")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    window.mainloop()

def guiTitle_Test():
    window=Tk()
    window.title("Test")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    window.mainloop()

def guiTitle_HelloWorld():
    window=Tk()
    window.title("Hello, World!")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    window.mainloop()

def guiTitle_SophusGUI():
    window=Tk()
    window.title("SophusGUI")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    window.mainloop()

def guiCheckBox_Coding():
    window=Tk()
    window.title("SophusGUI")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    c1 = Checkbutton(window, text='Tkinter', onvalue=1, offvalue=0)
    c1.pack()
    c2 = Checkbutton(window, text='PyQt5',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='PySimpleGUI',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='SophusGUI',onvalue=1, offvalue=0)
    c2.pack()
    window.mainloop()

def guiCheckBox_Languages():
    window=Tk()
    window.title("SophusGUI")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    c1 = Checkbutton(window, text='Arabic', onvalue=1, offvalue=0)
    c1.pack()
    c2 = Checkbutton(window, text='English',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='Spanish',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='Mandarin',onvalue=1, offvalue=0)
    c2.pack()
    window.mainloop()

def guiCheckBox_Countries():
    window=Tk()
    window.title("SophusGUI")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    c1 = Checkbutton(window, text='USA', onvalue=1, offvalue=0)
    c1.pack()
    c2 = Checkbutton(window, text='UK',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='Iraq',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='China',onvalue=1, offvalue=0)
    c2.pack()
    window.mainloop()

def guiCheckBox_Games():
    window=Tk()
    window.title("SophusGUI")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    c1 = Checkbutton(window, text='Minecraft', onvalue=1, offvalue=0)
    c1.pack()
    c2 = Checkbutton(window, text='Fortnite',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='Call Of Duty II',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='FIFA 21',onvalue=1, offvalue=0)
    c2.pack()
    window.mainloop()

def guiCheckBox_PL():
    window=Tk()
    window.title("SophusGUI")
    photo = PhotoImage(file = "SophusGUIlogo.png")
    window.iconphoto(False, photo)
    window.configure(width=900, height=500)
    window.configure(bg="lightgray")
    c1 = Checkbutton(window, text='Python', onvalue=1, offvalue=0)
    c1.pack()
    c2 = Checkbutton(window, text='JS/TS',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='Java',onvalue=1, offvalue=0)
    c2.pack()
    c2 = Checkbutton(window, text='C#',onvalue=1, offvalue=0)
    c2.pack()
    window.mainloop()