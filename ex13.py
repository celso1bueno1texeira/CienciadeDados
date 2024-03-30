"""
Faça uma função chamada dias que retorne o número de dias que um dado mês, passado por argumento, contém. O mês é indicado por um número entre 1 e 12, sendo 1 o mês de janeiro. 
A sua função deve também receber um argumento opcional chamado bissexto de valor padrão False. 
Quando o valor do argumento bissexto é True considere fevereiro com 29 dias, senão 28.
For example:
Test	                  Result
print(dias(1))           31
print(dias(2))           28
print(dias(2, True))     29
print(dias(3))           31
print(dias(2, bissexto=True))29
print(dias(2, bissexto=False))28
"""

def dias(mes, bissexto=False):
    meses = {
        1: 31,
        2: 29 if bissexto else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    return meses.get(mes, "Mês inválido")

# Testes da função
print(dias(1))  # Janeiro, 31 dias
print(dias(2))  # Fevereiro, 28 dias (ou 29 se bissexto)
print(dias(2, True))  # Fevereiro, 29 dias
print(dias(3))  # Março, 31 dias
print(dias(2, bissexto=True))  # Fevereiro, 29 dias
print(dias(2, bissexto=False))  # Fevereiro, 28 dias