import random
import time

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

erros = 0

palavraAleatoria = random.choice(list(dicionarioPalavras.values()))

palavraOriginal = list(palavraAleatoria)

palavraEditada = ['_'] * len(palavraOriginal)

def mostrarLetra():
    global erros
    acerto = False

    for i in range(len(palavraOriginal)):
        if letraUsuario.lower() == palavraOriginal[i].lower():
            palavraEditada[i] = palavraOriginal[i]
            acerto = True

            
    if acerto == False:
        erros += 1
        letrasErradas.append(letraUsuario)

    return ''.join(palavraEditada), print(mostrarForca(erros))

def mostrarForca (erros):

    global quantidadeDeErro
    quantidadeDeErro = [
    """
      _____
     |/    |
     |
     |
     |
     |
    _|___
    """,
    """
      _____
     |/    |
     |     0
     |
     |
     |
    _|___
    """,
    """
      _____
     |/    |
     |     0
     |     |
     |     | 
     |
    _|___
    """,
    """
      _____
     |/    |
     |     0
     |    \| 
     |     | 
     |
    _|___
    """,
    """
      _____
     |/    |
     |     0
     |    \|/
     |     | 
     |
    _|___
    """,
    """
      _____
     |/    |
     |     0
     |    \|/
     |     | 
     |    /
    _|___
    """,
    """
      _____
     |/    |
     |     0
     |    \|/
     |     | 
     |    / \ 
    _|___
    """,
    ]
    desenhoForca = quantidadeDeErro[erros]
    return desenhoForca


def Forca():
    
    global letrasDigitadas, letrasErradas, palavraComAcento

    palavraComAcento = getPalavraComAcento(palavraAleatoria)

    letrasDigitadas = []
    
    letrasErradas = []
    
    print('Bem vindo(a) ao jogo da forca das frutas!')
    time.sleep(2)

    print(f'\nAdivinhe a palavra abaixo:')
    time.sleep(2)

    print(mostrarForca(erros))

    

    while True:
        
        global letraUsuario

        time.sleep(1)

        print(f'{''.join(palavraEditada).lower()}')

        time.sleep(1)

        letraUsuario = str(input('\n\nDigite uma letra: '))
        
        avaliarEntrada(letraUsuario)

        time.sleep(1.5)

        if erros >= 6:

            time.sleep(2)

            print("\nQue pena! Você perdeu!")
            print(f"A palavra era: '{palavraComAcento}'")

            break

        if palavraEditada == palavraOriginal:

            time.sleep(2)

            print(f"\nPARABÉNS, A PALAVRA ERA: '{palavraComAcento}', VOCÊ GANHOU!!!")

            break

def getPalavraComAcento (palavraSemAcento):
    for k, v in dicionarioPalavras.items():
        if v == palavraAleatoria:
            return k

def avaliarEntrada(letraUsuario):
    if not letraUsuario.isalpha():           
        print('\nVocê precisa digitar uma letra! Tente novamente:')
    elif len(letraUsuario) > 1:
        print('\nVocê só pode digitar uma letra! Tente novamente:')
    elif letraUsuario in letrasDigitadas:
        print('\nVocê já digitou essa letra')
    else:
        letrasDigitadas.append(letraUsuario)
        time.sleep(1.5)
        mostrarLetra()







Forca()