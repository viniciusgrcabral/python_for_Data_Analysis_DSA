# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)

dicionarioPalavras = {'Cajá':'Caja', 
                      'Caju' : 'Caju', 
                      'Caqui' : 'Caqui', 
                      'Carambola': 'Carambola',
                      'Coco':'Coco', 
                      'Graviola':'Graviola', 
                      'Guaraná':'Guarana', 
                      'Jaca':'Jaca', 
                      'Jabuticaba':'Jabuticaba',
                      'Kiwi':'Kiwi', 
                      'Laranja':'Laranja', 
                      'Limão':'Limao', 
                      'Maçã':'Maça', 
                      'Mamão':'Mamao', 
                      'Manga':'Manga', 
                      'Maracujá':'Maracuja', 
                      'Melancia':'Melancia', 
                      'Melão':'Melao', 
                      'Morango':'Morango', 
                      'Pera':'Pera',
                      'Pitanga':'Pitanga', 
                      'Pêssego':'Pessego', 
                      'Pinha':'Pinha', 
                      'Pitaia':'Pitaia', 
                      'Pitomba':'Pitomba',
                      'Pindaíba':'Pindaiba', 
                      'Pegui':'Pequi', 
                      'Romã':'Roma', 
                      'Uva':'Uva'}

letrasDigitadas = []

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']



# Classe
class Hangman:

     
	# Método Construtor
     def __init__(self, palavra, palavraOriginal):
          
          self.palavra = list(palavra.lower())
          self.palavraOriginal = list(palavraOriginal)
          self.board = board
          self.boardAtual = board[0]
          self.contadorBoard = 0
          self.letrasDigitadas = []

     # Avaliar entrada
     def avaliarEntrada(self, letraUsuario):
          if not letraUsuario.isalpha():           
               print('\nVocê precisa digitar uma letra! Tente novamente:')
          elif len(letraUsuario) > 1:
               print('\nVocê só pode digitar uma letra! Tente novamente:')
          elif letraUsuario in self.letrasDigitadas:
               print('\nVocê já digitou essa letra: ', self.letrasDigitadas)
          else:
               self.letrasDigitadas.append(letraUsuario)
               print('\nLetras já digitadas', self.letrasDigitadas)
               self.entradaCorreta = True
               
     # Método para adivinhar a letra
     def adivinharLetra(self):
          self.entradaCorreta = False
          letraUsuario = str(input('\nDigite uma letra: ')).lower()
          self.avaliarEntrada(letraUsuario)
          for i in range(len(self.palavra)):
               if letraUsuario == self.palavra[i]:
                    self.palavraEscondida[i] = self.palavraOriginal[i]
          if letraUsuario not in self.palavra and self.entradaCorreta == True:
               self.contadorBoard += 1
               self.boardAtual = board[self.contadorBoard]
          print('\n',''.join(self.palavraEscondida))
          print(self.boardAtual)
          
               
	# Método para verificar se o jogo terminou
     def jogoTerminou (self):
          while True:
               self.adivinharLetra()
               if self.contadorBoard >= 6:
                    break
               elif ''.join(self.palavraEscondida) == ''.join(self.palavraOriginal):
                    break
          self.venceu()
          
	# Método para verificar se o jogador venceu
     def venceu (self):
          if self.boardAtual == board[6]:
               print('O jogo terminou, você perdeu!')
          else:
               print(f'Parabéns! Você venceu, a palavra era {"".join(self.palavraOriginal)}')

               
	# Método para não mostrar a letra no board
     def esconderPalavra(self):
          self.palavraEscondida = len(self.palavraOriginal) * ['_']
          return ''.join(self.palavraEscondida)
          
	# Método para checar o status do game e imprimir o board na tela
     def gameForca (self):
          print('\n',self.esconderPalavra())
          self.jogoTerminou()


     
palavraOriginal, palavraPadronizada = random.choice(list(dicionarioPalavras.items()))

forca = Hangman(palavraPadronizada, palavraOriginal)


forca.gameForca()





