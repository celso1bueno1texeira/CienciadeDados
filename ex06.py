'''
Faça um programa em Python 3 que leia uma linha contendo um texto (string) da entrada padrão e imprima o texto com todos os seus caracteres em minúsculo.
Dica:
Uma maneira de fazer a leitura é:
texto = input()
A função s.lower() retorna a string, s, em minúsculo.
'''
def main():
    texto = input("")
    texto_minusc = texto.lower()
    print(texto_minusc)

if __name__ == "__main__":
    main()
