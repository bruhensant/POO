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

!!!! VEJA OS VÍDEOS DE GETTER E SETTER:

https://youtu.be/PGXwNophTOQ

!!!! VEJA /\ /\ /\ /\ /\ /\

class Pessoa():
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

class Empregado(Pessoa):
    def __init__(self, nome, idade, salario, cargo, endereco):
        super().__init__(nome, idade)

        self.salario = salario
        self.cargo = cargo
        self.endereco = endereco

class Endereco():
    def __init__(self,rua, ncasa,):
        self.rua = rua
        self.ncasa = ncasa

e2 = Endereco('Rua dos Bobos', 51)

a1 = Pessoa('João',18)

a2 = Empregado('Maria',36, 200, 'Dona', e2)