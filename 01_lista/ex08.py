'''
Faça um programa em Python3 que leia da entrada padrão o nomes de meses, um em cada linha, e para cada mês imprima uma linha com o valor numérico daquele mês (inteiro). Use o dicionário definido abaixo, a entrada termina com uma linha com a palavra 'fim'. O nome do mês pode conter caracteres maiúsculos e minúsculos (use lower).
meses = {
    'janeiro': 1,
    'fevereiro': 2,
    'março': 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12,
}
For example:
Input	Result
setembro  9
SETEMBRO  9
Agosto    8
fim

Setembro  9
fim

ABRIL     4
MAIO      5
maio      5
fim

'''
meses = {
    'janeiro': 1,
    'fevereiro': 2,
    'março': 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12,
}

while True:
    entrada = input().lower()  # Converter para minúsculas
    
    if entrada == 'fim':
        break
    
    if entrada in meses:
        print(meses[entrada])
