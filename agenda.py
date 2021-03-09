class Agenda():
    def __init__(self):   # construtor
        self.Pessoas = [] # ou seja, tudo que for definido como "Agenda", vai receber essa característica

    def inserirPessoa(self, usuario): # método = função, que vai dar append(x)
        self.Pessoas.append(usuario)  # dentro de uma lista chamada Pessoas, que é o Atributo de "Agenda"

    def removerPessoa(self, usuario):
        #for contatinho in self.Pessoas:
            #if contatinho == nome:
                #removo
        pass

    def imprimirAgenda(self): # método que exibe todos os itens da agenda
        for contatinho in self.Pessoas:
            print(contatinho.nome)

class Pessoa():
    def __init__(self, nome, telefone, email, matricula):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.matricula = matricula

####################################################################### 
#                           >> EXECUÇÕES <<                           #
#######################################################################

a1 = Pessoa('Bunda', 12345678, 'bunda@cu.com', 1111)

contatos = Agenda()

contatos.inserirPessoa(a1)

contatos.imprimirAgenda()