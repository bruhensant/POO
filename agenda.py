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

    def obterNome(self):
        print(self.nome)

    def obterEmail(self):
        print(self.email)

    def alterarTelefone(self, numero):
        self.telefone = numero
    
    def alterarMatricula(self, novaM):
        self.matricula = novaM

    def validarMatricula(self):
        if len(str(self.matricula)) <4:
            print('Matrícula inválida ')
        else:
            print('Matrícula válida')