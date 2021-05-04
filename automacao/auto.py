import pyautogui as pg
import time
import pyperclip as pc

pg.PAUSE = 1

#alerta
pg.alert("nao mexa ate que o programa termine")

#entrar no google chrome
pg.press("win")
pg.write("google chrome")
pg.press("enter")
time.sleep(2)

#digitar o link e entrar
link = "https://drive.google.com/drive/folders/1wRTFw0sUVBjRr4hW5U9LF7DjLixRyxym"
pc.copy(link)
pg.hotkey('ctrl','v')
pg.press("enter")
time.sleep(5)

#baixar tabela
pg.click(1298,412)
pg.click(1658,244)
pg.click(1513,706)
time.sleep(5)

#calcular
import pandas as pd
tabela = pd.read_excel("C:/Users/cecilia/Downloads/Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
qnt_prod = tabela["Quantidade"].sum()
print(faturamento)
print(qnt_prod)

#entrar no gmail
pg.hotkey('ctrl','t')
link = "https://mail.google.com/"
pc.copy(link)
pg.hotkey('ctrl','v')
pg.press("enter")
time.sleep(6)
#escrever
pg.click(127,256)
time.sleep(2)

endereco = "cecidonelas.pb@gmail.com"
pc.copy(endereco)
pg.hotkey('ctrl','v')
pg.press("tab")

assunto = "relatório de vendas"
pc.copy(assunto)
pg.hotkey('ctrl','v')
pg.press("tab")
time.sleep(1)
texto = f""" prezados , boa noite 
o faturamento foi de R${faturamento :,.2f}
a quantidade de produtos foi de {qnt_prod:,.2f}

abs
Cecilia Dornelas"""
pc.copy(texto)
pg.hotkey('ctrl','v')

#enviar
pg.hotkey('ctrl','enter')