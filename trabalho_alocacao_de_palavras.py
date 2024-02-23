class No:
    def __init__(self, palavra):
        self.palavra = palavra
        self.prox = None

class Lista:
    def __init__(self):
        self.prim = None

    def inserir(self, palavra):
        novo_no = No(palavra)
        if self.prim == None:
            self.prim = novo_no
        elif palavra < self.prim.palavra:
            novo_no.prox = self.prim
            self.prim = novo_no
        else:
            atual = self.prim
            while atual.prox != None and atual.prox.palavra < palavra:
                atual = atual.prox
            novo_no.prox = atual.prox
            atual.prox = novo_no

    def remover(self, palavra):
        if self.prim == None:
            return False
        elif self.prim.palavra == palavra:
            self.prim = self.prim.prox
            return True
        else:
            atual = self.prim
            while atual.prox != None and atual.prox.palavra != palavra:
                atual = atual.prox
            if atual.prox != None:
                atual.prox = atual.prox.prox
                return True
        return False

    def listar(self):
        atual = self.prim
        while atual != None:
            print(atual.palavra)
            atual = atual.prox

class ListaPalavras:
    def __init__(self):
        self.palavras_com_5_letras = Lista()  
        self.palavras_com_10_letras = Lista()  
        self.palavras_mais_10_letras = Lista()  
        self.lista_de_palavras = Lista() 

    def executar_comando(self, comando):
        if comando == 'i':
            palavra = input()
            if self.buscar_palavra(palavra):
                print("palavra já existente:", palavra)
            else:
                self.inserir_palavra(palavra)
                print("palavra inserida:", palavra)
        elif comando == 'l':
            lista_num = int(input())
            if lista_num == 1:
                self.palavras_com_5_letras.listar()
            elif lista_num == 2:
                self.palavras_com_10_letras.listar()
            elif lista_num == 3:
                self.palavras_mais_10_letras.listar()
            elif lista_num == 4:
                self.lista_de_palavras.listar()
        elif comando == 'x':
            num_letras = int(input())
            encontrou = False
            if num_letras <= 5:
                atual = self.palavras_com_5_letras.prim
                while atual != None:
                    if len(atual.palavra) == num_letras:
                        print(atual.palavra)
                        palavra_achada = True
                    atual = atual.prox
            elif num_letras <= 10:
                atual = self.palavras_com_10_letras.prim
                while atual != None:
                    if len(atual.palavra) == num_letras:
                        print(atual.palavra)
                        palavra_achada = True
                    atual = atual.prox
            else:
                atual = self.palavras_mais_10_letras.prim
                while atual != None:
                    if len(atual.palavra) == num_letras:
                        print(atual.palavra)
                        palavra_achada = True
                    atual = atual.prox
            if not palavra_achada:
                print("lista vazia")
        elif comando == 'o':
            letra1 = input()
            letra2 = input()
            atual = self.lista_de_palavras.prim
            palavra_achada = False
            while atual != None:
                if letra1 <= atual.palavra[0] <= letra2:
                    print(atual.palavra)
                    palavra_achada = True
                atual = atual.prox
            if not palavra_achada:
                print("lista vazia")
        elif comando == 'r':
            palavra = input()
            self.palavras_com_5_letras.remover(palavra)
            self.palavras_com_10_letras.remover(palavra)
            self.palavras_mais_10_letras.remover(palavra)
            removido =  self.lista_de_palavras.remover(palavra)
            if removido:
                print("palavra removida:", palavra)
            else:
                print("palavra inexistente:", palavra)
        elif comando == 'e':
            return False
        return True

    def buscar_palavra(self, palavra):
        atual = self.lista_de_palavras.prim
        while atual != None:
            if atual.palavra == palavra:
                return True
            atual = atual.prox
        return False
    
    def inserir_palavra(self, palavra):
        novo_no = No(palavra)
        self.lista_de_palavras.inserir(palavra)
        if len(palavra) <= 5:
            self.palavras_com_5_letras.inserir(palavra)
        elif len(palavra) <= 10:
            self.palavras_com_10_letras.inserir(palavra)
        else:
            self.palavras_mais_10_letras.inserir(palavra)
    
           
    def ler_comandos(self):
        while True:
            comando = input()
            if not self.executar_comando(comando):
                break
lista_palavras = ListaPalavras()
lista_palavras.ler_comandos()