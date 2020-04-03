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

        #Aposta Any Craps 
        if A == 'n' or A == 'não':
            pass
        else:
            #Declaracão de quanto será apostado em Any Craps
            valor_da_aposta1 = int(input('Quanto você deseja apostar em Any Craps? '))
            time.sleep(1)
            if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:  
                fichas = fichas + valor_da_aposta1 * 7
                print("Você ganhou sete vezes o que apostou, {0} fichas!".format(valor_da_aposta1 * 7))
                print ('Você detém {0} fichas'.format(fichas))
            else:
                fichas = fichas - valor_da_aposta1
                print("Você perdeu o que apostou!")
                print ('Você detém {0} fichas'.format(fichas))

        #Aposta Field
        if F == 'n' or F == 'não' :
            pass
        else:
            #Declaracão de quanto será apostado em Field
            valor_da_aposta2 = int(input('Quanto você deseja apostar em Field? '))
            time.sleep(1)
            if soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8 :
                fichas = fichas - valor_da_aposta2
                print("Você perdeu o que apostou!")
                print ('Você detém {0} fichas'.format(fichas))
            elif soma_dos_dados == 3 or soma_dos_dados == 4 or soma_dos_dados == 9 or soma_dos_dados == 10 or soma_dos_dados == 11:
                fichas = fichas + valor_da_aposta2
                print("Você ganhou o que apostou!")
                print ('Você detém {0} fichas'.format(fichas))
            elif soma_dos_dados == 2:
                fichas = fichas + 2 * valor_da_aposta2
                print("Você ganhou o dobro do que apostou, {0} fichas!". format(valor_da_aposta2 * 2))
                print ('Você detém {0} fichas'.format(fichas))
            else:
                fichas = fichas + 3 * valor_da_aposta2
                print("Você ganhou o triplo do que apostou, {0} fichas!".format(valor_da_aposta2 * 3))
                print ('Você detém {0} fichas'.format(fichas))

        #Aposta Twelve
        if T == 'n' or T == 'não':
            pass
        else:
            #Declaracão de quanto será apostado em Twelve
            valor_da_aposta3 = int(input('Quanto você deseja apostar em Twelve? '))
            time.sleep(1)
            if soma_dos_dados == 12:
                fichas = fichas + valor_da_aposta3 * 30
                print("Você ganhou trinta vezes o que apostou, {0} fichas!". format(valor_da_aposta3 * 30))
                print ('Você detém {0} fichas'.format(fichas))
            else:
                fichas = fichas - valor_da_aposta3
                print("Você perdeu o que apostou!")
                print ('Você detém {0} fichas'.format(fichas))

        #Aposta Pass Line Bet
        if P == 'n' or P == 'nao':
            pass
        else:
            valor_da_aposta4 = int(input('Quanto você deseja apostar em Pass Line Bet? '))
            time.sleep(1)
            if soma_dos_dados == 7 or soma_dos_dados == 11:
                fichas = fichas + valor_da_aposta4 * 2
                print("Você ganhou o dobro do que apostou, fichas {0}!".format(valor_da_aposta4 * 2))
                print ('Você detém {0} fichas'.format(fichas))
            elif soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                fichas = fichas - valor_da_aposta4
                print("Você perdeu o que apostou!")
                print ('Você detém {0} fichas'.format(fichas))
            else:
                #Entrando na fase Point pois a soma dos dados foi 4,5,6,8,9 ou 10 
                Point = True
                print('Você entrou na fase Point!')
                while Point:
                    time.sleep(1)
                    print ('Você detém {0} fichas'.format(fichas))
                    Dado3 = random.randint(1,6)
                    Dado4 = random.randint(1,6)
                    soma_dos_dados2 = Dado3 + Dado4
                    time.sleep(1)
                    A_p = input('Você quer apostar em Any Craps? (Digite "s" ou "sim" / "n" ou "não"): ') 
                    F_p= input('Você quer apostar em Field? (Digite "s" ou "sim" / "n" ou "não"): ')
                    T_p = input('Você quer apostar em Twelve? (Digite "s" ou "sim" / "n" ou "não"): ')

                    #Aposta Any Craps em Point
                    if A_p == 'n':
                        pass
                    else:
                        #Declaração de quanto quer apostar em Any Craps na Point
                        valor_da_aposta_p1 = int(input('Quantas fichas você quer apostar em Any Craps? '))
                        time.sleep(1)
                        if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                            fichas = fichas + valor_da_aposta_p1 * 7
                            print("Você ganhou sete vezes o que apostou, {0} fichas!".format(valor_da_aposta_p1 * 7))
                            print ('Você detém {0} fichas'.format(fichas))
                        else:
                            fichas = fichas - valor_da_aposta_p1
                            print("Você perdeu o que apostou!")
                            print ('Você detém {0} fichas'.format(fichas))

                    #Aposta Field em Point  
                    if F_p == 'n':
                        pass
                    else:
                        #Declaração de quanto apostar em Field na Point
                        valor_da_aposta_p2 = int(input('Quantas fichas você quer apostar em Field? '))
                        time.sleep(1)
                        if soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                            fichas = fichas - valor_da_aposta_p2
                            print("Você perdeu o que apostou!")
                            print ('Você detém {0} fichas'.format(fichas))
                        elif soma_dos_dados2 == 3 or soma_dos_dados2 == 4 or soma_dos_dados2 == 9 or soma_dos_dados2 == 10 or soma_dos_dados2 == 11:
                            fichas = fichas + valor_da_aposta_p2
                            print("Você ganhou o que apostou!")
                            print ('Você detém {0} fichas'.format(fichas))
                        elif soma_dos_dados2 == 2:
                            fichas = fichas + 2 * valor_da_aposta_p2
                            print("Você ganhou o dobro do que apostou, {0} fichas!".format(valor_da_aposta_p2 * 2))
                            print ('Você detém {0} fichas'.format(fichas))
                        else:
                            fichas = fichas + 3 * valor_da_aposta_p2
                            print("Você ganhou o triplo do que apostou, {0} fichas!".format(valor_da_aposta_p2 * 3))
                            print ('Você detém {0} fichas'.format(fichas))
                            
                    #Aposta Twelve em Point
                    if T_p == 'n':
                        pass
                    else:
                        #Declaração de quanto apostar em Twelve na Point
                        valor_da_aposta_p3 = int(input('Quantas fichas você quer apostar em Twelve? '))
                        time.sleep(1)
                        if soma_dos_dados2 == 12:
                            fichas = fichas + valor_da_aposta_p3 * 30
                            print("Você ganhou trinta vezes o que apostou, {0} fichas!".format(valor_da_aposta_p3 * 30))
                            print ('Você detém {0} fichas'.format(fichas))
                        else:
                            fichas = fichas - valor_da_aposta_p3
                            print("Você perdeu o que apostou!")
                            print ('Você detém {0} fichas'.format(fichas))

                     #Soma dos Dados       
                    print('Saiu na primeira soma: {0}'.format(soma_dos_dados))
                    print("Saiu na segunda soma: {0}".format(soma_dos_dados2))