'''
Escreva uma função em Python 3 com o seguinte protótipo:
quadrado(x)
Sua função deve retornar o quadrado do número x. O código que usa esta função é automaticamente atrelado pelo corretor.
Uma resposta para esta questão é
def quadrado(x):
    return x*x
For example:
Test	Input	Result
value = int(input())
print(quadrado(value))
2
4
value = int(input())
print(quadrado(value))
3
9

'''
def quadrado(x):
    return x * x

def main():
    try:
        while True:
            valor = int(input())
            print(quadrado(valor))
    except EOFError:
        pass

if __name__ == "__main__":
    main()


