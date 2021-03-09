class Agenda():
    def __init__(self): # construtor
        self.Pessoas = [] # ou seja, tudo que for definido como "Agenda", vai receber essa característica

    def inserirPessoa(self, usuario): # método = função, que vai dar append(x)
        self.Pessoas.append(usuario)  # dentro de uma lista chamada Pessoas, que é o Atributo de "Agenda"

    # removerPessoa(pessoa)

    def imprimirAgenda(self):
        print(self.Pessoas)

class Pessoa():
    pass

#######################################################################
#                           >> EXECUÇÕES <<                           #
####################################################################### 

contatos = Agenda()

# contatos.Pessoas = []

contatos.inserirPessoa('fulano')
contatos.inserirPessoa('sicrano')
contatos.inserirPessoa('beltrano')

contatos.imprimirAgenda()

# print(contatos) >> ERRO!