class Pilha:
    def __init__(self, maxlem):
        self.dados = [0] * maxlem
        self.nlens = 0
    
    def empilhar(self, chave):
        if self.nlens == len(self.dados):
            return False  
        self.dados[self.nlens] = chave
        self.nlens += 1
        return True  
    
    def desempilhar(self):
        if self.nlens == 0:
            return False  
        self.nlens -= 1
        return self.dados[self.nlens], True 
        