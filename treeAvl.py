from node import Node

class treeExceptionL(Exception): 
    def __init__(self, mensagem): 
        super().__init__(mensagem)

# Construindo uma Árvore AVL.
class ArvoreAVL:
    def __init__(self):
        self.node = None

    # Rotina para adção das chames na Árvore AVL.
    def inserir(self, raiz, dado):
        # Adição da raiz.
        if raiz == None: 
            return Node(dado, dado.key)
        elif dado.key == raiz.key:
            raise treeExceptionL(f'A chave {dado.key} já existe')
        # Adicionando o folha da "Esquerda".
        elif dado.key < raiz.key: 
            raiz.esq = self.inserir(raiz.esq, dado)
        # Adicionando o folha da "Direita".
        else:
            raiz.dir = self.inserir(raiz.dir, dado)
        # Atualização da Altura da Árvore.
        raiz.altura = 1 + max(self.tam(raiz.esq), self.tam(raiz.dir))
        # Atualizando o Fator de Balanceamento.
        balance = self.fatorBalance(raiz)
        print('Chave {}, Fator de balanceamento: {}\n'.format(dado.key,balance))
        # Rotação Simples à Direita.
        if balance > 1 and dado.key < raiz.esq.dado.key:
            print('Rotação simples à direita\n')
            return self.rotaDir(raiz)
        # Rotação Simples à ESquerda.
        if balance < -1 and dado.key > raiz.dir.dado.key:
            print('Rotação simples à esquerda\n')
            return self.rotaEsq(raiz)
        # Rotação Dupla à Direita.
        if balance > 1 and dado.key > raiz.esq.dado.key:
            print('Rotação dupla à direita\n')
            raiz.esq = self.rotaEsq(raiz.esq)
            return self.rotaDir(raiz)
        # Rotação Dupla à Esquerda.
        if balance < -1 and dado.key < raiz.dir.dado.key:
            print('Rotação dupla à esquerda\n')
            raiz.dir = self.rotaDir(raiz.dir)
            return self.rotaEsq(raiz)
        return raiz

    # Rotina para verificar a altura da Árvore.
    def tam(self, raiz=0):
        if raiz == 0:
            raiz= self.node

        if raiz != None:
            return raiz.altura
        else:
            return 0
    
    # Rotina para calculo do Fator de Balanceamento.
    def fatorBalance(self, raiz):
        if raiz != None:
            return self.tam(raiz.esq) - self.tam(raiz.dir)
        else:
            return 0        
        
    
    # Rotina para Rotação Simples à Direita.
    def rotaDir(self, raiz):
        aux = raiz.esq
        raiz.esq = aux.dir
        aux.dir = raiz
        raiz.altura = 1 + max(self.tam(raiz.esq), self.tam(raiz.dir))
        aux.altura = 1 + max(self.tam(aux.esq), self.tam(aux.dir))
        return aux

    # Rotina para Rotação Simples à ESquerda.
    def rotaEsq(self, raiz):
        aux = raiz.dir
        raiz.dir = aux.esq
        aux.esq = raiz
        raiz.altura = 1 + max(self.tam(raiz.esq), self.tam(raiz.dir))
        aux.altura = 1 + max(self.tam(aux.esq), self.tam(aux.dir))
        return aux
        
    # Rotina que fornece as chaves na sequência para desenhar a Árvore AVL.
    def preOrdem(self, raiz):
        if raiz != None:
            print('{}, '.format(raiz.key), end='')
            self.preOrdem(raiz.esq)
            self.preOrdem(raiz.dir)

    def addDado(self,dado):
        raiz = None
        for i in dado:
            raiz = self.inserir(raiz, i)
        print('Altura da árvore: {}\n'.format(raiz.altura))
        print('Chaves da Árvore AVL:') 
        self.preOrdem(raiz)
        print()
        self.node = raiz

    def Buscar(self,key,provedor,raiz = 0):

        if self.node == None:
            raise treeExceptionL('Não há nenhum nó na arvore.')
        
        if raiz == 0:
            raiz = self.node

        if raiz.key == key:
            return raiz
        elif key < raiz.key:
            return self.Buscar(key,provedor,raiz.esq)
        else:
            return self.Buscar(key,provedor,raiz.dir)



    def printTree(self, node = 0, level =0):
        if self.node == None:
            raise treeExceptionL('Não há nenhum nó na arvore.')

        if node == 0:
            node = self.node
        if node != None:
            self.printTree(node.dir, level + 1)
            print(' ' * 4 * level + '->', node.key)
            self.printTree(node.esq, level + 1)

    def inorderTraversal(self, root=0):
        if self.node == None:
            raise treeExceptionL('Não há nenhum nó na arvore.')

        if root == 0:
            root = self.node
        res = []
        if root:
            res = self.inorderTraversal(root.esq)
            res.append(root.dado.display())
            res = res + self.inorderTraversal(root.dir)
        res.sort()
        return res   

    

