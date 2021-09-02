#&/xZ
import os
from tkinter import *

def main():
    
    #Janela
    janela = Tk()
    
    #titulo da janela
    janela.title("Programar Desligamento")

    #texto na janela
    lb = Label(janela, text="BEM VINDO\n\n\n O que deseja fazer?")
    lb.place(x=150, y=30)

    #Botao Desligar
    btd = Button(janela, width=10, text="Desligar", command=desligar)
    btd.place(x=20, y=200)

    #Botao Cancelar
    btc = Button(janela, width=10, text="Cancelar", command=cancelar)
    btc.place(x=160, y=200)

    #Botao Fechar
    btf = Button(janela, width=10, text="Fechar", command=janela.destroy)
    btf.place(x=300, y=200)

    #Tamanho da janela
    janela.geometry("400x250+100+100")

    janela.mainloop()

def desligar():
    def ok():
        t = int(ed.get())
        t = str(t*60)
        cmd = 'shutdown -s -f -t ' + (t)
        comando(cmd)
        janela.destroy()
        
    janela = Tk()
    
    janela.title("Programar Desligamento")
    
    texto = Label(janela, text="Desligar\n\nEm quantos minutos voce deseja desligar sua maquina?")
    texto.place(x=50, y=30)
    
    janela.geometry("425x150+100+100")
    
    ed = Entry(janela)
    ed.place(x=130, y=80)
    ed.focus_force()

    bto = Button(janela, width=10, text="Ok", command=ok)
    bto.place(x=100, y=120)

    btf = Button(janela, width=10, text="Fechar", command=janela.destroy)
    btf.place(x=250, y=120)

def fechar():
    fechar.destroy()
    
def cancelar():
    comando('shutdown -a')

def comando(cmd):
    os.system(cmd)


if __name__ == '__main__':
    main()
