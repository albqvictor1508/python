numeros_reais = []
soma = 0

for pos in range(4):
    reais = int(input('Digite um número: '))
    numeros_reais.append(reais)
    soma += numeros_reais[pos]

print(f'a soma dos elementos {numeros_reais} deu {soma}, o menor número foi {min(numeros_reais)} e o maior foi {max(numeros_reais)}')
