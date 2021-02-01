print('         calculadora         ')
print('qual operação você deseja?')
print('1 - adição')
print('2 - subitração')
print('3 - divisão')
print('4 - multiplicação')

esc = int(input())

if esc>=1 and esc<=4:
    num1=int(input('digite um numero: '))
    num2=int(input('digite outro numero: '))
    if esc==1:
        total = num1+num2
        print(total)
    if esc==2:
        total = num1-num2
        print(total)
    if esc==3:
        total = num1/num2
        print(total)
    if esc==4:
        total = num1*num2
        print(total)
else:
    print('escolha invalida!')
  