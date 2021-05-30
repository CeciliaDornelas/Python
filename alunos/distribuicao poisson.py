#formula da distribuição Poisson

#base do log natural 2.71828
e = 2.71828
try:
    #numero medio de sucessos no intervalo
    lamb = float(input("digite o numero medio de sucessos no intervalo (lambida): "))

    #numero total de sucessos
    x = float(input("digite o numero total de sucessos (X): "))
except ValueError:
    print("\n Observação: vc boto virgula, ele so aceita ponto. bote pra rodar denovo e bote o ponto. \n")

#calculo da probabilidade

#calculo da parte de cima da divisao
calc = (lamb ** x)*(e ** -lamb)

#calcular o fatorial
fat = 1
i = 2
#calculo da parte de baixo da divisao
while i <= x:
    fat = fat*i
    i = i + 1

p = (calc/fat)*100

resp = f"A probabilidade é: {p:.4f}%"
print(resp)