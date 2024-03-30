'''
Faça um programa em Python 3 que leia uma linha contendo um número inteiro de 4 dígitos e calcule a soma dos dígitos. Por exemplo para o número 1234 o resultado é 1 + 2 + 3 + 4 = 10
Dica:
Não converta todo o número como um único inteiro, ao invés acesse cada dígito separadamente e então coverta cada dígitos em inteiro.
valor = input()
digito0 = int(valor[0])
digito1 = int(valor[1])

'''

# Ler o número de 4 dígitos
numero = input("Digite um número inteiro de 4 dígitos: ")

# Verificar se o número tem 4 dígitos
if len(numero) != 4:
    print("Por favor, insira um número de 4 dígitos.")
else:
    # Inicializar a soma
    soma = 0
    
    # Percorrer cada dígito e somá-los
    for digito in numero:
        soma += int(digito)
    
    # Exibir o resultado
    print("A soma dos dígitos é:", soma)