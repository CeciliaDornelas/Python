ganhohr = float(input("quanto vc ganha por hr ?"))
numhrmes = int(input("numero de hrs trabalhadas no mês :"))
#input(f'')
salbruto = float(ganhohr*numhrmes)
ir = float(salbruto*0.11)
inss = float(salbruto*0.08)
sindicato = float(salbruto*0.05)

desconto = inss + ir + sindicato

salliquido = salbruto - desconto

print("salario bruto: R$",salbruto)
print("IR(11%): ",ir)
print("sindicato (5%): ",sindicato)
print("salario liquido: ", salliquido)
#print(f'salario bruto: R$ {salbruto}')