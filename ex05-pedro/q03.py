sexos = []

for i in range(3):
    perguntas = str(input(f'Digite o sexo da {i + 1} pessoa: '))
    sexos.append(perguntas)

    homens = sexos.count('masculino')
    mulher = sexos.count('feminino')

print(sexos)
print(f'{homens} homens e {mulher} mulheres')