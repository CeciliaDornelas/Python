import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
#botar titulo na janela
janela.title("minha janelinhaaaa")

#fixa o tamanho da janela
#janela.resizable(False,False)

#inserir texto na janela
ttk.Label(janela, text="vc esta vendo um textinho!").grid(column=0,row=0)
janela.mainloop()
