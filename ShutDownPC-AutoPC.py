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
    win.geometry("400x215+50+50")

    #Texts
    lb = Label(win, text="Welcome to AutoPC\n\n\n\nWhat you want to do?")
    lb.place(x=140, y=30)

    #buttons
    btc = Button(win, width=10, text="Cancel\nShutdown", command=cancel)
    btc.place(x=160, y=150)

    btf = Button(win, width=10, text="Close\nAutoPC", command=win.destroy)
    btf.place(x=300, y=150)

    btd = Button(win, width=10, text="Auto\nShutdown", command=shutdown)
    btd.place(x=20, y=150)

    win.mainloop()

def backup():
    win1 = Tk()

    #Window informations
    win1.title("AutoPC")
    win1.geometry("400x215+50+50")

    #Texts
    lb = Label(win1, text="Welcome to AutoPC\n\n\n\nWhat you want to do?")
    lb.place(x=140, y=30)

    #buttons
    btc = Button(win1, width=10, text="Cancel\nShutdown", command=cancel)
    btc.place(x=160, y=150)

    btf = Button(win1, width=10, text="Close\nAutoPC", command=win1.destroy)
    btf.place(x=300, y=150)

    btd = Button(win1, width=10, text="Auto\nShutdown", command=shutdown)
    btd.place(x=20, y=150)

    win1.mainloop()
    
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
    
    texto = Label(wins, text="Shutdown\n\nHow many minutes to shut down?")
    texto.place(x=120, y=15)
    
    wins.geometry("425x150+100+100")
    
    ed = Entry(wins)
    ed.place(x=150, y=80)
    ed.focus_force()

    bto = Button(wins, width=10, text="Confirm", command=ok)
    bto.place(x=100, y=120)

    btf = Button(wins, width=10, text="Close Tab", command=wins.destroy)
    btf.place(x=250, y=120)

def cancel():
    comandcmd('shutdown -a')
    
    winc = Tk()    
    winc.title("AutoPC")
    winc.geometry("350x90+100+100")
    
    texto = Label(winc, text="The auto shutdown has been canceled.")
    texto.place(x=70, y=20)

    btf = Button(winc, width=10, text="Ok", command=winc.destroy)
    btf.place(x=135, y=50)

def comandcmd(cmd):
    os.system(cmd)

if __name__ == '__main__':
    main()
