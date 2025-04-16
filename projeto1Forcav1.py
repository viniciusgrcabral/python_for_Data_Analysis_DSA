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

chancesRestantes = 0

palavraAleatoria = random.choice(list(dicionarioPalavras.values()))

palavraOriginal = list(palavraAleatoria)

palavraEditada = ['_'] * len(palavraOriginal)


def selecionandoDificuldade (dificuldade):

    global chancesRestantes

    if dificuldade == 1:
        chancesRestantes = len(palavraOriginal) + 3
    elif dificuldade == 2:
        chancesRestantes = round(len(palavraOriginal) * 1.5)
    elif dificuldade == 3:
        chancesRestantes = len(set(palavraOriginal))


def Forca():
    
    global letrasDigitadas, letrasErradas, palavraComAcento

    palavraComAcento = getPalavraComAcento(palavraAleatoria)

    letrasDigitadas = []
    
    letrasErradas = []
    
    print('Bem vindo(a) ao jogo da forca das frutas!')
    time.sleep(2)

    dificuldade = int(input('\nSelecione uma dificuldade:\n\nFácil = Digite 1\nMédio = digite 2\nDifícil = digite 3\n\n'))

    time.sleep(3)

    print(f'\nAdivinhe a palavra abaixo:\n\n{''.join(palavraEditada).lower()}')
    time.sleep(1)

    selecionandoDificuldade(dificuldade)

    while True:
        
        global letraUsuario

        print(f'\nChances restantes: {chancesRestantes}')

        print(f'Letras erradas: {letrasErradas}\n')
        time.sleep(1)

        letraUsuario = str(input('Digite uma letra: '))

        avaliarEntrada(letraUsuario)

        time.sleep(1.5)

        if chancesRestantes <= 0:

            time.sleep(3)

            print("\nQue pena! Você perdeu!")
            print(f"A palavra era: '{palavraComAcento}'")

            break
        if palavraEditada == palavraOriginal:

            time.sleep(3)

            print(f"\nPARABÉNS, A PALAVRA ERA '{palavraComAcento}', VOCÊ GANHOU!!!")

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
        print(f'\n{mostrarLetra()}')


def mostrarLetra():
    global chancesRestantes
    acerto = False

    for i in range(len(palavraOriginal)):
        if letraUsuario.lower() == palavraOriginal[i].lower():
            palavraEditada[i] = palavraOriginal[i]
            acerto = True

            
    if acerto == False:
        chancesRestantes -= 1
        letrasErradas.append(letraUsuario)

    return ''.join(palavraEditada)
    

Forca()