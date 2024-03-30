'''
Escreva uma função em Python 3 com o seguinte protótipo:
maior(a, b)
Sua função deve retornar o maior valor entre a e b. Sua função deve retornar o valor mesmo quando a for igual a b.
For example:
Test	Input	Result
a, b = map(int, input().split())
print(maior(a, b))
2 3
3
a, b = map(int, input().split())
print(maior(a, b))
7 2
7

'''

def maior(a, b):
    if a >= b:
        return a
    else:
        return b
    
a, b = map(int, input().split())
print(maior(a, b))