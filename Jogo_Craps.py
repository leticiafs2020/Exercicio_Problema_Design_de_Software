#Design de Software - Exercício Problema 1 
#Jogo Craps Insper
#Criadora: Letícia Sanchez
#Esse programa permite fazer mais de uma aposta por vez


import random
import time

#Apresentação inicial e das regras das apostas
print("Olá")
time.sleep(1)
nome = input("Qual o seu nome?")
time.sleep(1)
print("Bem-vindo(a) ao Craps, {0}!".format(nome))
time.sleep(1)
print("Farei uma simples apresentação das regras das apostas:")
time .sleep(1)
print("Em Any Craps, se você apostar e a soma de dados der 2, 3 ou 12, você ganha sete vezes o que apostou!")
time.sleep(3)
print("Se sair qualquer outro número, você perde o que apostou.")
time.sleep(2)
print("Em Field, se a soma de dados der 5, 6, 7 ou 8, você perde o que apostou, se der 3 , 4, 9, 10 ou 11, você ganha o que apostou!")
time.sleep(4)
print("Se sair 2, você ganha o dobro, se der 12, você ganha o triplo do que apostou!")
time.sleep(3)
print("Em Twelve, se a soma dos dados der 12, você ganha 30 vezes o que apostou!")
time.sleep(2)
print("Se sair qualquer outro número você perde o que apostou." )
time.sleep(3)
print("Em Pass Line Bet, você só pode fazê-la apenas na fase 'Come Out'. ")
time.sleep(2)
print("Se a soma de dados der 2, 3 ou 12, você perde o que apostou.")
time.sleep(2)
print("Se der 7 ou 11, você mantém o valor da aposta e ganha mais o valor dela.")
time.sleep(3)
print("Se der qualquer outro número, você entra na fase 'Point'.")
time.sleep(4)
print("Nela, você poderá apostar apenas Any Craps, Field e Twelve." )
time.sleep(2)
print("A aposta já feita continua valendo, porém, o valor tirado se torna o Point.")
time.sleep(3)
print("E para o jogador ganhar agora, a soma do novo lançamento dos dados deve ser igual ao do Point.")
time.sleep(3)
print("Se isso acontecer, o jogador ganha o mesmo valor que apostou.")
time.sleep(3)
print("Se sair 7, o jogador perde o que apostou.")
time.sleep(2)
print("Caso saia qualquer outro número, se mantem na fase 'Point' sem perder ou ganhar.")
time.sleep (3)
print("E se continua lançando os dados até um veredito, quando sair ou o número do Point ou o 7, terminando essa rodada.")
time.sleep(5)
print("E assim iniciando novamente uma fase 'Come Out'.")
time.sleep(2)
#Iniciando o jogo
print("Bem, vamos ao jogo!")
time.sleep(1)
#Declaração de quantas fichas o jogador começa a partida 
fichas = 1000

#O jogador pode jogar enquanto tiver mais que zero fichas senão o jogo se encerra
while fichas > 0:
    print ('Você detém {0} fichas'.format(fichas))
    #Declaração de seguir no jogo ou sair, se ele sair o jogo se encerra
    seguir_ou_sair = input("Você deseja seguir no jogo ou sair? (Digite seguir ou sair): ")
    if seguir_ou_sair == "seguir":
        print("Você entrou na fase 'Come Out'") 
        Dado1 = random.randint(1,6)
        Dado2 = random.randint(1,6)
        soma_dos_dados = Dado1 + Dado2
        #Opções de aposta
        time.sleep(1)
        print("Você pode apostar em Any Craps, Field, Twelve e Pass Line Bet.")
        A = input('Deseja apostar em Any Craps? (Digite "s" ou "sim" / "n" ou "não"): ')
        F = input('Deseja apostar em Field? (Digite "s" ou "sim" / "n" ou "não"): ')
        T = input('Deseja apostar em Twelve? (Digite "s" ou "sim" / "n" ou "não"): ')
        P = input('Deseja apostar em Pass Line Bet? (Digite "s" ou "sim" / "n" ou "não"): ')