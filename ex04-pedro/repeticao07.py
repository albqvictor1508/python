numbers = []

for i in range(1,11):
    n = float(input(f"Digite o {i} número:\n"))
    numbers.append(n)
else:
    print(numbers)

for n in numbers:
    dobro = n * 2
    triplo = n * 3
print(f"\nNúmero: {n}, Dobro: {dobro}, Triplo: {triplo}")