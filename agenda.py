class Agenda():
    def __init__(self):   # construtor
        self.Pessoas = [] # ou seja, tudo que for definido como "Agenda", vai receber essa característica

    def inserirPessoa(self, usuario): # método = função, que vai dar append(x)
        self.Pessoas.append(usuario)  # dentro de uma lista chamada Pessoas, que é o Atributo de "Agenda"

    def removerPessoa(self, usuario):
        for contatinho in self.Pessoas:
            if contatinho.nome == usuario:
                self.Pessoas.remove(contatinho)

    def imprimirAgenda(self): # método que exibe todos os itens da agenda
        for contatinho in self.Pessoas:
            print(contatinho.nome)

class Pessoa():
    def __init__(self, nome, telefone, email, matricula):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.matricula = matricula

    # 1 get <|

    def obterNome(self):
        print(self.nome)

    def obterEmail(self):
        print(self.email)
    
    # 2 set <|

    def alterarTelefone(self, numero):
        self.telefone = numero
    
    def alterarMatricula(self, novaM):
        self.matricula = novaM

    # 3 validar matricula

    def validarMatricula(self):
        if len(str(self.matricula)) < 4:
            print('Matrícula inválida')
        else:
            print('Matrícula válida')


#######################################################################
#                          >=> EXECUÇÕES <=<                          #
#######################################################################

a1 = Pessoa('Furlano', 1111-1111, 'email1@email.com', 1111)
a2 = Pessoa('Sicrano', 2222-2222, 'email2@email.com', 2222)
a3 = Pessoa('Beltrano', 3333-3333, 'email3@email.com', 3333)

contatos = Agenda()

contatos.inserirPessoa(a1)
contatos.inserirPessoa(a2)
contatos.inserirPessoa(a3)

contatos.imprimirAgenda()

contatos.removerPessoa('Sicrano')

print('==============================')

contatos.imprimirAgenda()

print('==============================')

a1.obterNome()
a3.obterEmail()