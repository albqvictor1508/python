salario = float(input('Digite seu salário:'))


if salario < 300:
    reajuste = salario * (35/100) + salario
    print(reajuste)
else:
    reajuste2 = salario * (15/100) + salario
    print(reajuste2)
