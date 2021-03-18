# Escreva uma classe que encapsule um valor inteiro qualquer. Essa classe deve
# esconder o valor encapsulado de programadores-usuários, fazendo com que o
# acesso ao valor seja feito através de métodos que devem zerar, incrementar e
# imprimir o valor da variável.

class Encapsular():
    def __init__(self,x):
        self.__valor = int(x)
    
    def zerar(self):
        self.__valor = int(0)

    def incrementar(self, x):
        self.__valor += int(x)

    def imprimir(self):
        print(self.__valor)

a1 = Encapsular(2)

a1.imprimir
a1.incrementar(8)
a1.imprimir
a1.zerar
a1.imprimir
