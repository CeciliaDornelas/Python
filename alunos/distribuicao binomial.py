#distribuição binomial das probabilidades

# numero de ensaios
n = float(input("digite o numero de ensaios (n):"))
# sucessos
x = float(input("digite o numero de sucesso (x):"))
#probablilidade de sucesso em cada ensaio
p = float(input("digite a probabilidade de sucesso em cada ensaio (p):"))
#probabilidade de fracassos
q = 1-p

#fatorial de n e x
nx = n-x
fatn = 1
fatx = 1
fatnx = 1

i= 2
while i <= n:
    fatn = fatn*i
    i = i + 1

i= 2
while i <= x:
   fatx = fatx*i
   i = i + 1 

i=2
while i <= nx:
   fatnx = fatnx*i
   i = i + 1 

#combinação
c = fatn/(fatx*fatnx)

#calculo da formula
P = c * (p ** x) * (q ** nx) 

result= f'A probabilidade de x sucessos em n ensaios é: {P:.4f}'
resp = f'Em porcentagem ficaria: {P*100:.2f} %'
print(result)
print(resp)