escolha = str(input('Sim ou Não?\n'))

while escolha == 'Sim':
    distancia = float(input('Qual foi a distância percorrida pelo atleta?'))

    tempo = float(input('Qual foi o tempo gasto pelo atleta?'))

    vm = distancia / tempo
    print('velocidade média:',vm)

    escolha = str(input('Quer Continuar o programa? Sim ou Não:\n'))
else:
    print('Programa encerrado com sucesso!')

    
    