# Escreva uma classe que encapsule um valor inteiro qualquer. Essa classe deve
# esconder o valor encapsulado de programadores-usuários, fazendo com que o
# acesso ao valor seja feito através de métodos que devem zerar, incrementar e
# imprimir o valor da variável.

class Encapsular():
    def __init__(self,valor):
        self.__valor:int = valor
    
    def zerar(self):
        self.valor = 0

    def incrementar(self, valor):
        self.valor += valor

    def imprimir(self):
        print(self.valor)

a1 = Encapsular(2)

a1.imprimir
a1.incrementar(8)
a1.imprimir
a1.zerar
a1.imprimir
