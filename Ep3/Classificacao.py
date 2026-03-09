# Ep 3 Classificacao.py
# Autor: Andre Felipe
# NUSP: 10301411
from time import time
from Compara import comp1, comp2, comp3, comp4, data
comps = {
    "1": comp1,
    "2": comp2,
    "3": comp3,
    "4": comp4
}

def LeArquivo(nome):
    TAB = []
    with open(nome, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()       # remove \n
            if linha == "": 
                continue                # ignora linhas vazias
            dados = linha.split(",")    # identidade, nome, data
            if len(dados) != 3:         # ignora linhas com formato invalido
                continue

            TAB.append([dados[0],dados[1],dados[2]])
    return TAB

def ordem(comp):
    if comp == comp1:
        return "Ordem: cresc. por nome - cresc. por data - cresc. por id."
    elif comp == comp2:
        return "Ordem: cresc. por nome - decresc. por data - cresc. por id."
    elif comp == comp3:
        return "Ordem: decresc. por data - cresc. por nome - cresc. por id."
    elif comp == comp4:
        return "Ordem: cresc. por id. - cresc. por data - cresc. por nome"

def particao(TAB, E, D, comp):
    pivo = TAB[D]             # pivô: último elemento
    i = E                      # i serao os menores que o pivô

    # percorre todos os elementos antes do pivô
    for j in range(E, D):      # j vai de L até R-1
        if comp(TAB[j], pivo):    # se TAB[j] vem antes do pivô
            TAB[i], TAB[j] = TAB[j], TAB[i]
            i += 1

    # coloca o pivô na posição final correta
    TAB[i], TAB[D] = TAB[D], TAB[i]
    return i                   # devolve o índice final do pivô

def ClassificaQuick(TAB,comp):
    n = len(TAB)
    if n <= 1:
        return TAB
    
    # pilha com intervalos (E,D)
    pilha = [(0 , n - 1)]

    while pilha:
        E, D = pilha.pop()      # obtém o próximo intervalo
        if E < D:
            p = particao(TAB, E, D, comp)
            esquerda = (E, p - 1)
            direita = (p + 1, D)
            if (esquerda[1] - esquerda[0]) > (direita[1] - direita[0]):
                pilha.append(esquerda)
                pilha.append(direita)
            else:
                pilha.append(direita)
                pilha.append(esquerda)

def ClassificaMerge(TAB,comp):
    n = len(TAB)
    largura = 1
    while largura < n:
        for i in range(0, n, 2 * largura):
            meio = min(i + largura, n)
            fim = min(i + 2 * largura, n)
            esquerda = TAB[i:meio]
            direita = TAB[meio:fim]
            k = i
            j = 0
            l = 0
            while j < len(esquerda) and l < len(direita):
                if comp(esquerda[j], direita[l]):
                    TAB[k] = esquerda[j]
                    j += 1
                else:
                    TAB[k] = direita[l]
                    l += 1
                k += 1
            while j < len(esquerda):
                TAB[k] = esquerda[j]
                j += 1
                k += 1
            while l < len(direita):
                TAB[k] = direita[l]
                l += 1
                k += 1
        largura *= 2

if __name__ == "__main__":
    arq = input("Nome do arquivo de origem:")
    print("")

    # Loop principal
    while True:
        TAB = LeArquivo(arq)

        #Define o metodo de classificacao
        Metodo = input("Quick ou Merge (q ou m)? ")
        if Metodo != "q" and Metodo != "m":
            break
        print("")

        #Define o tipo de comparacao
        Ordem = input("Ordem - comp1a4? ")
        if Ordem not in comps:
            break
        print("")
        comp = comps[Ordem]


        if Metodo == "q":
            inicio = time()
            ClassificaQuick(TAB,comp)
            fim = time()
            t = fim - inicio
            print(f"Tempo do Quick: {t:.6f}")
            
        else:
            inicio = time()
            ClassificaMerge(TAB,comp)
            fim = time()
            t = fim - inicio
            print(f"Tempo do Merge: {t:.6f}")
        
        ordenacao = ordem(comp)
        print("")
        print("100 primeiros registros da tabela:")
        print(ordenacao)
        print("")
        print("Ind    Identidade     Nome                                   Data")
        for i in range(100):
            print(f"{i+1}      {TAB[i][0]}    {TAB[i][1]}         {TAB[i][2]}")
        print("")

    print("*** fim")

