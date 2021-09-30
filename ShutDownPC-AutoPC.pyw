#&/xZ
import os
from tkinter import *
import tkinter as tk

def main():
    win = Tk()
    try:
        win.iconphoto(True, tk.PhotoImage(file='icon.png'))
    except:
        win.destroy()
        win = Tk()

    #Window informations
    win.title("AutoPC")
    win.geometry("400x215")
    canvas = tk.Canvas(win, height=1000, width=1000, bg="#4f4f4f")
    canvas.pack()

    #Texts
    lb = Label(win, text="Welcome to AutoPC\n\n\n\nWhat you want to do?", bg="#4f4f4f", fg="#eee")
    lb.place(x=140, y=30)

    #buttons
    btc = Button(win, width=10, text="Cancel\nShutdown", command=cancel, bg="#707070", fg="#eee")
    btc.place(x=160, y=150)

    btf = Button(win, width=10, text="Close\nAutoPC", command=win.destroy, bg="#707070", fg="#eee")
    btf.place(x=300, y=150)

    btd = Button(win, width=10, text="Auto\nShutdown", command=shutdown, bg="#707070", fg="#eee")
    btd.place(x=20, y=150)

    win.mainloop()
   
def shutdown():
    #It need to be in "shutdown" cause it need to find "win"
    def ok():
        t = int(ed.get())
        t = str(t*60)
        cmd = 'shutdown -s -f -t ' + (t)
        comandcmd(cmd)
        wins.destroy()
        
    wins = Tk()
    wins.title("AutoPC")

    canvas = tk.Canvas(wins, height=1000, width=1000, bg="#4f4f4f")
    canvas.pack()
    
    texto = Label(wins, text="Shutdown\n\nHow many minutes to shut down?", bg="#4f4f4f",  fg="#eee")
    texto.place(x=120, y=15)
    
    wins.geometry("425x150+100+100")
    
    ed = Entry(wins,bg="#707070", fg="#eee")
    ed.place(x=150, y=80)
    ed.focus_force()

    bto = Button(wins, width=10, text="Confirm", command=ok, bg="#707070", fg="#eee")
    bto.place(x=100, y=120)

    btf = Button(wins, width=10, text="Close Tab", command=wins.destroy, bg="#707070", fg="#eee")
    btf.place(x=250, y=120)

def cancel():
    comandcmd('shutdown -a')
    
    winc = Tk()    
    winc.title("AutoPC")
    winc.geometry("350x90+100+100")

    canvas = tk.Canvas(winc, height=1000, width=1000, bg="#4f4f4f")
    canvas.pack()
    
    texto = Label(winc, text="The auto shutdown has been canceled.", bg="#4f4f4f", fg="#eee")
    texto.place(x=70, y=20)

    btf = Button(winc, width=10, text="Ok", command=winc.destroy, bg="#707070", fg="#eee")
    btf.place(x=135, y=50)

def comandcmd(cmd):
    os.system(cmd)

if __name__ == '__main__':
    main()
