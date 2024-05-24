opinioes = []

for i in range(5):
    espectadores = int(input('Digite sua opinião, 3 para ótimo, 2 para bom, 1 para regular: '))
    opinioes.append(espectadores)

    otimos = opinioes.count(3)
    bons = opinioes.count(2)
    regulares = opinioes.count(1)

print(f'{otimos} otimos {bons} bons {regulares} regulares')