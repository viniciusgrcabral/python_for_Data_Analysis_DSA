# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")


def chamarcalculadora():
    print("Selecione a operação desejada:\n\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Potência\n6-Raiz Quadrada\n0-Se deseja sair\n")
    global opcao 
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    elif opcao == 5:
        potencia()
    elif opcao == 6:
        raiz2()
    return chamarcalculadora
    
def soma():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    soma = numero1 + numero2
    print(f'{numero1} + {numero2} = {soma}')
    return soma

def subtracao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    subtracao = numero1 - numero2
    print(f'{numero1} - {numero2} = {subtracao}\n')
    return subtracao

def multiplicacao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    multiplicacao = numero1 * numero2
    print(f'{numero1} * {numero2} = {multiplicacao}\n')
    return multiplicacao

def divisao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    divisao = numero1 / numero2
    print(f'{numero1} / {numero2} = {divisao}\n')
    return divisao

def potencia():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    potencia = numero1 ** numero2
    print(f'{numero1} ** {numero2} = {potencia}\n')
    return potencia

def raiz2():
    numero = float(input("Digite o número para a raiz: "))
    erro = 0.0000001
    if numero >= 2:
        primeiroChute = numero/2
    elif numero < 0:
        print("Entrada inválida, não há raiz de números negativos")
    else:
        primeiroChute = numero
    chuteAtual = primeiroChute
    while abs(chuteAtual * chuteAtual - numero) > erro:
        novoChute = (chuteAtual + numero/chuteAtual)/2
        chuteAtual = novoChute
    print(f'√{numero} = {chuteAtual}')


while True:
    chamarcalculadora()
    if opcao == 0:
        break
    else:
        print('\nOpção inválida, tente novamente!\n')
    