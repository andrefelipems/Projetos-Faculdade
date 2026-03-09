from random import randrange
import time
solucoes = 0
tmatriz = 0
tinicial = 0

class TempoExcedido(Exception):
    pass

def GeraMatrizSudoku(npp):
    while True:
        tgerador = time.time()
        if tgerador - tmatriz >= 30:
            return None
        matriz = [9 * [0] for k in range(9)]
        numeros = []
        duplas = []
        for i in range(npp):
            numeros.append(randrange(1, 10))
            while True:
                lin = randrange(0, 9)
                col = randrange(0, 9)
                if (lin, col) not in duplas:
                    duplas.append((lin, col))
                    break
            matriz[lin][col] = numeros[i]
        if TestaMatrizSudoku(matriz):
            return matriz
        
""" 
    # Uma versão recursiva da função que gera a matriz Sudoku
    def GeraMatrizSudoku(npp):
        matriz = [9 * [0] for k in range(9)]
        numeros = []
        duplas = []
        global geradorint
        for i in range(npp):
            numeros.append(randrange(1, 10))
            while True:
                lin = randrange(0, 9)
                col = randrange(0, 9)
                if (lin, col) not in duplas:
                    duplas.append((lin, col))
                    break
            matriz[lin][col] = numeros[i]
        if TestaMatrizSudoku(matriz):
            return matriz
        geradorint += 1
        matriz = GeraMatrizSudoku(npp)
        return matriz """

def Sudoku(Matriz, LinAnt = 0, ColAnt = 0):
    global solucoes
    t0 = time.time()
    if t0 - tinicial >= 30:
        raise TempoExcedido
    vazia = False
    if solucoes >= 20:
        return
    # Procura a proxima posicao vazia
    for i in range(LinAnt, 9):
        for j in range(9):
            if i == LinAnt and j < ColAnt:
                continue
            if Matriz[i][j] == 0:
                LinVazia = i
                ColVazia = j
                vazia = True
                break
        else:
            continue
        break

    # Se nao encontrou posicao vazia, testa para ver se a solução esta correta e imprime
    if not vazia:
        if TestaMatrizSudoku(Matriz):
            solucoes += 1
            print(f"* * * Matriz Completa - Solução {solucoes}")
            for linha in Matriz:
                for num in linha:
                    print(num, end=" ")
                print()
            print("linhas OK * * * * * *")
            print("colunas OK * * * * * *")
            print("quadrados OK * * * * *")
            print("* * * Matriz Completa e Consistente")
            print(" ")

            # Backtracking
            Matriz[LinAnt][ColAnt] = 0
            return
        else:
            Matriz[LinAnt][ColAnt] = 0
            return

    # Obtem os candidatos para a posicao vazia
    if vazia:
        candidatos = Candidatos(Matriz, LinVazia, ColVazia)
        if len(candidatos) == 0:
            return
        for i, candidato in enumerate(candidatos):
            Matriz[LinVazia][ColVazia] = candidato
            Sudoku(Matriz, LinVazia, ColVazia)
            t0 = time.time()
            if solucoes >= 20:
                return
            if t0 - tinicial > 30:
                raise TempoExcedido
            Matriz[LinVazia][ColVazia] = 0
        return

def TestaMatrizSudoku(MatrizSudoku):
    
    # Testa Linhas
    for i in range(9):
        linha = []
        for j in range(9):
            if MatrizSudoku[i][j] != 0:
                if MatrizSudoku[i][j] in linha:
                    return False
                else:
                    linha.append(MatrizSudoku[i][j])


    # Testa Colunas
    for j in range(9):
        coluna = []
        for i in range(9):
            if MatrizSudoku[i][j] != 0:
                if MatrizSudoku[i][j] in coluna:
                    return False
                else:
                    coluna.append(MatrizSudoku[i][j])

    # Testa Quadrados Internos

    for q in range(9):
        quadrado = []
        addlinha =  3 * (q // 3)
        addcoluna = 3 * (q % 3)
        for i in range(3):
            for j in range(3):
                if MatrizSudoku[i + addlinha][j + addcoluna] != 0:
                    if MatrizSudoku[i + addlinha][j + addcoluna] in quadrado:
                        return False
                    else:
                        quadrado.append(MatrizSudoku[i + addlinha][j + addcoluna])

    return True

def Candidatos(Matriz, Linha, Coluna):
    candidatos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Elimina os numeros da linha
    for j in range(9):
        if Matriz[Linha][j] in candidatos:
            candidatos.remove(Matriz[Linha][j])

    # Elimina os numeros da coluna
    for i in range(9):
        if Matriz[i][Coluna] in candidatos:
            candidatos.remove(Matriz[i][Coluna])

    # Elimina os numeros do quadrado
    addlinha =  3 * (Linha // 3)
    addcoluna = 3 * (Coluna // 3)
    for i in range(3):
        for j in range(3):
            if Matriz[i + addlinha][j + addcoluna] in candidatos:
                candidatos.remove(Matriz[i + addlinha][j + addcoluna])

    return candidatos

if __name__ == "__main__":
    while True:
        npp = input("Entre com o número de posições a preencher inicialmente: ")
        if npp == "fim":
            break
        npp = int(npp)
        tmatriz = time.time()
        matriz = GeraMatrizSudoku(npp)
        if matriz is None:
            print("Não foi possível gerar uma matriz válida no tempo esperado.")
            continue
        print("* * * Matriz Inicial")
        for linha in matriz:
            for num in linha:
                print(num, end=" ")
            print()
        print()
        solucoes = 0
        tinicial = time.time()
        try:
            Sudoku(matriz, 0, 0)
        except TempoExcedido:
            print("Tempo limite excedido ao buscar soluções.")
        if solucoes == 0:
            print("Nenhuma solução encontrada")
        elif solucoes >= 20:
            print("* * * Há mais soluções")

        print()