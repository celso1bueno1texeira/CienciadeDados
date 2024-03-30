'''

Implemente a classe Racional, apresentada no material 05-Introdução à Orientação a ObjetosArquivo
O principal objetivo desta questão é você coompreender como questões de implementação de classes são automaticamente corrigidas no Moodle usando CodeRunner.
Especificação:
Os nomes devem ser precisamente como estabelecidos;
Nome da classe: Racional;
Métodos já existentes no material:
__init__(self, num, den): Inicia o objeto, onde num é o numerador e den o denominador do número racional
__str__(self): Retorna o número racional em forma de texto no formato "<numerador>/<denominado>"
__int__(self): Converte o valor racional em inteiro arredondando se necessário
__float__(self): Converte o valor em float
__add__(self, obj2): faz a soma de dois números racionais ou de um racional (self) com um inteiro ou float (obj2)
__eq__(self, obj2), __nq__(self, obj2), __lt__(self, obj2), __gt__(self, obj2), __le__(self, obj2) e __ge__(self, obj2): retorna o comparativo entre dois números racionais
Métodos novos:
get_denominador(self): retorna o denominador (em self._den)
get_numerador(self): retorna o numerador (em self._num)
For example:

Test	                   Result
a = Racional(1, 2)
b = Racional(3, 4)
print(a+b)                 10/8
a = Racional(1, 2)
b = Racional(3, 4)
print(a < b)               True
a = Racional(1, 2)
print(a.get_numerador())    1
print(a.get_denominador()   2
a = Racional(1, 2)
b = Racional(3, 4)
print(a == b)              False
a = Racional(1, 2)
b = Racional(3, 4)
print(a != b)              True
a = Racional(6, 2)
print(int(a))               3 

'''

class Racional:
    def __init__(self, num, den):
        self._num = num
        self._den = den

    def __str__(self):
        return f"{self._num}/{self._den}"

    def __int__(self):
        return int(self._num / self._den)

    def __float__(self):
        return float(self._num / self._den)

    def __add__(self, obj2):
        if isinstance(obj2, Racional):
            num = self._num * obj2._den + obj2._num * self._den
            den = self._den * obj2._den
            return Racional(num, den)
        else:
            num = self._num + obj2 * self._den
            den = self._den
            return Racional(num, den)

    def __eq__(self, obj2):
        return self._num * obj2._den == obj2._num * self._den

    def __ne__(self, obj2):
        return not self.__eq__(obj2)

    def __lt__(self, obj2):
        return self._num * obj2._den < obj2._num * self._den

    def __gt__(self, obj2):
        return self._num * obj2._den > obj2._num * self._den

    def __le__(self, obj2):
        return self._num * obj2._den <= obj2._num * self._den

    def __ge__(self, obj2):
        return self._num * obj2._den >= obj2._num * self._den

    def get_numerador(self):
        return self._num

    def get_denominador(self):
        return self._den

# Testes da classe Racional
a = Racional(1, 2)
b = Racional(3, 4)
print(a + b)  # Deve imprimir 10/8
a = Racional(1, 2)
b = Racional(3, 4)
print(a < b)  # Deve imprimir True
a = Racional(1, 2)
print(a.get_numerador())  # Deve imprimir 1
print(a.get_denominador())  # Deve imprimir 2
a = Racional(1, 2)
b = Racional(3, 4)
print(a == b)  # Deve imprimir False
a = Racional(1, 2)
b = Racional(3, 4)
print(a != b)  # Deve imprimir True
a = Racional(6, 2)
print(int(a))  # Deve imprimir 3
