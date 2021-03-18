# Escreva uma classe que encapsule um valor inteiro qualquer. Essa classe deve
# esconder o valor encapsulado de programadores-usuários, fazendo com que o
# acesso ao valor seja feito através de métodos que devem zerar, incrementar e
# imprimir o valor da variável.

class Encapsular():
    def __init__(self,x):
        self.__valor = x
    
    def zerar(self):
        self.__valor = 0

    def incrementar(self, x):
        self.__valor += x

    def imprimir(self):
        print(self.__valor)