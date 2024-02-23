class Fila:
    def __init__(self, maxlem):
        self.dados = [0] * maxlem
        self.prim = 0
        self.nlens = 0
        

    def enfileirar(self, chave):
        if self.nlens == len(self.dados):
            return False  
        self.dados[(self.prim +self.nlens-1)%(len(self.dados))]=chave
        self.nlens+=1
        return True

    def desenfileirar(self):
        if self.nlens==0:
            return False, -1
        elemento = self.dados[self.prim]
        self.prim = (self.prim + 1) % len(self.dados)
        self.nlens -= 1
        return elemento, True