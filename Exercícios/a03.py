# 3 - Crie uma classe Termômetro com as seguintes características:
#   – Atributo: Temperatura
#   – Construtor(es):
#       > o Construtor que não receba nenhum parâmetro e inicialize o campo
#           temperatura com o valor de 15.
#       > o Construtor que recebe uma temperature inicial
#   – Métodos
#       > o aumentarTemperatura: a temperature aumenta em 5 unidades;
#       > o diminuirTemperatura: a temperature diminui em 5 unidades;
#       > o getTemperatura: retorna o valor da temperatura.
#   – Restrições
#       > o O termômetro só permite temperaturas entre -20oC e 100oC. Logo, ao
#       aumentar ou diminuir a temperatura, esses valores devem ser
#       verificados, retornando um valor booleano em caso de sucesso ou
#       falha.

class Termometro():
    def __init__(self, temperatura=15): # default = 15, a menos que outro valor seja inserido
            self.temperatura = temperatura

    def aumentarTemperatura(self):
        if self.temperatura >= 100:
            return False
        else:
            self.temperatura += 5

    def diminuirTemperatura(self):
        if self.temperatura <= -20:
            return False
        else:
            self.temperatura -= 5

    def getTemperatura(self):
        return self.temperatura

# Done