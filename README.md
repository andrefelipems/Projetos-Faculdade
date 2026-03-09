# Projetos-Faculdade
Alguns projetos que fiz durante minha graduação

# Programa 1 - EP 1 PosFixa - Interpretador de Expressões com Números Complexos
Este projeto implementa um interpretador de expressões aritméticas envolvendo números complexos. O programa funciona de forma semelhante ao prompt do Python, lendo expressões digitadas pelo usuário e retornando o resultado calculado.
As expressões aceitas incluem números complexos na forma (a + bi), operadores aritméticos (+, -, *, /), operadores unários e parênteses para controle de precedência. O programa converte a expressão da notação infixa tradicional para notação pós-fixa (Reverse Polish Notation) e então calcula o resultado utilizando uma pilha de operandos.
# Principais conceitos utilizados
# Estruturas de dados:
- Implementação de pilha (stack) para operadores e operandos
# Algoritmos:
- Algoritmo de conversão infixa → pós-fixa
- Avaliação de expressões em notação pós-fixa
# Programação orientada a objetos:
- Classe Complexo para representar números complexos
- Sobrecarga de operadores (+, -, *, /)

# Programa 2- EP2 Sudoku — Solucionador de Sudoku com Backtracking
Este projeto implementa um solucionador automático para o jogo Sudoku. O programa recebe uma matriz parcialmente preenchida e busca todas as soluções possíveis respeitando as regras do jogo.
A solução é encontrada por meio do algoritmo de backtracking, que tenta preencher recursivamente as posições vazias da matriz, retrocedendo quando encontra uma configuração inválida. 
Além disso, o programa também é capaz de gerar tabuleiros iniciais consistentes com um número configurável de posições já preenchidas.
# O programa realiza as seguintes tarefas:
1. Gera um tabuleiro inicial de Sudoku com um número definido de posições preenchidas.
2. Resolve o Sudoku utilizando backtracking.
3. Encontra todas as soluções possíveis para o tabuleiro gerado.
4. Verifica se cada solução encontrada é válida
5. Principais conceitos utilizados
# Algoritmos:
- Backtracking
- Busca recursiva em espaço de estados
# Estruturas de dados:
- Matrizes (listas bidimensionais)
# Outros conceitos:
- Verificação de restrições
- Geração de instâncias aleatórias usando random
- Recursão
- Testes de consistência de estruturas

# Programa 3 - EP3 Classificacao - Classificação de Arquivos com QuickSort e MergeSort
Este projeto implementa um sistema de classificação de registros armazenados em arquivos de texto. Cada registro contém três campos:
identidade, nome, data
O programa lê os registros do arquivo, armazena-os em uma estrutura de dados e permite classificá-los utilizando diferentes critérios de ordenação.
Deve-se utilizar primeiro o gerador.py para criar os arquivos .txt para a utilização do programa principal
Sendo o arquivo compara.py o modulo que defini as opções de comparação de dados para a ordenação
# Principais conceitos utilizados
# Algoritmos clássicos:
- QuickSort(recursivo e não recursivo)
- MergeSort(recursivo e não recursivo)
# Outros conceitos:
- Implementação não recursiva de algoritmos
- Funções de comparação customizadas
- Modularização em múltiplos arquivos
- Manipulação de arquivos
- Parsing de registros
- Conversão e comparação de datas
- Medição de tempo de execução
