
class No:
    def __init__(self, palavra):
        self.palavra = palavra
        self.proximo = None

class Lista:
    def __init__(self):
        self.prim = None

    def inserir(self, palavra):
        nova_palavra = No(palavra)
        if self.prim == None:
            self.prim = nova_palavra
        else:
            atual = self.prim
            anterior = None
            while atual != None and atual.palavra < palavra:
                anterior = atual
                atual = atual.proximo
            if anterior == None:
                nova_palavra.proximo = self.prim
                self.prim = nova_palavra
            else:
                anterior.proximo = nova_palavra
                nova_palavra.proximo = atual

    def listar_palavras(self):
        palavras = []
        atual = self.prim
        while atual != None:
            palavras.append(atual.palavra)
            atual = atual.proximo
        return palavras

class ListaPalavras:
    def __init__(self):
        self.palavras_com_5_letras = Lista()  # palavras com até 5 letras
        self.palavras_com_10_letras = Lista()  # palavras de 6 a 10 letras
        self.palavras_mais_10_letras = Lista()  # palavras com mais de 10 letras
        self.lista_de_palavras = Lista()  # lista que conecta todas as palavras

    def executar_comando(self, comando):
        if comando[0] == 'i':  
            palavra = comando[1]
            if self.buscar_palavra(palavra):
                print("palavra já existente:", palavra)
            else:
                self.inserir_palavra(palavra)
                print("palavra inserida:", palavra)
        elif comando[0] == 'l':  
            num_lista = int(comando[1])
            if num_lista == 1:
                self.palavras_com_5_letras.listar_palavras()
            elif num_lista == 2:
                self.palavras_com_10_letras.listar_palavras()
            elif num_lista == 3:
                self.palavras_mais_10_letras.listar_palavras()
            elif num_lista == 4:
                self.lista_de_palavras.listar_palavras()
        elif comando[0] == 'x':  
            num_letras = int(comando[1])
            palavras = self.palavras_por_tamanho(num_letras)
            if len(palavras) == 0:
                print("lista vazia")
            else:
                for i in range(len(palavras)):
                    print(palavras[i])
        elif comando[0] == 'o': 
            l1 = comando[1]
            l2 = comando[2]
            palavras = self.palavras_por_ordem_alfabetica(l1, l2)
            if len(palavras) == 0:
                print("lista vazia")
            else:
                for i in range(len(palavras)):
                    print(palavras[i])
        elif comando[0] == 'r':  
            palavra = comando[1]
            if not self.buscar_palavra(palavra):
                print("palavra inexistente:", palavra)
            else:
                self.remover_palavra(palavra)
                print("palavra removida:", palavra)

    def buscar_palavra(self, palavra):
        atual = self.lista_de_palavras.prim
        while atual != None:
            if atual.palavra == palavra:
                return True
            atual = atual.proximo
        return False

    def inserir_palavra(self, palavra):
        nova_palavra = No(palavra)
        self.lista_de_palavras.inserir(palavra)
        if len(palavra) <= 5:
            self.palavras_com_5_letras.inserir(palavra)
        elif len(palavra) <= 10:
            self.palavras_com_10_letras.inserir(palavra)
        else:
            self.palavras_mais_10_letras.inserir(palavra)

    def palavras_por_tamanho(self, num_letras):
        palavras = []
        atual = self.lista_de_palavras.prim
        while atual != None:
            if len(atual.palavra) == num_letras:
                palavras=palavras+[atual.palavra]
            atual = atual.proximo
        return palavras

    def palavras_por_ordem_alfabetica(self, l1, l2):
        palavras = []
        atual = self.lista_de_palavras.prim
        while atual != None:
            if l1 <= atual.palavra[0] <= l2:
                palavras=palavras+[atual.palavra]
            atual = atual.proximo
        return palavras

    def remover_palavra(self, palavra):
        atual = self.lista_de_palavras.prim
        anterior = None
        while atual != None:
            if atual.palavra == palavra:
                if anterior == None:
                    self.lista_de_palavras.prim = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                break
            anterior = atual
            atual = atual.proximo

    def ler_comandos(self):
        comandos = []
        while True:
            comando = input()
            comandos = comandos + [comando]
            if comando[0] == 'e':  
                break
        return comandos
    
lista_palavras = ListaPalavras()
comandos = lista_palavras.ler_comandos()
for i in range(len(comandos)):
    lista_palavras.executar_comando(comandos[i])

lista_palavras = ListaPalavras()
lista_palavras.inserir_palavra("casa")
lista_palavras.inserir_palavra("azulejo")
lista_palavras.inserir_palavra("escola")
lista_palavras.inserir_palavra("parque")
lista_palavras.inserir_palavra("gato")

lista_palavras.palavras_com_5_letras.listar_palavras()

