class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def empilhar(self, elemento):
        novo_no = No(elemento)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def desempilhar(self):
        if self.topo==None:
            return False
        elemento = self.topo.valor
        self.topo = self.topo.proximo
        return True, elemento

    
