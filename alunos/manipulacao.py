with open("C:/Users/cecilia/Desktop/prog/Python/alunos/notas.txt","r") as arquivo:
    print("representação da linha apos strip")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        lista = linha.split(',')
        print(lista)
        contador = linha.count('nota')
        print(contador)
