#Design de Software - Exercíçio Problema 1 
#Jogo Craps Insper
#Criadora: Letícia Sanchez
#Esse programa permite realizar apenas uma aposta por vez
import random

print("Olá")

nome = input("Qual o seu nome?")

print("Bem-vindo(a) ao Craps, {0}!".format(nome))

# Cada jogador começa cada um com 1000 fichas - Declaração de fichas
fichas = 1000

#Declaração de Seguir no jogo ou Sair
while fichas != 0:
    print('Você detém {0} fichas.'.format(fichas))
    seguir_no_jogo_ou_sair = input('Você deseja seguir no jogo ou sair. (Digite Seguir ou Sair): ')
    if seguir_no_jogo_ou_sair == 'Seguir':
        
        #Iniciando o jogo - Fase "Come Out"
        print('Começa agora a fase 1 - "Come Out"') 
        print('Você pode escolher entre quatro opções de aposta: Pass Line Bet, Any Craps, Field, Twelve.') #Declaração de opções de apostas e escolha
        aposta = input('Qual delas você escolherá?: ')
        
       # Aposta "Any Craps" (na Fase "Come Out")
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

        #Aposta "Twelve" (na Fase "Come Out")
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

        #Aposta "Field" (na Fase "Come Out")
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

        #Aposta "Pass Line Bet" (na fase "Come Out")
        if aposta == 'Pass Line Bet':
            Dado1 = random.randint(1,6)
            Dado2 = random.randint(1,6)
            soma_dos_dados = Dado1 + Dado2
            valor_da_aposta = int(input('Quanto você apostará?: '))
            print('Saiu a soma: {0}'.format(soma_dos_dados))
            if soma_dos_dados == 7 or soma_dos_dados == 11:
                print('Você mantém as fichas apostadas e recebe a mesma quantia apostada!')
                fichas = fichas + valor_da_aposta
            elif soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12:
                print('Você perdeu o que apostou!')
                fichas = fichas - valor_da_aposta

            #Início fase "Point" - (a soma dos dados em Pass Line Bet deram 4,5, 6, 8, 9 ou 10)
            else:
                print('Você entrou na fase Point!')
                Point = True
                while Point:
                    Dadon3 = random.randint(1,6)
                    Dadon4 = random.randint(1,6)
                    soma_dos_dados_2 = Dadon3 + Dadon4
                    aposta = input('Qual delas você escolherá?: ')
                    
                    if aposta == 'Any Craps':   
                        valor_da_aposta_2 = int(input('Quanto você apostará?: '))
                        print('Saiu a soma: {0}'.format(soma_dos_dados_2))
                        if soma_dos_dados_2 == 2 or soma_dos_dados_2 == 3 or soma_dos_dados_2 == 12:
                            print('Você ganhou sete vezes a quantidade de fichas apostada!')
                            fichas = fichas + valor_da_aposta_2 * 7
                        else:
                            print('Você perdeu!')
                            fichas =  fichas - valor_da_aposta_2

        #Aposta "Twelve" (nas fases seguintes)
                    if aposta == 'Twelve':
                        valor_da_aposta_2 = int(input('Quanto você apostará?: '))
                        print('Saiu a soma: {0}'.format(soma_dos_dados_2))
                        if soma_dos_dados_2 == 12:
                            print('Você ganhou trinta vezes a quantidade de fichas que apostou!')
                            fichas = fichas + valor_da_aposta_2 * 30
                        else:
                            print('Você perdeu!')
                            fichas = fichas - valor_da_aposta_2

        #Aposta "Field" (nas fases seguintes)
                    if aposta == 'Field':
                        valor_da_aposta_2 = int(input('Quanto você apostará?: '))
                        print('Saiu a soma: {0}'.format(soma_dos_dados_2))
                        if soma_dos_dados_2 == 12:
                            print('Você ganhou o triplo da quantidade de fichas que apostou!')
                            fichas = fichas + valor_da_aposta_2 * 3
                        elif soma_dos_dados_2 == 2:
                            print('Você ganhou o dobro da quantidade de fichas que apostou!')
                            fichas = fichas + valor_da_aposta_2 * 2
                        elif soma_dos_dados_2 == 5 or soma_dos_dados_2 == 6 or soma_dos_dados_2 == 7 or soma_dos_dados_2 == 8:
                            print('Você perdeu tudo que tinha!')
                            fichas = fichas - valor_da_aposta_2
                        else:
                            print('Você ganhou a mesma quantidade que apostou!')
                            fichas = fichas + valor_da_aposta_2

                
                    if soma_dos_dados_2 == soma_dos_dados:
                        print('Você ganhou!')
                        fichas = fichas + valor_da_aposta
                        Point = False

                    elif soma_dos_dados_2 == 7:
                        print('Você perdeu tudo!')
                        fichas = fichas - valor_da_aposta
                        Point = False

                    else :
                        print ('Reiniciando fase!')
                        Point = True

                    print('Você detém {0} fichas.'.format(fichas))
    else:
        break
    

print('Jogo encerrado!')
                        