import tkinter as tk

botao_config = {
    "bg":"#242742",
    "fg":"#d1d2de",
    "font":("Consolas",12),
    "heigth":"2",
    "width":"9",
    "relief":"9",
    "activebackground":"#313454"
}
class calculadora:
    def __init__ (self,master):
        self.master = master
        self.displayFrame=tk.Frame(self.master)
        self.displayFrame.pack()
        self.buttonsFrame = tk.Frame(self.master)
        self.buttonsFrame.pack()
        
        self.output = tk.Entry(self.displayFrame,width=36,relief="sunken",bd=3,font=("consolas bold",17),fg="#c9c9c5",bg="#242742")
        self.output.grid(row=0,column=0)
        self.criarBotoes()

    def criarBotoes(self):
        self.botoes = [
            ["√","x2","**","(",")","/"],
            ["sin","cos","7","8","9","+"],
            ["sin-1","cos-1","4","5","6","-"],
            ["n!","π",".","0","=","C"],
        ]
        for linha in range(len(self.botoes)):
            for coluna in range(len(self.botoes)):
                self.botoes[linha][coluna]
                texto = self.botoes[linha][coluna]
                b = tk.Button(self.buttonsFrame,botao_config,text=texto)
                b.grid(row=linha,column=coluna) 


raiz = tk.Tk()

calculadora(raiz)

raiz.mainloop()