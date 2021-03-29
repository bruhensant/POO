# Crie uma classe que represente um departamento de uma empresa, registrando
# os funcionários criados na questão anterior. Além disso, crie as classes
# Recepcionista, Porteiro e Motorista. O salário de cada um dos três é $2000,00,
# $2050,00 e $2030,00, respectivamente, acrescido de $300,00 de abono para todos
# os funcionários.
# Através do método main, mostre a execução do seu programa, considerando:
#   – Registrar funcionários
#   – Remover funcionários
#   – Apresentar lista dos atuais funcionários, com os respectivos salários.

from a04 import *

class Funcionarios():
    def __init__(self):
        self.funcs = []
    
    def listarFuncionarios(self):
        for x in self.funcs:
            return x.nome(), x.salario()

    def addFuncionario(self, funcio):
        self.funcs.append(funcio)

    def demitirFuncionario(self, funcio):
        self.funcs.remove(funcio)

class Recepcionista():
    def __init__(self):
        self.salario = 2000.00
        self.abono = 300

class Porteiro():
    def __init__(self):
        self.salario = 2050.00
        self.abono = 300

class Motorista():
    def __init__(self):
        self.salario = 2030.00
        self.abono = 300

lista = Funcionarios()

e2 = Endereco('Rua dos Bobos', 51)
a1 = Empregado('Marcelo', 21, Recepcionista().salario, Recepcionista(), e2)

# Done ?