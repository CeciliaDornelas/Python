#menor preço
p1 = float(input(f'primeiro produto R$ '))
p2 = float(input(f'segundo produto R$ '))
p3 = float(input(f'terceiro produto R$'))

if (p1<p2) and (p1<p3):
    print(f'deve comprar o primeiro produto R$ {p1}')
elif (p2<p1) and (p2<p3):
    print(f'deve comprar o segundo produto R$ {p2}')
elif (p3<p1) and (p3<p2):
    print(f'deve comprar o terceiro produto R$ {p3}')
elif (p1<p3) and (p1==p2):
    print(f'deve comprar o primeiro ou o segundo produto R$ {p1}')
elif (p2<p1) and (p2==p3):
    print(f'deve comprar o segundo ou o terceiro produto R$ {p2}')
elif (p1<p2) and (p1==p3):
    print(f'deve comprar o primeiro ou o terceiro produto R$ {p1}')
else:
    print(f'deve comprar qualquer produto R$ {p1}')
