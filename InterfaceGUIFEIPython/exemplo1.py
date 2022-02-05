from curses import COLOR_WHITE
import tkinter as tk
from turtle import color


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        #self.nossaTela.title("Primeira Aula")
        
        self.lbl = tk.Label(self.nossaTela, text="Olá Mundo", foreground="white", background="#808080")
        
        self.lbl["font"] = ("Verdana", "18")
        
        self.lbl.pack(pady = 20, side=tk.LEFT, fill=tk.Y)        
    
    
        self.lbl2 = tk.Label(self.nossaTela, text="Olá Mundo", background="white")
        
        self.lbl2["font"] = ("Verdana", "18")
        
        self.lbl2.pack(ipadx = 25, ipady = 10, side=tk.RIGHT)
    
        self.lbl3 = tk.Label(self.nossaTela, text="Terceiro Label", foreground="white", background="#808080")
        
        self.lbl3["font"] = ("Verdana", "18")
        
        self.lbl3.pack(fill = tk.X)  
#Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()
