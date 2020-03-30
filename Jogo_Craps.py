#Design de Software - Exercíçio Problema 1 
#Jogo Craps Insper
#Criadora: Letícia Sanchez

import random


# Cada jogador começa cada um com 1000 fichas - Declaração de fichas
fichas = 1000

#Declaração de Seguir no jogo ou Sair
while fichas != 0:
    print('Você detém {0} fichas.'.format(fichas))
    seguir_no_jogo_ou_sair = input('Você deseja seguir no jogo ou sair. (Digite Seguir ou Sair)')
    if seguir_no_jogo_ou_sair == 'Seguir':
        
        #Iniciando o jogo - Fase 1
        print('Começa agora a fase "Come Out"') 
        print('Você pode escolher entre quatro opções de aposta: Pass Line Bet, Any Craps, Field, Twelve') #Declaração de opções de apostas e escolha
        aposta = input('Qual delas você escolherá?')

       # Aposta "Any Craps" (na Fase 1)
        if aposta == 'Any Craps':   
            Dado1 = random.randint(1,6)
            Dado2 = random.randint(1,6)
            soma_dos_dados = Dado1 + Dado2
            valor_da_aposta = int(input('Quanto você apostará?'))
            if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                print('Você ganhou sete vezes a quantidade de fichas apostada')
                fichas = fichas + valor_da_aposta * 7
            else:
                print('Você perdeu!')
                fichas =  fichas - valor_da_aposta

        #Aposta "Twelve" (na Fase 1)
        if aposta == 'Twelve':
            Dado1 = random.randint(1,6)
            Dado2 = random.randint(1,6)
            soma_dos_dados = Dado1 + Dado2
            valor_da_aposta = int(input('Quanto você apostará?'))
            if soma_dos_dados == 12:
                print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                fichas = fichas + valor_da_aposta * 30
            else:
                print('Você perdeu!')
                fichas = fichas - valor_da_aposta

        #Aposta "Field" (na Fase 1)
        if aposta == 'Field':
            Dado1 = random.randint(1,6)
            Dado2 = random.randint(1,6)
            soma_dos_dados = Dado1 + Dado2
            valor_da_aposta = int(input('Quanto você apostará?'))
            if soma_dos_dados == 12:
                print('Você ganhou o triplo da quantidade de fichas que apostou')
                fichas = fichas + valor_da_aposta * 3
            elif soma_dos_dados == 2:
                print('Você ganhou o dobro da quantidade de fichas que apostou')
                fichas = fichas + valor_da_aposta * 2
            elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 11:
                print('Você perdeu tudo que tinha')
                fichas = 0 
            else:
                print('Você ganhou a mesma quantidade que apostou')
                fichas = fichas + valor_da_aposta

        #Aposta "Pass Line Bet" (na fase 1)
        elif aposta == 'Pass Line Bet':
            Dado1 = random.randint(1,6)
            Dado2 = random.randint(1,6)
            soma_dos_dados = Dado1 + Dado2
            valor_da_aposta = int(input('Quanto você apostará?'))
            if soma_dos_dados == 7 or soma_dos_dados == 11:
                print('Você mantém as fichas apostadas e recebe a mesma quantia apostada')
                fichas = fichas + valor_da_aposta
            elif soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                print('Você perdeu o que apostou')
                fichas = fichas - valor_da_aposta

            #Início fase "Point" - Fase 2 (a soma dos dados em Pass Line Bet deram 4,5, 6, 8, 9 ou 10)
            else:
                print('Você entrou na fase Point')
                Point = True
                while Point:
                    nova_soma_dos_dados = soma_dos_dados
                    Dadon3 = random.randint(1,6)
                    Dadon4 = random.randint(1,6)
                    soma_dos_dados_2 = Dadon3 + Dadon4
                    print()
                    if soma_dos_dados_2 == nova_soma_dos_dados:
                        print('Você ganhou!')
                        fichas = fichas + aposta
                        Point = False

                    elif soma_dos_dados_2 == 7:
                        print('Você perdeu tudo')
                        fichas = 0
                        Point = False

                    else:
                        print ('Reiniciando fase')
                        Point = True



                

                

                while fichas != 0:
                    print('Você detém {0} fichas.'.format(fichas))
                    print('Escolha uma entre as três apostas: "Twelve", "Any Craps" ou "Field"')
                    aposta = input('Qual delas você escolherá?')
                    if aposta == 'Any Craps':
                        if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                            print('Você ganhou sete vezes a quantidade de fichas apostada')
                            fichas = fichas + valor_da_aposta * 7
                        else:
                            print('Você perdeu!')
                            fichas =  fichas - valor_da_aposta

                    elif aposta == 'Twelve':
                        if soma_dos_dados == 12:
                            print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                            fichas = fichas + valor_da_aposta*30
                        else:
                            print('Você perdeu!')
                            fichas = fichas - valor_da_aposta
                            
                    
                    elif aposta == 'Field':
                        if soma_dos_dados == 12:
                            print('Você ganhou o triplo da quantidade de fichas que apostou')
                            fichas = fichas + valor_da_aposta * 3
                        elif soma_dos_dados == 2:
                            print('Você ganhou o dobro da quantidade de fichas que apostou')
                            fichas = fichas + valor_da_aposta * 2
                        elif soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 11:
                            print('Você perdeu tudo que tinha')
                            fichas = 0 
                        else:
                            print('Você ganhou a mesma quantidade que apostou')
                            fichas = fichas + valor_da_aposta

                    
                





                #PAss Line BEt no point
                #while Point != nova_soma_dos_dados:
                    #if nova_soma_dos_dados == 7:
                        #print('Você perdeu tudo que tinha')
                        #fichas = 0
                        #Point = True
                    #elif nova_soma_dos_dados == Point:
                        #print('Você ganhou o mesmo valor que apostou')
                        #fichas = fichas + valor_da_aposta
                        #Point = False
                    #else:
                        #Point = True 

    else:
        break

print('Jogo encerrado')
