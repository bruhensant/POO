# A fim de representar empregados em uma firma, crie uma classe chamada
# Empregado que herda as características de uma classe Pessoa, incluindo as
# seguintes características:
#    – Atributos
#        o Salário mensal
#        o Cargo
#        o Endereço: o endereço deve ser um objeto da classe Endereço.
#    – Construtores:
#        > o Um constructor para inicializar os três atributos e os dados pessoais
#        para classe Pessoa
#        > o Um constructor para inicializar apenas o salário os dados pessoais
#        para classe Pessoa
#        > o Um constructor para inicializar salário e cargo os dados pessoais para
#        classe Pessoa
#    – Métodos
#        o Obter valores dos atributos
#        o Atualizar os valores dos atributos.
#    - Restrições
#        > o Um salário não pode ter seu valor negativo. Logo, ao atualizar salário,
#        deve-se verificar sua consistência

class Pessoa():
    def __init__(self,nome):
        self.nome = nome

class Empregado(Pessoa):
    def __init__(self, nome, salario, cargo, endereco):
        self.nome= nome
        self.salario = salario 
        self.cargo = cargo 
        self.endereco = endereco  

a1 = Pessoa('João')

a2 = Empregado('Maria', 200, 'Dona', 'Rua dos Bobos')

