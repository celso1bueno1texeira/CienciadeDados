'''
Faça uma função chamada mediana que calcula e retorna a mediana de três valores passados por argumento.
O valor da mediana é o valor do meio de um conjunto de valores quando eles estão ordenados.
Protótipo:
mediana(a, b, c)
For example:
Test	                 Result
print(mediana(1,3,2))      2
print(mediana(2,3,1))      2
print(mediana(0,1,2))      1
print(mediana(4,3,6))      4



'''

def mediana(a, b, c):
    valores = [a, b, c]
    valores.sort()  # Ordena os valores
    
    return valores[1]  # Retorna o valor do meio

#Lê os valores
a = int(input())
b = float(input())
c = float(input())

# Teste da função
print(mediana(a, b, c)) 