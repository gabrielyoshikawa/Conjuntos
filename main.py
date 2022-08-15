#Leitura e print do arquivo txt
import os
lista_arq = []
def LeituraArq(arquivo):
    path = "arquivos/" + arquivo
    global lista_arq
    lista_arq = open(path).read().split("\n")
    print("Arquivo Selecionado:", arquivo)
path = "arquivos/"
dirs = os.listdir(path)
i=0
for file in dirs:
    print(i, "-", file)
    i += 1
x = True
while(x == True):
    opcao = int(input("Selecione o número do arquivo: "))
    try:
        LeituraArq(dirs[opcao])
        x = False
    except:
        print("Número inválido")
#Manipular TXT
def ManipularTXT(var1, var2):
    var1_nocomma = str(var1)
    var1_nocomma = var1_nocomma.replace(",", "")
    var2_nocomma = str(var2)
    var2_nocomma = var2_nocomma.replace(",", "")
    var1_lista = var1_nocomma.split()
    var2_lista = var2_nocomma.split()
    return var1_lista, var2_lista
#Realizar operação
def Uniao(var1_lista, var2_lista):
    uniao_lista = []
    ManipularTXT(var1_lista, var2_lista)
    uniao_lista = var1_lista + ', ' + var2_lista
    aux = uniao_lista.split(", ")
    i = 0
    while i < len(aux):
        j = i + 1
        while j < len(aux):
            if aux[i] == aux[j]:
                del aux[j]
                j += 1
            else:
                j += 1
        i += 1
    print("União: conjunto 1 [{0}], conjunto 2 [{1}], Resultado: {2}".format(var1_lista, var2_lista, aux))
def Intersecao(var1_lista, var2_lista):
    intersecao_lista = []
    ManipularTXT(var1_lista, var2_lista)
    aux_1 = var1_lista.split(", ")
    aux_2 = var2_lista.split(", ")
    for n in aux_1:
        if n in aux_2:
            intersecao_lista.append(n)
    print("Interseção: conjunto 1 [{0}], conjunto 2 [{1}], Resultado: {2}".format(var1_lista, var2_lista, intersecao_lista))
def Diferenca(var1_lista, var2_lista):
    diferenca_lista = []
    ManipularTXT(var1_lista, var2_lista)
    aux_1 = var1_lista.split(", ")
    aux_2 = var2_lista.split(", ")
    i = 0
    while i < len(aux_1):
        j = 0
        while j < len(aux_2):
            if (aux_1[i] == aux_2[j]):
                del aux_2[j]
                j += 1
            else:
                j += 1
        i += 1
    diferenca_lista = aux_1 + aux_2
    print("Diferença: conjunto 1 [{0}], conjunto 2 [{1}], Resultado: {2}".format(var1_lista, var2_lista, diferenca_lista))
def ProdutoCartesiano(var1_lista, var2_lista):
    produtoCartesiano_lista = []
    ManipularTXT(var1_lista, var2_lista)
    aux_1 = var1_lista.split(", ")
    aux_2 = var2_lista.split(", ")
    for x in aux_1:
      for y in aux_2:
        produtoCartesiano_lista.append((x,y))
    print("Produto Cartesiano: conjunto 1 [{0}], conjunto 2 [{1}], Resultado: {2}".format(var1_lista, var2_lista, produtoCartesiano_lista))
#Identificar operação
def Identificador(lista_arq):
    for i in range(1, len(lista_arq), 3):
        var1 = lista_arq[i + 1]
        var2 = lista_arq[i + 2]
        if lista_arq[i] == "U":
            Uniao(var1, var2)
        elif lista_arq[i] == "I":
            Intersecao(var1, var2)
        elif lista_arq[i] == "D":
            Diferenca(var1, var2)
        elif lista_arq[i] == "C":
            ProdutoCartesiano(var1, var2)
Identificador(lista_arq)