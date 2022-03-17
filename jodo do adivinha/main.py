print('**********************')
print('** JOGO DO ADIVINHA **')
print('**********************')

numero_secreto = 10

chute = int(input('Digite um número: '))
print('Você chutou o número {}'.format(chute))

acertou = chute == numero_secreto
maior = chute < numero_secreto
menor = chute > numero_secreto

if(acertou):
    print('Parabéns você acertou!! ')
elif(maior):
    print('Você errou, tente um número mais alto')
elif(menor):
    print('Você errou, tente um número mais baixo')
