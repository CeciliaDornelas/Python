import tkinter as tk
janela = tk.Tk()
mensagem_para_usuario = "mensagem que pode ser util para um user"
msg = tk.Message(janela, text= mensagem_para_usuario)
msg.config(bg='#f5fffa',font=('times',24,'italic'))
msg.pack()
janela.mainloop()