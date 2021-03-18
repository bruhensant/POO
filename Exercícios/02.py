# 2 - Escreva uma classe Quadrado com atributo lado do tipo double. A classe deve ter
# um construtor que recebe como parâmetro o lado do quadrado. A classe deve ter
# também os métodos area() e perimetro() que retornam, respectivamente, a área e
# perímetro do quadrado.

class Quadrado():
    def __init__(self,l):
        self.lado:float = l  # IMPORTANTE -> o 'float' do Python tem a mesma precisão do 'double'

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4

quadrado = Quadrado(4.2)
print(quadrado.area())
print(quadrado.perimetro())