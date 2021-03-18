'''
private / privado
    nada pode acessar, só suas próprias funções

protected / protegido
    privado, mas as classes que herdam podem acessar

public / público
    tudo pode acessar
'''

class Nome():
    def __init__(self):
        self.__privado = None   # valor privado
        self._protegido = None  # valor protegido
        self.publico = None     # valor público