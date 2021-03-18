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

class termometro():
    