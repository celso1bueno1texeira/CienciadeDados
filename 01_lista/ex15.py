'''
Implemente as classes, Veiculo e Carro conforme diagrama abaixo em Python.
Especificação:
Os nomes devem ser precisamente como estabelecidos;
Classe Veiculo:
Deve ter dois atributos: nome (string), com padrão "" e valor (int), com padrão 0
Deve ter três métodos: o de inicialização (__init__), __str__ e get_valor:
__init__: Além do argumento self deve receber os argumentos nome e valor nesta ordem e iniciar os atributos com os respectivos nomes;
__str__: Recebe apenas o argumento self, simplesmente retorna o atributo nome;
get_valor: Recebe apenas o argumento self, simplesmente retorna o atributo valor;
Classe Carro:
Deve herdar da classe Veiculo (i.e. é sub classe de Veiculo)
Deve ter um atributo: portas (int)
Deve respeitar os atributos padrões da classe Veiculo
Deve ter dois métodos o de inicialização (__init__) e get_portas:
__init__: Além do argumento self deve receber os argumentos portas, nome e valor nesta ordem e iniciar os atributos com os respectivos nomes. 
Use super() para chamar o __init__ da super classe (Veiculo) para iniciar os atributos nome e valor;
get_portas: Recebe apenas o argumento self, simplesmente retorna o atributo portas;
Os casos de teste testarão tanto quanto ao uso das classes quanto a correta implementação das especificações acima.
Dica: Estude os casos de teste de exemplo.
For example:

Test	                                                 Result
v1 = Veiculo("Corsa", 32000)
print(v1)                                                Corsa
print(v1.get_valor())                                    32000

v2 = Veiculo("Corsa 2")
print(v2)                                                Corsa 2
print(v2.get_valor())                                       0

c1 = Carro(5, "Ka", 30000)                                 Ka
print(c1)                                                 30000
print(c1.get_valor())                                      5
print(c1.get_portas())

c2 = Carro(4, "Ka")                                        Ka
print(c2)                                                  0
print(c2.get_valor())                                      4
print(c2.get_portas())

print("get_valor" in Veiculo.__dict__)                    True
print("get_valor" in Carro.__dict__)                      False
print("__str__" in Veiculo.__dict__)                      True
print("__str__" in Carro.__dict__)                        False
print("get_portas" in Veiculo.__dict__)                   False
print("get_portas" in Carro.__dict__)                     True

'''

class Veiculo:
    def __init__(self, nome="", valor=0):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return self.nome

    def get_valor(self):
        return self.valor


class Carro(Veiculo):
    def __init__(self, portas, nome="", valor=0):
        super().__init__(nome, valor)
        self.portas = portas

    def get_portas(self):
        return self.portas


# Testes das classes
v1 = Veiculo("Corsa", 32000)
print(v1)  # Deve imprimir "Corsa"
print(v1.get_valor())  # Deve imprimir 32000

v2 = Veiculo("Corsa 2")
print(v2)  # Deve imprimir "Corsa 2"
print(v2.get_valor())  # Deve imprimir 0

c1 = Carro(5, "Ka", 30000)
print(c1)  # Deve imprimir "Ka"
print(c1.get_valor())  # Deve imprimir 5
print(c1.get_portas())  # Deve imprimir 30000

c2 = Carro(4, "Ka")
print(c2)  # Deve imprimir "Ka"
print(c2.get_valor())  # Deve imprimir 0
print(c2.get_portas())  # Deve imprimir 4

print("get_valor" in Veiculo.__dict__)  # Deve imprimir True
print("get_valor" in Carro.__dict__)  # Deve imprimir False
print("__str__" in Veiculo.__dict__)  # Deve imprimir True
print("__str__" in Carro.__dict__)  # Deve imprimir False
print("get_portas" in Veiculo.__dict__)  # Deve imprimir False
print("get_portas" in Carro.__dict__)  # Deve imprimir True
