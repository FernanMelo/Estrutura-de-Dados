

class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1  

    # Nessa clase de arvore binaria nós podemos construir ela passando inicialmente um dado vazio, 
    # caso tenha algo no dado ela se torna raiz      
class Arvore:  
      
    def __init__(self, dado=None, node=None):
        
        if node:
              self.raiz = node

        if dado:
            node = No(dado)
            self.raiz = node
        else:
            self.raiz = None     
       
    
    #Percurso em ordem simétrica
    def inOrdem(self, node=None):
      
      if node is None:
        node = self.raiz
            
      if node.esquerda:
        self.inOrdem(node.esquerda)
        print(node)
      
      if node.direita:
        self.inOrdem(node.direita)
    
   #Percuso de pós-ordem (olha para todas as arvores) visita a raiz verificando se à sub-arvore sempre analisando da
   #Esquerda para a direita e printa na tela sua folha depois sua raizes.
    def posOrdem(self, node=None):
      
      if node is None:
         node = self.raiz
            
      if node.esquerda:
        self.posOrdem(node.esquerda)
      
      if node.direita:
        self.posOrdem(node.direita)
        print(node)

   # Percurso pré ordem mostrando Profundidade
    def preOrdem(self, node=None):
      
      if node is None:
        node = self.raiz
        print(node)  
      if node.esquerda:
        self.preOrdem(node.esquerda)
      
      if node.direita:
        self.preOrdem(node.direita)
     
      
 
   # Funçao pra ver se a arvore está cheia 
    def isCheioORVazio(self, dado):
      
            if dado:
                  print('Arvore Cheia')
            else:
                  self.__init__(dado)
    
    # Altura dos NO 1 log(n)
    def alturaMinMx(self, node=None):
         
         if node is None:
               node = self.raiz
         
         al_esquerda = 0
         al_direita = 0

         if node.esquerda:
               al_esquerda = self.alturaMinMx(node.esquerda)
         
         if node.direita:
               al_direita = self.alturaMinMx(node.direita)

         if al_direita > al_esquerda:
               return al_direita + 1
         
         return al_esquerda + 1

     
class ArvoreBinariaBusca(Arvore, No): 
      
      def buscaBinaria(self, valor, node=None):
            
            if node == 0:
               node = self.raiz
            
            if node is None or node.dado == valor:
                return ArvoreBinariaBusca(node)
            
            if valor < self.dado:
                return buscaBinaria(valor, node.esquerda)
            
            return buscaBinaria(valor, node.direita)
            
          
                 


            
   

   



