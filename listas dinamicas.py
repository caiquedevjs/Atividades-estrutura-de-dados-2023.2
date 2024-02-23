class No:
    def __init__(self,chave):
        self.no=chave
        self.prox=None
class lista:
    def __init__(self):
        self.prim=None

    def consulta(self,chave):
        p=self.prim
        while p!= None:
            if p.no==chave:
                return True
            p=p.prox
        return False
    
    def inserir(self,chave):
        if self.consulta(chave):
            return False
        p=No(chave)
        p.prox=self.prim
        self.prim=p
        return True
    
    def remover (self,chave):
        if self.prim==None:
            return False,-1
        res,p=self.consulta(chave)
        if res:
            p.no=self.prim.no
            self.prim=self.prim.prox
            return res
        
   
    