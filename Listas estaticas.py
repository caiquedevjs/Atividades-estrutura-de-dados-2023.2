class lista:
    def __init__(self,maxlen):
        self.dados=[0]*maxlen
        self.nlems=0

    def consulta(self,chave):
        for i in range(self.nlems):
            if self.dados[i]==chave:
                return True
        return False
    
    def inserir(self, chave):
        if self.nlems == len(self.dados):
            return False  
        if self.consulta(chave):
            return False  
        self.dados[self.nlems] = chave
        self.nlems += 1
        return True  

        
    def remover(self,chave):
        if self.nlems==0:
            return False
        for i in range(self.nlems):
            if self.dados[i]== chave:
                self.dados[i]=self.dados[self.nlems-1]
                self.nlems-=1
                return True, self.dados[self.nlems-1]
        return False
    
    def menor(self):
        if self.nlems == 0:
            return False
        menor = self.dados[0]
        for i in range(self.nlems):
            if self.dados[i] < menor:
                menor = self.dados[i]
        return menor
    def maior(self):
        if self.nlems == 0:
                return False
        maior = self.dados[0]
        for i in range(self.nlems):
            if self.dados[i] > maior:
                maior = self.dados[i]
        return maior

    def pares(self):
        par=0
        if self.nlems==0:
            return False
        for i in range(self.nlems):
            if self.dados[i]%2==0:
                par+=1

        return par
    
    def soma(self):
        soma=0
        if self.nlems==0:
            return False,0
        for i in range(self.nlems):
            soma+=self.dados[i]
        return soma
    
    def remover_maior(self):
        maior=self.maior
        if maior==None:
            return False
        self.remover(maior)
        return True

        


    

        