""""
A tarifa de um táxi é por padrão R$ 4,00 mais R$ 0,50 para cada 200 metros rodados. 
Faça uma função chamada tarifa que retorne o valor de uma corrida com base nos quilômetros rodados.
A função deve ter os seguintes argumentos:
km: Obrigatório, quilômetros rodados (lembre-se que o preço é por 200 metros);
largada: Opcional, o valor da largada, por padrão 4.00;
valor: Opcional, O valor em reais para cada 200 metros rodados, por padrão 0.50.

"""

def tarifa(km, largada=4.00, valor=0.50):
    # Converter quilômetros em metros
    metros = km * 1000
    
    # Calcular o valor da tarifa
    valor_corrida = largada + (metros / 200) * valor
    
    return valor_corrida
a = int(input())
b = float(input())
c = float(input())

print(tarifa(a))  # Testando com 2 km, usando os valores padrão
print(tarifa(a, b, c))  # Testando com 5 km, largada R$ 5,00 e valor por km R$ 0,60
