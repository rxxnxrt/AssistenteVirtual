#Você precisa programar um Assistente Pessoal Virtual que vai tomar decisões por você durante um dia cheio.
#Esse assistente precisa responder a três situações:
#1. Hora de acordar (Decisão)
#2. Escolha do transporte (Decisão)
#3. Check-list do dia (Repetição)

print('\033[1:36m-=\033[m' * 9)
print('\033[1:36:40mASSISTENTE VIRTUAL\033[m')
print('\033[1:36m-=\033[m' * 9)
while True:
    horas = int(input('\033[1:35mASSISTENTE:\033[m Olá! Que horas são agora? '))
    if 0 <= horas <= 24:
        break
    else:
        print("Formato invalido! Por gentileza digite um horário valido [0-24]: ")

if horas <= 6:
    print('\033[1:35mASSISTENTE:\033[m Muito cedo para acordar, volte a dormir.')
elif horas > 6 and horas <= 8:
    print('\033[1:35mASSISTENTE:\033[m Hora de levantar e começar o dia!')
else:
    print('\033[1:35mASSISTENTE:\033[m Você está atrasado! Levante agora!')
print('\033[1:36m-=\033[m' * 29)

distancia = int(input('\033[1:35mASSISTENTE:\033[m Qual a distância da sua casa até a faculdade? '))
if distancia <= 2:
    print('\033[1:35mASSISTENTE:\033[m Vá a pé.')
elif distancia > 2 and distancia <= 10:
    print('\033[1:35mASSISTENTE:\033[m Use bicicleta ou ônibus.')
else:
    print('\033[1:35mASSISTENTE:\033[m Use carro ou transporte por app.')
print('\033[1:36m-=\033[m' * 28)

while True:
    pergunta = str(input('\033[1:35mASSISTENTE:\033[m Você terminou todas as tarefas do dia? [S/N]: ')).strip().upper()[0]
    if pergunta == 'S':
        print('\033[1:35mASSISTENTE:\033[m Parabéns dia concluido!')
        print('\033[1:36m-=\033[m' * 28)
        break

    elif pergunta == 'N':
        continue
    else:
        print('\033[1:35mASSISTENTE:\033[m Formato invalido! Por gentileza responda com [S/N]: ')
