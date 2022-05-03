import random

from arvoreEscopo import Arvore, No


class ArvoreAVL(Arvore, No):
    
    #  Inserindo um nó 
    def inserir(self, raiz, dado):

        # Encontrar o local corre e inserir o Nó
        if not raiz:
            return No(dado)
        elif dado < raiz.dado:
            raiz.esquerda = self.inserir(raiz.esquerda, dado)
        else:
            raiz.direita = self.inserir(raiz.direita, dado)

        raiz.altura = 1 + max(self.alturaMinMx(raiz.esquerda),
                              self.alturaMinMx(raiz.direita))

        # Atualizar o fator de balanceamento e balancear a árvore
        balanco_Fator = self.getBalanco(raiz)
        if balanco_Fator > 1:
            if dado < raiz.esquerda.dado:
                return self.rotacionaDireita(raiz)
            else:
                raiz.esquerda = self.rotacionaEsquerda(raiz.esquerda)
                return self.rotacionaDireita(raiz)

        if balanco_Fator < -1:
            if dado > raiz.direita.dado:
                return self.rotacionaEsquerda(raiz)
            else:
                raiz.direita = self.rotacionaDireita(raiz.direita)
                return self.rotacionaEsquerda(raiz)

        return raiz

    def rotacionaEsquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.esquerda = 1 + max(self.alturaMinMx(z.esquerda),
                           self.alturaMinMx(z.direita))
        y.altura = 1 + max(self.alturaMinMx(y.esquerda),
                           self.alturaMinMx(y.direita))
        return y


    def rotacionaDireita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.alturaMinMx(z.esquerda),
                           self.alturaMinMx(z.direita))
        y.height = 1 + max(self.alturaMinMx(y.esquerda),
                           self.alturaMinMx(y.direita))
        return y


    # Setando o balanço do Nó
    def getBalanco(self, raiz):
        if not raiz:
            return 0
        return self.alturaMinMx(raiz.esquerda) - self.alturaMinMx(raiz.direita)


if __name__ == "__main__":

    valor = random.sample(range(1, 100), 28)
    avl = ArvoreAVL()
    
    v = 0
    
    
    for v in valor:
        avl.__init__(v)


    avl.inOrdem()
    avl.preOrdem()
    avl.posOrdem()
    avl.alturaMinMx()


    




    
