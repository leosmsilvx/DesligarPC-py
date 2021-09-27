#&/xZ
import os
from tkinter import *
import tkinter as tk

def main():
    win = Tk()

    #Window informations
    win.title("AutoPC")
    win.geometry("400x215+50+50")

    #Texts
    lb = Label(win, text="Welcome to AutoPC\n\n\n\nWhat you want to do?")
    lb.place(x=140, y=30)

    xz = Label(win, text="&/xZ")
    xz.place(x=350, y=193)

    #icons
    #janela.iconbitmap('icon.ico') -- This do not work for all windows so...
    win.iconphoto(True, tk.PhotoImage(file='icon.png'))

    #buttons
    btc = Button(win, width=10, text="Cancel\nShutdown", command=cancel)
    btc.place(x=160, y=150)

    btf = Button(win, width=10, text="Close\nAutoPC", command=win.destroy)
    btf.place(x=300, y=150)

    btd = Button(win, width=10, text="Auto\nShutdown", command=shutdown)
    btd.place(x=20, y=150)

    win.mainloop()

def shutdown():
    #It need to be in "shutdown" cause it need to find "win"
    def ok():
        t = int(ed.get())
        t = str(t*60)
        cmd = 'shutdown -s -f -t ' + (t)
        comandcmd(cmd)
        win.destroy()
        
    win = Tk()
    win.title("AutoPC")
    
    texto = Label(win, text="Shutdown\n\nHow many minutes to shut down?")
    texto.place(x=120, y=15)
    
    win.geometry("425x150+100+100")
    
    ed = Entry(win)
    ed.place(x=150, y=80)
    ed.focus_force()

    bto = Button(win, width=10, text="Confirm", command=ok)
    bto.place(x=100, y=120)

    btf = Button(win, width=10, text="Close Tab", command=win.destroy)
    btf.place(x=250, y=120)

def cancel():
    comandcmd('shutdown -a')
    
    win = Tk()    
    win.title("AutoPC")
    win.geometry("350x90+100+100")
    
    texto = Label(win, text="The auto shutdown has been canceled.")
    texto.place(x=70, y=20)

    btf = Button(win, width=10, text="Ok", command=win.destroy)
    btf.place(x=135, y=50)

def comandcmd(cmd):
    os.system(cmd)


if __name__ == '__main__':
    main()
