import re

class Pilha:
    def __init__(self):
        self.pilha = []

    def __len__(self):
        return len(self.pilha)

    def vazia(self):
        return (len(self.pilha) == 0)

    def empilha(self, item):
        self.pilha.append(item)

    def desempilha(self):
        if not self.vazia():
            return self.pilha.pop()
        else:
            raise IndexError("Pilha vazia")
        
    def topo(self):
        if not self.vazia():
            return self.pilha[-1]
        else:
            raise IndexError("Pilha vazia")
        
    def __str__(self):
        return " ".join(str(item) for item in self.pilha)


class Complexo:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complexo(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complexo(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complexo(self.real * other.real - self.imag * other.imag,
                        self.real * other.imag + self.imag * other.real)
    
    def __truediv__(self, other):
        denominador = other.real**2 + other.imag**2
        return Complexo((self.real * other.real + self.imag * other.imag) / denominador,
                        (self.imag * other.real - self.real * other.imag) / denominador)

    def __neg__(self):
        return Complexo(-self.real, -self.imag)
    
    def __pos__(self):
        return Complexo(+self.real, +self.imag)
    
    def __str__(self):
        return f"({self.real}, {self.imag})"
    
    def __repr__(self):
        return f"({self.real}, {self.imag})"

def TraduzPosFixa(exp):
    t = re.findall(r"(\b\d*[\.]?\d+[i]?\b|[\(\)\+\*\-\/\%])", exp)
    precedencia = {'u#':3, 'u_':3, 'b*':2, 'b/':2, 'b#':1, 'b_':1}
    saida = Pilha()
    temporario = Pilha()
    anterior = None
    real = None
    imaginario = None
    i = 0

    while i < len(t):
        item = t[i]

        # Verifica se há erro de sintaxe ou caracteres inválidos
        if item not in ["(", ")", "+", "-", "*", "/"]:
            if item.replace('.', '', 1).isdigit() == False or (item.endswith("i") and item[:-1].replace('.', '', 1).isdigit() == False):
                print(f"Erro: Erro de Sintaxe ou caractere inválido: ('{item}') na expressão.")
                return None
        # Teste para número complexo com parte real negativa
        if item == "(" and (i + 5) < len(t):
            if (t[i+1] == "-" and
                t[i+2].replace('.', '', 1).isdigit() and
                t[i+3] in ["-", "+"] and
                t[i+4].endswith("i") and
                t[i+5] == ")"):
                
                real = float(t[i+2])
                real = -real
                imaginario = float(t[i+4][:-1])
                if t[i+3] == "-":
                    imaginario = -imaginario
                saida.empilha(Complexo(real, imaginario))
                anterior = "complexo"
                i += 6
                continue
        
        # Teste para número complexo com parte real positiva
        if item == "(" and (i + 4) < len(t):
            if (t[i+1].replace('.', '', 1).isdigit() and
                t[i+2] in ["-", "+"] and
                t[i+3].endswith("i") and
                t[i+4] == ")"):
                
                real = float(t[i+1])
                imaginario = float(t[i+3][:-1])
                if t[i+2] == "-":
                    imaginario = -imaginario
                saida.empilha(Complexo(real, imaginario))
                anterior = "complexo"
                i += 5
                continue

        # Verifica se é um parentese aberto para calcular precendência
        if item == '(':
            temporario.empilha(item)
            anterior = item
            i += 1 
            continue

        # Verifica se é um parentese fechado para desempilhar até o parentese aberto
        if item == ')':
            while not temporario.vazia() and temporario.topo() != '(':
                saida.empilha(temporario.desempilha())
            if not temporario.vazia() and temporario.topo() == '(':
                temporario.desempilha()  # Remove '('
            anterior = item
            i += 1
            continue

        # Verifica se é um operador
        if item in "+-*/":
            if anterior == None or anterior in ['b*', 'b/', 'b#', 'b_', 'u#', 'u_', '(']:
                if item == '+':
                    operador = 'u#'  # Operador unário
                elif item == '-':
                    operador = 'u_'  # Operador unário
            else:
                # Substituição dos símbolos por conveniencia
                if item == '*':
                    operador = 'b*'  # Simbolo para operador multiplicativo binário
                elif item == '/':
                    operador = 'b/'  # Simbolo para operador divisivo binário
                elif item == '+':
                    operador = 'b#'   # Simbolo para operador aditivo binário
                elif item == '-':
                    operador = 'b_'   # Simbolo para operador subtrativo binário

            # Desempilha operadores de maior ou igual precedência
            while (not temporario.vazia() and 
            temporario.topo() != '(' and
            precedencia[temporario.topo()] >= precedencia[operador]):
                saida.empilha(temporario.desempilha())

            # Empilha o operador atual
            temporario.empilha(operador)
            anterior = operador
            i += 1
            continue

    # Desempilha o restante da pilha temporária
    while not temporario.vazia():
        saida.empilha(temporario.desempilha())
        
    # Formata a saída como uma lista
    lista_saida = []
    while not saida.vazia():
        lista_saida.append(saida.desempilha())

    # Inverte a lista para manter a ordem correta
    lista_saida.reverse()
    return lista_saida

def CalcPosFixa(listaexp):
    # Verifica se a lista está vazia (erro de sintaxe na expressão)
    if listaexp is None:
        print("Não foi possível calcular pois a expressão é inválida.")
        return None
    operandos = Pilha() # Pilha para os operandos.
    unarios = Pilha() # Pilha para a possivel exceção.
    for item in listaexp:

        # Empilha os Números Complexos
        if type(item) == Complexo:
            operandos.empilha(item)

        # EXCEÇÃO: Descobri que no caso de entrada começando por unários
        # a lista da notação posfixa começa com o operador unário.
        # Então, para evitar erros vou aplicar os operadores unários
        # que aparecem antes de qualquer operando ao primeiro operando que encontrar.
            while not unarios.vazia():
                operando = operandos.desempilha()
                operador = unarios.desempilha()
                if operador == 'u#':
                    resultado = +operando
                elif operador == 'u_':
                    resultado = -operando
                operandos.empilha(resultado)
            continue

        # Operadores Unários de Exceção
        if item in ['u#', 'u_'] and operandos.vazia():
            unarios.empilha(item)
            continue

        # Operadores Unários Comuns
        elif item in ['u#', 'u_']:
            operando = operandos.desempilha()
            if item == 'u#':
                resultado = +operando
            elif item == 'u_':
                resultado = -operando
            operandos.empilha(resultado)
            continue

        # Operadores Binários
        elif item in ['b*', 'b/', 'b#', 'b_']:
            if len(operandos) < 2:
                print("Erro: Operação inválida. Não há operandos suficientes.")
                return None
            operando2 = operandos.desempilha()
            operando1 = operandos.desempilha()
            if item == 'b#':
                resultado = operando1 + operando2
            elif item == 'b_':
                resultado = operando1 - operando2
            elif item == 'b*':
                resultado = operando1 * operando2
            elif item == 'b/':
                denominador = operando2.real**2 + operando2.imag**2
                if denominador == 0:
                    print("Erro: Divisão por zero.")
                    return None
                resultado = operando1 / operando2
            operandos.empilha(resultado)
            continue

    if len(operandos) == 1:
        resultado_final = operandos.desempilha()
    else:
        print("Erro: Operação inválida. Sobram operandos na pilha.")
        return None

    # Formata a saída, transformando para int se não houver parte fracionária.   
    r_final = resultado_final.real
    i_final = resultado_final.imag
    if r_final == int(r_final):
        r_final = int(r_final)
    else:
        r_final = float(f"{r_final:.5f}")
    if i_final == int(i_final):
        i_final = int(i_final)
    else:
        i_final = float(f"{i_final:.5f}")

    if i_final >= 0:
        print(f"({r_final} + {i_final}i)")
    else:
        print(f"({r_final} - {abs(i_final)}i)")

    return resultado_final


def corrigir_input(exp):
    #Como encontrei alguns caracteres especiais no PDF, vou substituí-los por caracteres normais.
    exp = exp.replace("–", "-")   #Corrigir o EN DASH presente no PDF.
    exp = exp.replace("—", "-")    
    exp = exp.replace("−", "-")   
    exp = exp.replace("\u00A0", " ")
    return exp


if __name__== "__main__":
    while True:
        t = input(">>> ")
        if t.lower() == "fim":
            break
        exp = corrigir_input(t)
        listaexp = TraduzPosFixa(exp)
        CalcPosFixa(listaexp)