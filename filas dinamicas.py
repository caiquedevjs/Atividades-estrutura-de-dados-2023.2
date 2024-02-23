class No:
    def __init__(self,chave):
        self.no=chave
        self.prox=None

class fila:
    def __init__(self):
        self.prim=None
        self.ultimo=None

    def enfileirar(self,chave):
        p=No(chave)
        if self.prim==None:
            self.prim=p
        else:
            self.ultimo.prox=p
        
        self.ultimo=p
        
    
        
        