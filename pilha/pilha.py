class Pilha:

    #construtor
    def __init__(self, capacidade):
        self.lista = [None] * capacidade   #declarando e inicializando os atributos  
        self.topo = -1

    #empilha
    def put(self, elemento: object):
        if self.topo == len(self.lista) - 1:   #nao tenho espaco livre na lista
            self.lista.append(elemento)
            self.topo = self.topo + 1
        else: 
            self.topo = self.topo + 1
            self.lista[self.topo] = elemento

    #desempilha
    def pop(self) -> object:
        resp = self.lista[self.topo]
        self.topo = self.topo - 1
        return resp

    #elemento topo
    def peek(self) -> object:
        return selt.lista[self.topo]

    #esta cheia
    def isFull(self) -> bool:
        return False

    #esta vazia
    def isEmpty(self) -> bool:
        if self.topo == -1:
            return True
        else:
            return False