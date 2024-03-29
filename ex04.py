'''
Há duas maneiras usuais de se expressar a eficiência do uso de combustíveis em carros no Brasil: (1) em km/L (quilômetro por litro); e (2) L/100 km (litros para cada 100 quilômetro).
Faça um programa em Python 3 que leia da entrada padrão uma linha com um valor real, n, que representa o número de km/L e imprima o valor convertido em L/100 km na saída padrão, com duas casas decimais.
For example:

Input	Result
10.00
10.00
5.00
20.00
12.00
8.33
5.10
19.61
'''
def km_100km(km_l):
    return 100 / km_l

def main():
    try:
        while True:
            km_l = float(input())
            l_100km = km_100km(km_l)
            print("{:.2f}".format(l_100km))
    except EOFError:
        pass

if __name__ == "__main__":
    main()
