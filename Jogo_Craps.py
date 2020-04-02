#Design de Software - Exercício Problema 1 
#Jogo Craps Insper
#Criadora: Letícia Sanchez

import random

print("Olá")

nome = input("Qual o seu nome?")

print("Bem-vindo(a) ao Craps, {0}!".format(nome))

# Cada jogador começa cada um com 1000 fichas - Declaração de fichas
fichas = 1000

while fichas != 0:
    print('Você detém {0} fichas.'.format(fichas))
    #Declaração de Seguir no jogo ou Sair
    seguir_no_jogo_ou_sair = input('Você deseja seguir no jogo ou sair. (Digite Seguir ou Sair): ')
    if seguir_no_jogo_ou_sair == 'Seguir':
        quantidade_de_apostas= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3 ou 4) "))
        if quantidade_de_apostas == 1:
            print('Começa agora a fase "Come Out"!') 
            print('Você pode escolher entre quatro opções de aposta: Pass Line Bet, Any Craps, Field, Twelve.') #Declaração de opções de apostas e escolha
            aposta = input('Qual delas você escolherá?: ')
            
            # Aposta "Any Craps" sozinha
            if aposta == 'Any Craps':   
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                    print('Você ganhou sete vezes a quantidade de fichas apostada!')
                    fichas = fichas + valor_da_aposta * 7
                else:
                    print('Você perdeu!')
                    fichas =  fichas - valor_da_aposta

            #Aposta "Twelve" sozinha
            if aposta == 'Twelve':
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 12:
                    print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                    fichas = fichas + valor_da_aposta * 30
                else:
                    print('Você perdeu!')
                    fichas = fichas - valor_da_aposta

            #Aposta "Field" sozinha
            if aposta == 'Field':
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 12:
                    print('Você ganhou o triplo da quantidade de fichas que apostou!')
                    fichas = fichas + valor_da_aposta * 3
                elif soma_dos_dados == 2:
                    print('Você ganhou o dobro da quantidade de fichas que apostou!')
                    fichas = fichas + valor_da_aposta * 2
                elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                    print('Você perdeu tudo que tinha!')
                    fichas = fichas - valor_da_aposta
                else:
                    print('Você ganhou a mesma quantidade que apostou!')
                    fichas = fichas + valor_da_aposta

            #Aposta "Pass Line Bet" sozinha
            if aposta == 'Pass Line Bet':
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 7 or soma_dos_dados == 11:
                    print('Você mantém as fichas apostadas e recebe a mesma quantia apostada!')
                    fichas = fichas + valor_da_aposta * 2
                elif soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                    print('Você perdeu o que apostou!')
                    fichas = fichas - valor_da_aposta

                #Início fase "Point" sozinha - (a soma dos dados em Pass Line Bet deram 4,5, 6, 8, 9 ou 10)
                else:
                    print('Você entrou na fase Point!')
                    Point = True
                    while Point and fichas != 0:
                        print('Você detém {0} fichas.'.format(fichas))
                        quantidade_de_apostas2= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3) "))
                        if quantidade_de_apostas2 == 1:
                            print("Dentre as opções de aposta temos: Any Craps, Field e Twelve")
                            aposta_p = input("Qual delas você escolherá?: ")
                            #Aposta "Any Craps" sozinha na Fase Point
                            if aposta_p == 'Any Craps':   
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                                    print('Você ganhou sete vezes a quantidade de fichas apostada!')
                                    fichas = fichas + valor_da_aposta2 * 7
                                else:
                                    print('Você perdeu o que apostou!')
                                    fichas =  fichas - valor_da_aposta2

                            #Aposta "Twelve" sozinha na Fase Point
                            if aposta_p == 'Twelve':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 30
                                else:
                                    print('Você perdeu!')
                                    fichas = fichas - valor_da_aposta2

                            #Aposta "Field" sozinha na Fase Point
                            if aposta_p == 'Field':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou o triplo da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 3
                                elif soma_dos_dados2 == 2:
                                    print('Você ganhou o dobro da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print('Você perdeu tudo que apostou!')
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print('Você ganhou a mesma quantidade que apostou!')
                                    fichas = fichas + valor_da_aposta2
                        
                        if quantidade_de_apostas2 == 2:
                            print("Dentre as opções de aposta temos:")
                            print("Any Craps e Field")
                            print("Any Craps e Twelve")
                            print("Field e Twelve")
                            aposta_p2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
                            #Apostas Any Craps e Field juntas na Point
                            if aposta_p2 == "Any Craps e Field":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2:
                                    print("Você ganhou nove vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 9
                                elif soma_dos_dados2 == 3:
                                    print("Você ganhou oito vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 8
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print ("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém sua quantidade de fichas.")
                                    fichas = fichas
                            #Apostas Any Craps e Twelve juntas na Point
                            if aposta_p2 == "Any Craps e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e sete vezes o que apostou! ")
                                    fichas = fichas + valor_da_aposta2 * 37
                                elif soma_dos_dados2 == 2 or soma_dos_dados2 == 3:
                                    print("Você ganhou seis vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 6
                                else:
                                    print("Você perdeu o dobro do que apostou!")
                                    fichas = fichas - valor_da_aposta2 * 2
                            #Apostas Field e Twelve juntas na Point
                            if aposta_p2 == "Field e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e três vezes o que apostou!")
                                    fichas = fichas +valor_da_aposta2*33
                                elif soma_dos_dados2 == 2:
                                    print("Você ganhou o que apostou!")
                                    fichas = fichas + valor_da_aposta2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém a quantidade de fichas!")
                                    fichas = fichas

                        if quantidade_de_apostas2 == 3:
                            print("Você fará as três apostas de uma vez só Any Craps, Field e Twelve.")
                            #Apostas Any Craps, Field e Twelve juntas na Point
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou quarenta vezes o que apostou!")
                                fichas = fichas +valor_da_aposta2 * 40
                            elif soma_dos_dados2 == 3:
                                print("Você ganhou o triplo do que apostou!")
                                fichas = fichas + valor_da_aposta2 * 3
                            elif soma_dos_dados2 == 2:
                                print("Você ganhou oito vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 8
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print("Você perdeu tudo que apostou!")
                                fichas = fichas = valor_da_aposta2
                            else:
                                print("Você perdeu o que apostou!")
                                fichas = fichas - valor_da_aposta2
                        #Condições da Fase Point
                        if soma_dos_dados2 == soma_dos_dados:
                            print('Você ganhou!')
                            fichas = fichas + valor_da_aposta
                            Point = False

                        elif soma_dos_dados2 == 7:
                            print('Você perdeu tudo!')
                            fichas = fichas - valor_da_aposta
                            Point = False

                        else:
                            print ('Reiniciando fase!')
                            Point = True

                        print('Você detém {0} fichas.'.format(fichas))


        if quantidade_de_apostas == 2 :
            print('Começa agora a fase "Come Out"')
            print("Dentre as opções de aposta temos:")
            print("Any Craps e Field")
            print("Any Craps e Pass Line Bet")
            print("Any Craps e Twelve")
            print("Field e Pass Line Bet")
            print("Field e Twelve")
            print("Pass Line Bet e Twelve")
            aposta2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
            #Apostas Any Craps e Field juntas
            if aposta2 == "Any Craps e Field":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 2:
                    print("Você ganhou nove vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 9
                elif soma_dos_dados == 3:
                    print("Você ganhou oito vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 8
                elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                    print ("Você perdeu tudo que apostou!")
                    fichas = fichas - valor_da_aposta
                else:
                    print("Você mantém sua quantidade de fichas!")
                    fichas = fichas
            #Apostas Any Craps e Twelve juntas
            if aposta2 == "Any Craps e Twelve":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 12:
                    print("Você ganhou trinta e sete vezes o que apostou! ")
                    fichas = fichas + valor_da_aposta * 37
                elif soma_dos_dados == 2 or soma_dos_dados == 3:
                    print("Você ganhou seis vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 6
                else:
                    print("Você perdeu o dobro do que apostou!")
                    fichas = fichas - valor_da_aposta*2
            #Apostas Any Craps e Pass Line Bet juntas
            if aposta2 == "Any Craps e Pass Line Bet":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                    print("Você ganhou seis vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 6
                elif soma_dos_dados == 7 or soma_dos_dados == 11:
                    print("Você ganhou a aposta!")
                    fichas = fichas + valor_da_aposta
                else: 
                    print("Você perdeu o que apostou pelo Any Craps e entrou na fase Point!")
                    fichas = fichas - valor_da_aposta
                    Point = True
                    while Point and fichas != 0:
                        print('Você detém {0} fichas.'.format(fichas))
                        quantidade_de_apostas2= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3) "))
                        if quantidade_de_apostas2 == 1:
                            print("Dentre as opções de aposta temos: Any Craps, Field e Twelve.")
                            aposta_p = input("Qual delas você escolherá?: ")
                            #Aposta Any Craps sozinha na Fase Point
                            if aposta_p == 'Any Craps':   
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                                    print('Você ganhou sete vezes a quantidade de fichas apostada!')
                                    fichas = fichas + valor_da_aposta2 * 7
                                else:
                                    print('Você perdeu!')
                                    fichas =  fichas - valor_da_aposta2

                            #Aposta "Twelve" sozinha na Fase Point
                            if aposta_p == 'Twelve':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 30
                                else:
                                    print('Você perdeu!')
                                    fichas = fichas - valor_da_aposta2

                            #Aposta "Field" sozinha na Fase Point
                            if aposta_p == 'Field':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou o triplo da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 3
                                elif soma_dos_dados2 == 2:
                                    print('Você ganhou o dobro da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print('Você perdeu tudo que apostou!')
                                    fichas = fichas - valor_da_aposta2 
                                else:
                                    print('Você ganhou a mesma quantidade que apostou!')
                                    fichas = fichas + valor_da_aposta2
                        
                        if quantidade_de_apostas2 == 2:
                            print("Dentre as opções de aposta temos:")
                            print("Any Craps e Field")
                            print("Any Craps e Twelve")
                            print("Field e Twelve")
                            aposta_p2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
                            #Apostas Any Craps e Field juntas na Fase Point
                            if aposta_p2 == "Any Craps e Field":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2:
                                    print("Você ganhou nove vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 9
                                elif soma_dos_dados2 == 3:
                                    print("Você ganhou oito vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 8
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print ("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém sua quantidade de fichas.")
                                    fichas = fichas
                            #Apostas Any Craps e Twelve juntas na Fase Point
                            if aposta_p2 == "Any Craps e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e sete vezes o que apostou ")
                                    fichas = fichas + valor_da_aposta2 * 37
                                elif soma_dos_dados2 == 2 or soma_dos_dados2 == 3:
                                    print("Você ganhou seis vezes o que apostou.")
                                    fichas = fichas + valor_da_aposta2 * 6
                                else:
                                    print("Você perdeu o dobro do que apostou.")
                                    fichas = fichas - valor_da_aposta2*2
                            #Apostas Field e Twelve juntas na Fase Point
                            if aposta_p2 == "Field e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e três vezes o que apostou!")
                                    fichas = fichas +valor_da_aposta2 * 33
                                elif soma_dos_dados2 == 2:
                                    print("Você ganhou o que apostou!")
                                    fichas = fichas + valor_da_aposta2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantem a quantidade de fichas.")
                                    fichas = fichas

                        if quantidade_de_apostas2 == 3:
                            print("Você fará as três apostas de uma vez só")
                            #Apostas Any Craps, Field e Twelve na Fase Point
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou quarenta vezes o que apostou!")
                                fichas = fichas +valor_da_aposta2 * 40
                            elif soma_dos_dados2 == 3:
                                print("Você ganhou o triplo do que apostou!")
                                fichas = fichas + valor_da_aposta2 * 3
                            elif soma_dos_dados2 == 2:
                                print("Você ganhou oito vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 8
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print("Você perdeu tudoque apostou!")
                                fichas = fichas - valor_da_aposta2
                            else:
                                print("Você perdeu o que apostou!")
                                fichas = fichas - valor_da_aposta2
                        #Condições da Fase Point
                        if soma_dos_dados2 == soma_dos_dados:
                            print('Você ganhou!')
                            fichas = fichas + valor_da_aposta
                            Point = False

                        elif soma_dos_dados2 == 7:
                            print('Você perdeu tudo!')
                            fichas = fichas - valor_da_aposta
                            Point = False

                        else:
                            print ('Reiniciando fase!')
                            Point = True

                        print('Você detém {0} fichas.'.format(fichas))

            #Apostas Field e Pass Line Bet juntas
            if aposta2 == "Field e Pass Line Bet":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados==5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                    print("Você entraria na fase Point mas perdeu tudo qua apostou pelo Field")
                    fichas = fichas - valor_da_aposta
                elif soma_dos_dados == 11:
                    print("Você ganhou o triplo do que apostou!")
                    fichas = fichas + valor_da_aposta * 3
                elif soma_dos_dados == 12:
                    print("Você ganhou o dobro do que apostou!")
                    fichas = fichas + valor_da_aposta * 2
                elif soma_dos_dados == 2:
                    print("Você ganhou o que apostou!")
                    fichas = fichas + valor_da_aposta
                else:
                    print("Você ganhou o que apostou pelo Field mas entrou na fase Point!")
                    fichas = fichas + valor_da_aposta
                    Point = True
                    while Point and fichas != 0:
                        print('Você detém {0} fichas.'.format(fichas))
                        quantidade_de_apostas2= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3) "))
                        if quantidade_de_apostas2 == 1:
                            print("Dentre as opções de aposta temos: Any Craps, Field e Twelve.")
                            aposta_p = input("Qual delas você escolherá?: ")
                            #Aposta Any Craps sozinha na Fase Point
                            if aposta_p == 'Any Craps':   
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                                    print('Você ganhou sete vezes a quantidade de fichas apostada!')
                                    fichas = fichas + valor_da_aposta2 * 7
                                else:
                                    print('Você perdeu!')
                                    fichas =  fichas - valor_da_aposta2

                            #Aposta "Twelve" sozinha na Fase Point
                            if aposta_p == 'Twelve':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 30
                                else:
                                    print('Você perdeu!')
                                    fichas = fichas - valor_da_aposta2

                            #Aposta "Field" sozinha na Fase Point
                            if aposta_p == 'Field':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou o triplo da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 3
                                elif soma_dos_dados2 == 2:
                                    print('Você ganhou o dobro da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print('Você perdeu tudo que apostou!')
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print('Você ganhou a mesma quantidade que apostou!')
                                    fichas = fichas + valor_da_aposta2
                        
                        if quantidade_de_apostas2 == 2:
                            print("Dentre as opções de aposta temos:")
                            print("Any Craps e Field")
                            print("Any Craps e Twelve")
                            print("Field e Twelve")
                            aposta_p2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
                            #Apostas Any Craps e Field juntas na Fase Point
                            if aposta_p2 == "Any Craps e Field":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2:
                                    print("Você ganhou nove vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 9
                                elif soma_dos_dados2 == 3:
                                    print("Você ganhou oito vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 8
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print ("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém sua quantidade de fichas.")
                                    fichas = fichas
                            #Apostas Any Craps e Twelve juntas na Fase Point
                            if aposta_p2 == "Any Craps e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e sete vezes o que apostou ")
                                    fichas = fichas + valor_da_aposta2 * 37
                                elif soma_dos_dados2 == 2 or soma_dos_dados2 == 3:
                                    print("Você ganhou seis vezes o que apostou.")
                                    fichas = fichas + valor_da_aposta2 * 6
                                else:
                                    print("Você perdeu o dobro do que apostou.")
                                    fichas = fichas - valor_da_aposta2 * 2
                            #Apostas Field e Twelve juntas na Fase Point
                            if aposta_p2 == "Field e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e três vezes o que apostou!")
                                    fichas = fichas +valor_da_aposta2 * 33
                                elif soma_dos_dados2 == 2:
                                    print("Você ganhou o que apostou!")
                                    fichas = fichas + valor_da_aposta2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print("Você perdeu tudoque apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém a quantidade de fichas.")
                                    fichas = fichas

                        if quantidade_de_apostas2 == 3:
                            print("Você fará as três apostas de uma vez só")
                            #Apostas Any Craps, Field e Twelve juntas na Fase Point
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou quarenta vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 40
                            elif soma_dos_dados2 == 3:
                                print("Você ganhou o triplo do que apostou!")
                                fichas = fichas + valor_da_aposta2 * 3
                            elif soma_dos_dados2 == 2:
                                print("Você ganhou oito vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2*8
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print("Você perdeu tudou que apostou!")
                                fichas = fichas - valor_da_aposta2
                            else:
                                print("Você perdeu o que apostou!")
                                fichas = fichas - valor_da_aposta2
                        #Condições da Fase Point
                        if soma_dos_dados2 == soma_dos_dados:
                            print('Você ganhou!')
                            fichas = fichas + valor_da_aposta
                            Point = False

                        elif soma_dos_dados2 == 7:
                            print('Você perdeu tudo!')
                            fichas = fichas - valor_da_aposta
                            Point = False

                        else:
                            print ('Reiniciando fase!')
                            Point = True

                        print('Você detém {0} fichas.'.format(fichas))

            #Apostas Field e Twelve juntas
            if aposta2 == "Field e Twelve":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 12:
                    print("Você ganhou trinta e três vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 33
                elif soma_dos_dados == 2:
                    print("Você ganhou o que apostou!")
                    fichas = fichas + valor_da_aposta
                elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                    print("Você perdeu tudo que apostou!")
                    fichas = fichas - valor_da_aposta
                else:
                    print("Você mantém a quantidade de fichas.")
                    fichas = fichas
            #Apostas Pass Line Bet e Twelve juntas
            if aposta2 == "Pass Line Bet e Twelve":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 12:
                    print("Você ganhou vinte e nove vezes o que apostou!.")
                    fichas = fichas + valor_da_aposta * 29
                elif soma_dos_dados == 2 or soma_dos_dados == 3:
                    print("Você perdeu o dobro do que apostou!")
                    fichas = fichas - valor_da_aposta * 2
                elif soma_dos_dados == 7 or soma_dos_dados == 11:
                    print("Você ganhou o que apostou!")
                    fichas = fichas + valor_da_aposta
                else:
                    print("Você perdeu o que apostou pela Twelve e entrou na fase Point")
                    fichas = fichas - valor_da_aposta
                    Point = True
                    while Point and fichas != 0:
                        print('Você detém {0} fichas.'.format(fichas))
                        quantidade_de_apostas2= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3) "))
                        if quantidade_de_apostas2 == 1:
                            print("Dentre as opções de aposta temos: Any Craps, Field e Twelve.")
                            aposta_p = input("Qual delas você escolherá?: ")
                            #Aposta Any Craps sozinha na Fase Point
                            if aposta_p == 'Any Craps':   
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                                    print('Você ganhou sete vezes a quantidade de fichas apostada!')
                                    fichas = fichas + valor_da_aposta2 * 7
                                else:
                                    print('Você perdeu!')
                                    fichas =  fichas - valor_da_aposta2

                            #Aposta "Twelve" sozinha na Fase Point
                            if aposta_p == 'Twelve':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 30
                                else:
                                    print('Você perdeu!')
                                    fichas = fichas - valor_da_aposta2

                            #Aposta "Field" sozinha na Fase Point
                            if aposta_p == 'Field':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou o triplo da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 3
                                elif soma_dos_dados2 == 2:
                                    print('Você ganhou o dobro da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print('Você perdeu tudo que apostou!')
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print('Você ganhou a mesma quantidade que apostou!')
                                    fichas = fichas + valor_da_aposta2
                        
                        if quantidade_de_apostas2 == 2:
                            print("Dentre as opções de aposta temos:")
                            print("Any Craps e Field")
                            print("Any Craps e Twelve")
                            print("Field e Twelve")
                            aposta_p2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
                            #Apostas Any Craps e Field juntas na Fase Point
                            if aposta_p2 == "Any Craps e Field":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2:
                                    print("Você ganhou nove vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 9
                                elif soma_dos_dados2 == 3:
                                    print("Você ganhou oito vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 8
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print ("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém sua quantidade de fichas.")
                                    fichas = fichas
                            #Apostas Any Craps e Twelve juntas na Fase Point
                            if aposta_p2 == "Any Craps e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e sete vezes o que apostou ")
                                    fichas = fichas + valor_da_aposta2 * 37
                                elif soma_dos_dados2 == 2 or soma_dos_dados2 == 3:
                                    print("Você ganhou seis vezes o que apostou.")
                                    fichas = fichas + valor_da_aposta2 * 6
                                else:
                                    print("Você perdeu o dobro do que apostou.")
                                    fichas = fichas - valor_da_aposta2 * 2
                            #Apostas Field e Twelve juntas na Fase Point
                            if aposta_p2 == "Field e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e três vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 33
                                elif soma_dos_dados2 == 2:
                                    print("Você ganhou o que apostou!")
                                    fichas = fichas + valor_da_aposta2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém a quantidade de fichas.")
                                    fichas = fichas

                        if quantidade_de_apostas2 == 3:
                            print("Você fará as três apostas de uma vez só")
                            #Apostas Any Craps, Field e Twelve juntas na Fase Point
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou quarenta vezes o que apostou!")
                                fichas = fichas +valor_da_aposta2 * 40
                            elif soma_dos_dados2 == 3:
                                print("Você ganhou o triplo do que apostou!")
                                fichas = fichas + valor_da_aposta2 * 3
                            elif soma_dos_dados2 == 2:
                                print("Você ganhou oito vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 8
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print("Você perdeu tudo que tinha!")
                                fichas = fichas - valor_da_aposta2
                            else:
                                print("Você perdeu o que apostou!")
                                fichas = fichas - valor_da_aposta2
                        #Condições da Fase Point
                        if soma_dos_dados2 == soma_dos_dados:
                            print('Você ganhou!')
                            fichas = fichas + valor_da_aposta
                            Point = False

                        elif soma_dos_dados2 == 7:
                            print('Você perdeu tudo!')
                            fichas = fichas - valor_da_aposta
                            Point = False

                        else:
                            print ('Reiniciando fase!')
                            Point = True

                        print('Você detém {0} fichas.'.format(fichas))


        if quantidade_de_apostas == 3:
            print('Começa agora a fase "Come Out"')
            print("Dentre as opções de aposta temos:")
            print("Any Craps, Field e Pass Line Bet")
            print("Any Craps, Field e Twelve")
            print("Field, Pass Line Bet e Twelve")
            aposta3 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
            #Apostas Any Craps, Field e Pass Line Bet juntas 
            if aposta3 == "Any Craps, Field e Pass Line Bet":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 2:
                    print("Você ganhou oito vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 8
                elif soma_dos_dados == 12:
                    print("Você ganhou nove vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 9
                elif soma_dos_dados == 3:
                    print("Você ganhou sete vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 7
                elif soma_dos_dados == 11:
                    print("Você ganhou o dobro de fichas que apostou!")
                    fichas = fichas + valor_da_aposta * 2
                elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                    print("Você perdeu tudo que apostou!")
                    fichas = fichas - valor_da_aposta
                else:
                    fichas = fichas
                    print("Você entrou na fase Point!")
                    Point = True
                    while Point and fichas !=0:
                        print('Você detém {0} fichas.'.format(fichas))
                        quantidade_de_apostas2= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3) "))
                        if quantidade_de_apostas2 == 1:
                            print("Dentre as opções de aposta temos: Any Craps, Field e Twelve")
                            aposta_p = input("Qual delas você escolherá?: ")
                            #Aposta Any Craps sozinha na Fase Point
                            if aposta_p == 'Any Craps':   
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                                    print('Você ganhou sete vezes a quantidade de fichas apostada!')
                                    fichas = fichas + valor_da_aposta2 * 7
                                else:
                                    print('Você perdeu!')
                                    fichas =  fichas - valor_da_aposta2

                            #Aposta "Twelve" sozinha na Fase Point
                            if aposta_p == 'Twelve':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 30
                                else:
                                    print('Você perdeu!')
                                    fichas = fichas - valor_da_aposta2

                            #Aposta "Field" sozinha na Fase Point
                            if aposta_p == 'Field':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou o triplo da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 3
                                elif soma_dos_dados2 == 2:
                                    print('Você ganhou o dobro da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print('Você perdeu tudo que apostou!')
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print('Você ganhou a mesma quantidade que apostou!')
                                    fichas = fichas + valor_da_aposta2
                        
                        if quantidade_de_apostas2 == 2:
                            print("Dentre as opções de aposta temos:")
                            print("Any Craps e Field")
                            print("Any Craps e Twelve")
                            print("Field e Twelve")
                            aposta_p2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
                            #Apostas Any Craps e Field juntas na Fase Point
                            if aposta_p2 == "Any Craps e Field":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2:
                                    print("Você ganhou nove vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 9
                                elif soma_dos_dados2 == 3:
                                    print("Você ganhou oito vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 8
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print ("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém sua quantidade de fichas.")
                                    fichas = fichas
                            #Apostas Any Craps e Twelve juntas na Fase Point
                            if aposta_p2 == "Any Craps e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e sete vezes o que apostou! ")
                                    fichas = fichas + valor_da_aposta2 * 37
                                elif soma_dos_dados2 == 2 or soma_dos_dados2 == 3:
                                    print("Você ganhou seis vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 6
                                else:
                                    print("Você perdeu o dobro do que apostou!")
                                    fichas = fichas - valor_da_aposta2 * 2
                            #Apostas Field e Twelve juntas na Fase Point
                            if aposta_p2 == "Field e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e três vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 33
                                elif soma_dos_dados2 == 2:
                                    print("Você ganhou o que apostou!")
                                    fichas = fichas + valor_da_aposta2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print("Você perdeu tudo que tinha!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém a quantidade de fichas.")
                                    fichas = fichas

                        if quantidade_de_apostas2 == 3:
                            print("Você fará as três apostas de uma vez só")
                            #Apostas Any Craps, Field e Twelve juntas na Fase Point
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou quarenta vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 40
                            elif soma_dos_dados2 == 3:
                                print("Você ganhou o triplo do que apostou!")
                                fichas = fichas + valor_da_aposta2 * 3
                            elif soma_dos_dados2 == 2:
                                print("Você ganhou oito vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 8
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print("Você perdeu tudo que apostou!")
                                fichas = fichas - valor_da_aposta2
                            else:
                                print("Você perdeu o que apostou!")
                                fichas = fichas - valor_da_aposta2
                        #Condições da Fase Point
                        if soma_dos_dados2 == soma_dos_dados:
                            print('Você ganhou!')
                            fichas = fichas + valor_da_aposta
                            Point = False

                        elif soma_dos_dados2 == 7:
                            print('Você perdeu tudo!')
                            fichas = fichas - valor_da_aposta
                            Point = False

                        else:
                            print ('Reiniciando fase!')
                            Point = True

                        print('Você detém {0} fichas.'.format(fichas))

            #Apostas Any Craps, Field e Twelve juntas
            if aposta3 == "Any Craps, Field e Twelve":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 12:
                    print("Você ganhou quarenta vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 40
                elif soma_dos_dados == 3:
                    print("Você ganhou o triplo do que apostou!")
                    fichas = fichas + valor_da_aposta * 3
                elif soma_dos_dados == 2:
                    print("Você ganhou oito vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 8
                elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                    print("Você perdeu tudo que apostou!")
                    fichas = fichas - valor_da_aposta
                else:
                    print("Você perdeu o que apostou!")
                    fichas = fichas - valor_da_aposta

            #Apostas Field, Pass Line Bet e Twelve juntas
            if aposta3 == "Field, Pass Line Bet e Twelve":
                Dado1 = random.randint(1,6)
                Dado2 = random.randint(1,6)
                soma_dos_dados = Dado1 + Dado2
                valor_da_aposta = int(input('Quanto você apostará?: '))
                print('Saiu a soma: {0}'.format(soma_dos_dados))
                if soma_dos_dados == 12:
                    print("Você ganhou trinta e duas vezes o que apostou!")
                    fichas = fichas + valor_da_aposta * 32
                elif soma_dos_dados == 11:
                    print("Você ganhou o dobro do que apostou!")
                    fichas = fichas + valor_da_aposta * 2
                elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                    print("Você perdeu tudo que apostou!")
                    fichas = fichas - valor_da_aposta
                else:
                    fichas = fichas
                    print("Você entrou na fase Point!")
                    Point = True
                    while Point and fichas != 0:
                        print('Você detém {0} fichas.'.format(fichas))
                        quantidade_de_apostas2= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3) "))
                        if quantidade_de_apostas2 == 1:
                            print("Dentre as opções de aposta temos: Any Craps, Field e Twelve")
                            aposta_p = input("Qual delas você escolherá?: ")
                            #Aposta Any Craps sozinha na Fase Point
                            if aposta_p == 'Any Craps':   
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                                    print('Você ganhou sete vezes a quantidade de fichas apostada!')
                                    fichas = fichas + valor_da_aposta2 * 7
                                else:
                                    print('Você perdeu!')
                                    fichas =  fichas - valor_da_aposta2

                            #Aposta "Twelve" sozinha na Fase Point
                            if aposta_p == 'Twelve':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 30
                                else:
                                    print('Você perdeu!')
                                    fichas = fichas - valor_da_aposta2

                            #Aposta "Field" sozinha na Fase Point
                            if aposta_p == 'Field':
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print('Você ganhou o triplo da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 3
                                elif soma_dos_dados2 == 2:
                                    print('Você ganhou o dobro da quantidade de fichas que apostou!')
                                    fichas = fichas + valor_da_aposta2 * 2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print('Você perdeu tudo que apostou!')
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print('Você ganhou a mesma quantidade que apostou!')
                                    fichas = fichas + valor_da_aposta2
                        
                        if quantidade_de_apostas2 == 2:
                            print("Dentre as opções de aposta temos:")
                            print("Any Craps e Field")
                            print("Any Craps e Twelve")
                            print("Field e Twelve")
                            aposta_p2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
                            #Apostas Any Craps e Field juntas na Fase Point
                            if aposta_p2 == "Any Craps e Field":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 2:
                                    print("Você ganhou nove vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 9
                                elif soma_dos_dados2 == 3:
                                    print("Você ganhou oito vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 8
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print ("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém sua quantidade de fichas.")
                                    fichas = fichas
                            #Apostas Any Craps e Twelve na Fase Point
                            if aposta_p2 == "Any Craps e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input('Quanto você apostará?: '))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e sete vezes o que apostou ")
                                    fichas = fichas + valor_da_aposta2 * 37
                                elif soma_dos_dados2 == 2 or soma_dos_dados2 == 3:
                                    print("Você ganhou seis vezes o que apostou.")
                                    fichas = fichas + valor_da_aposta2 * 6
                                else:
                                    print("Você perdeu o dobro do que apostou.")
                                    fichas = fichas - valor_da_aposta2*2
                            #Apostas Field e Twelve juntas na Fase Point
                            if aposta_p2 == "Field e Twelve":
                                Dado3 = random.randint(1,6)
                                Dado4 = random.randint(1,6)
                                soma_dos_dados2 = Dado3 + Dado4
                                valor_da_aposta2 = int(input("Quanto você apostará?: "))
                                print('Saiu a soma: {0}'.format(soma_dos_dados2))
                                if soma_dos_dados2 == 12:
                                    print("Você ganhou trinta e três vezes o que apostou!")
                                    fichas = fichas + valor_da_aposta2 * 33
                                elif soma_dos_dados2 == 2:
                                    print("Você ganhou o que apostou!")
                                    fichas = fichas + valor_da_aposta2
                                elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                    print("Você perdeu tudo que apostou!")
                                    fichas = fichas - valor_da_aposta2
                                else:
                                    print("Você mantém a quantidade de fichas.")
                                    fichas = fichas

                        if quantidade_de_apostas2 == 3:
                            print("Você fará as três apostas de uma vez só")
                            #Apostas Any Craps, Field e Twelve juntas na Fase Point
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou quarenta vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 40
                            elif soma_dos_dados2 == 3:
                                print("Você ganhou o triplo do que apostou!")
                                fichas = fichas + valor_da_aposta2 * 3
                            elif soma_dos_dados2 == 2:
                                print("Você ganhou oito vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 8
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print("Você perdeu tudo que apostou!")
                                fichas = fichas - valor_da_aposta2
                            else:
                                print("Você perdeu o que apostou!")
                                fichas = fichas - valor_da_aposta2
                        #Condições da Fase Point
                        if soma_dos_dados2 == soma_dos_dados:
                            print('Você ganhou!')
                            fichas = fichas + valor_da_aposta
                            Point = False

                        elif soma_dos_dados2 == 7:
                            print('Você perdeu tudo!')
                            fichas = fichas - valor_da_aposta
                            Point = False

                        else:
                            print ('Reiniciando fase!')
                            Point = True

                        print('Você detém {0} fichas.'.format(fichas))



        if quantidade_de_apostas == 4:
            print('Começa agora a fase "Come Out"') 
            #Apostas Any Craps, Field, Pass Line Bet e Twelve juntas
            print("Você fará as quatro apostas de uma vez, Any Craps, Field, Pass Line Bet e Twelve!")
            Dado1 = random.randint(1,6)
            Dado2 = random.randint(1,6)
            soma_dos_dados = Dado1 + Dado2
            valor_da_aposta = int(input('Quanto você apostará?: ')) 
            print('Saiu a soma: {0}'.format(soma_dos_dados))         
            if soma_dos_dados == 12:
                print("Você ganhou trinta e nove vezes o que apostou!")
                fichas = fichas + valor_da_aposta * 39
            elif soma_dos_dados == 2:
                print("Você ganhou sete vezes o que apostou!")
                fichas = fichas + valor_da_aposta * 7
            elif soma_dos_dados == 3:
                print("Você ganhou seis vezes o que apostou!")
                fichas = fichas + valor_da_aposta * 6
            elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                print("Você perdeu tudo que apostou!")
                fichas = fichas - valor_da_aposta
            else:
                fichas = fichas - valor_da_aposta
                print("Você entrou na fase Point!")
                Point = True
                while Point and fichas != 0:
                    print('Você detém {0} fichas.'.format(fichas))
                    quantidade_de_apostas2= int(input("Quantos tipos de aposta você gostaria de fazer?: (Digite 1,2,3) "))
                    if quantidade_de_apostas2 == 1:
                        print("Dentre as opções de aposta temos: Any Craps, Field e Twelve")
                        aposta_p = input("Qual delas você escolherá?: ")
                        #Aposta Any Craps sozinha na Fase Point
                        if aposta_p == 'Any Craps':   
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 2 or soma_dos_dados2 == 3 or soma_dos_dados2 == 12:
                                print('Você ganhou sete vezes a quantidade de fichas apostada!')
                                fichas = fichas + valor_da_aposta2 * 7
                            else:
                                print('Você perdeu!')
                                fichas =  fichas - valor_da_aposta2

                        #Aposta "Twelve" sozinha na Fase Point
                        if aposta_p == 'Twelve':
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                                fichas = fichas + valor_da_aposta2 * 30
                            else:
                                print('Você perdeu!')
                                fichas = fichas - valor_da_aposta2

                        #Aposta "Field" sozinha na Fase Point
                        if aposta_p == 'Field':
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print('Você ganhou o triplo da quantidade de fichas que apostou!')
                                fichas = fichas + valor_da_aposta2 * 3
                            elif soma_dos_dados2 == 2:
                                print('Você ganhou o dobro da quantidade de fichas que apostou!')
                                fichas = fichas + valor_da_aposta2 * 2
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print('Você perdeu tudo que tinha que apostou!')
                                fichas = fichas - valor_da_aposta2
                            else:
                                print('Você ganhou a mesma quantidade que apostou!')
                                fichas = fichas + valor_da_aposta2
                    
                    if quantidade_de_apostas2 == 2:
                        print("Dentre as opções de aposta temos:")
                        print("Any Craps e Field")
                        print("Any Craps e Twelve")
                        print("Field e Twelve")
                        aposta_p2 = input ("Qual deseja fazer? (Digite da maneira como foi apresentado)")
                        #Apostas Any Craps e Field juntas na Fase Point
                        if aposta_p2 == "Any Craps e Field":
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 2:
                                print("Você ganhou nove vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 9
                            elif soma_dos_dados2 == 3:
                                print("Você ganhou oito vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 8
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print ("Você perdeu tudo que apostou!")
                                fichas = fichas - valor_da_aposta2
                            else:
                                print("Você mantém sua quantidade de fichas.")
                                fichas = fichas
                        #Apostas Any Craps e Twelve juntas na Fase Point
                        if aposta_p2 == "Any Craps e Twelve":
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou trinta e sete vezes o que apostou ")
                                fichas = fichas + valor_da_aposta2 * 37
                            elif soma_dos_dados2 == 2 or soma_dos_dados2 == 3:
                                print("Você ganhou seis vezes o que apostou.")
                                fichas = fichas + valor_da_aposta2 * 6
                            else:
                                print("Você perdeu o dobro do que apostou.")
                                fichas = fichas - valor_da_aposta2 * 2
                        #Apostas Field e Twelve juntas na Fase Point
                        if aposta_p2 == "Field e Twelve":
                            Dado3 = random.randint(1,6)
                            Dado4 = random.randint(1,6)
                            soma_dos_dados2 = Dado3 + Dado4
                            valor_da_aposta2 = int(input('Quanto você apostará?: '))
                            print('Saiu a soma: {0}'.format(soma_dos_dados2))
                            if soma_dos_dados2 == 12:
                                print("Você ganhou trinta e três vezes o que apostou!")
                                fichas = fichas + valor_da_aposta2 * 33
                            elif soma_dos_dados2 == 2:
                                print("Você ganhou o que apostou!")
                                fichas = fichas + valor_da_aposta2
                            elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                                print("Você perdeu tudo que apostou!")
                                fichas = fichas - valor_da_aposta2
                            else:
                                print("Você mantém a quantidade de fichas.")
                                fichas = fichas

                    if quantidade_de_apostas2 == 3:
                        print("Você fará as três apostas de uma vez só Any Craps, Field e Twelve.")
                        #Apostas Any Craps, Field e Twelve juntas na Fase Point
                        Dado3 = random.randint(1,6)
                        Dado4 = random.randint(1,6)
                        soma_dos_dados2 = Dado3 + Dado4
                        valor_da_aposta2 = int(input('Quanto você apostará?: '))
                        print('Saiu a soma: {0}'.format(soma_dos_dados2))
                        if soma_dos_dados2 == 12:
                            print("Você ganhou quarenta vezes o que apostou!")
                            fichas = fichas +valor_da_aposta2 * 40
                        elif soma_dos_dados2 == 3:
                            print("Você ganhou o triplo do que apostou!")
                            fichas = fichas + valor_da_aposta2 * 3
                        elif soma_dos_dados2 == 2:
                            print("Você ganhou oito vezes o que apostou!")
                            fichas = fichas + valor_da_aposta2 * 8
                        elif soma_dos_dados2 == 5 or soma_dos_dados2 == 6 or soma_dos_dados2 == 7 or soma_dos_dados2 == 8:
                            print("Você perdeu tudo que apostou!")
                            fichas = fichas - valor_da_aposta2
                        else:
                            print("Você perdeu o que apostou!")
                            fichas = fichas - valor_da_aposta2
                    #Condições da Fase Point
                    if soma_dos_dados2 == soma_dos_dados:
                        print('Você ganhou!')
                        fichas = fichas + valor_da_aposta
                        Point = False

                    elif soma_dos_dados2 == 7:
                        print('Você perdeu tudo!')
                        fichas = fichas - valor_da_aposta
                        Point = False

                    else:
                        print ('Reiniciando fase!')
                        Point = True

                    print('Você detém {0} fichas.'.format(fichas))

    else:
        break
print("Jogo encerrado!")