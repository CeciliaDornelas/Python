import os

#ver se o diretorio existe ou nao
caminho = r"caminho da pasta"

print("----------------")
if os.path.isdir(caminho):
    print("diretorio existe")
else:
    print("diretorio nao existe")
print("----------------")

#listar arquivos do diretorio
print("aquivos listados no diretorio:")

for file in os.listdir(caminho):
    print(file)

#tamanho do arquivo
print("----------------")
   
def tamanho(caminho):
    total = 0
    for caminho_diretorio,nome_diretorio, nome_arquivo in os.walk(caminho):
        for arquivo in nome_arquivo:
            fp = os.path.join(caminho_diretorio, arquivo)
            # pule se for um link simbólico
            if not os.path.islink(fp):
                total += os.path.getsize(fp)

    return total

print(tamanho(caminho), 'bytes')