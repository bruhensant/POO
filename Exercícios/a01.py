# 1 - Escreva uma classe que encapsule um valor inteiro qualquer. Essa classe deve
# esconder o valor encapsulado de programadores-usuários, fazendo com que o
# acesso ao valor seja feito através de métodos que devem zerar, incrementar e
# imprimir o valor da variável.

class Encapsular():                 # encapsula e armazena o valor passado
    def __init__(self,x):
        self.__valor:int = x
    
    def zerar(self):                # zera o valor armazenado
        self.__valor:int = 0

    def incrementar(self, x):       # incrementa o valor passado ao valor armazenado
        self.__valor += x

    def imprimir(self):             # exibe o valor armazenado
        print(self.__valor)

# Execuções

a1 = Encapsular(5)
a1.imprimir()
a1.zerar()
a1.imprimir()
a1.incrementar(10)
a1.imprimir()

# Done