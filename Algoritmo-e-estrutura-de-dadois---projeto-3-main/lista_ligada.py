from typing import Self
from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        return self.inicio is None

    def remove(self, item):
        if self.inicio is None:
            return  

        if self.inicio.valor == item:
            self.inicio = self.inicio.get_proximo()
            return

        anterior = self.inicio
        remove = self.inicio.get_proximo()

        while remove is not None:
            if remove.valor == item:
                anterior.set_proximo(remove.get_proximo())
                return
            anterior = remove
            remove = remove.get_proximo()

    def tamanho(self) -> int:
        contador = 0
        tamanho = self.inicio
        while tamanho is not None:
            contador += 1
            tamanho = tamanho.get_proximo()
        return contador
    
    def limpa(self):
        self.inicio = None

    def procura(self, item) -> bool:
        procura = self.inicio
        while procura is not None:
            if procura.valor == item:
                return True
            procura = procura.get_proximo()
        return False

    def indice_de(self, item):
        indice = self.inicio
        index = 0
        while indice is not None:
            if indice.valor == item:
                return index
            indice = indice.get_proximo()
            index += 1
        return -1        

    def recupera_indice(self, index):
        recupera_indice = self.inicio
        contador = 0
        while recupera_indice is not None:
            if contador == index:
                return recupera_indice.valor
            recupera_indice = recupera_indice.get_proximo()
            contador += 1
        raise IndexError
    def remove_indice(self,index):
        if index < 0 or index >= self.tamanho():
            raise IndexError
        if index == 0:
            self.inicio = self.inicio.get_proximo()
            return
        anterior = None
        atual = self.inicio
        contador = 0
        while contador < index:
            anterior = atual
            atual = atual.get_proximo()
            contador += 1
        anterior.set_proximo(atual.get_proximo())  

class no:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

                
class pilha:
    def __init__(self):
        self.topo = None

    def esta_vazio(self):
        return self.topo is None

    def push(salf,valor):
        novo_no = no(valor)
        if Self.esta_vazio():
            Self.topo = novo_no
        else:
            novo_no.next = Self.topo
            Self.topo = novo_no

    def pop(self):
        if self.esta_vazio():
            raise IndexError
        return self.topo.valor

    def search(self,item):
        atual = self.topo
        index = 0
        while atual is not None:
            if atual.valor == item:
                return index
            atual = atual.proximo
            index += 1
        return -1

class fila:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vazio(self):
        return self.frente is None

    def enqueue(self,valor):
        novo_no = no(valor)
        if self.esta_vazio():
            self.fente = novo_no
            self.final = novo_no
        else:
            self.final.proximo = novo_no
            self.final = novo_no

    def denqueue(self):
        if self.esta_vazio():
            raise IndexError
        valor = self.fente.valor
        if self.fente == self.final:
            self.frente = None
            self.final = None
        else:
            self.frente = self.frente.valor
        return valor    

    def search(self,item):
        atual = self.fente
        index = 0
        while atual is not None:
            if atual.valor == item:
                return index
            atual = atual.proximo
            index += 1
        return -1       





                 



                


            
                         




    

        
