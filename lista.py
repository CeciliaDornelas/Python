frutas = ['maça','uva','banana','morango']
for fruta in frutas:
    minha_fruta = f"nome:{fruta:12} - Numero de letras:{len(fruta):3}"

    print(minha_fruta)

pi = 3.1415
num = f"o numero de PI é :{pi:.1f}"
num_deslocado = f"o numero PI deslocado é:{pi:6.1f}"
num_preciso = f"o numero PI mais preciso é:{pi:.4f}"

print(num)
print(num_deslocado)
print(num_preciso)