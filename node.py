class Node:
    def __init__(self,dado, key):
        self.key = key
        self.dado = dado
        self.esq = None
        self.dir = None
        self.altura = 1   

    property 
    def dado(self):
        return self.dado
    
    def key(self):
        return self.key
    
    def altura(self):
        return self.altura

    def __str__(self):
        return str(self.dado)
    
    def imprimir(self):
        return self.__str__