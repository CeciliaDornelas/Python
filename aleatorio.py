from random import randint

num = randint(1,100)
print(num)

esc = num % 2

if esc == 0:
    print('par')
else:
    print('impar')
