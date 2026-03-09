# modulo compara.py

def data(x):
    # Converte a data para comparacao
    d, m, a = x.split('/')
    return (int(a), int(m), int(d))

def comp1(a,b):
    # ordem crescente de nome
    #   se os nomes forem iguais em ordem crescente de data
    #       se as datas forem iguais em ordem crescente de identidade
    if a[1] != b[1]:
        return a[1] <= b[1]
    if data(a[2]) != data(b[2]):
        return data(a[2]) <= data(b[2])
    return a[0] <= b[0]

def comp2(a,b):
    # ordem crescente de nome
    #   se os nomes forem iguais em ordem decrescente de data
    #       se as datas forem iguais em ordem crescente de identidade
    if a[1] != b[1]:
        return a[1] <= b[1]
    if data(a[2]) != data(b[2]):
        return data(a[2]) >= data(b[2])
    return a[0] <= b[0]

def comp3(a,b):
    # ordem decrescente de data
    #   se as datas forem iguais em ordem crescente de nome
    #       se os nomes forem iguais em ordem crescente de identidade
    if data(a[2]) != data(b[2]):
        return data(a[2]) >= data(b[2])
    if a[1] != b[1]:
        return a[1] <= b[1]
    return a[0] <= b[0]

def comp4(a,b):
    # ordem crescente de identidade
    #   se as identidades forem iguais em ordem crescente de data
    #       se as datas forem iguais em ordem crescente de nome
    if a[0] != b[0]:
        return a[0] <= b[0]
    if data(a[2]) != data(b[2]):
        return data(a[2]) <= data(b[2])
    return a[1] <= b[1]
