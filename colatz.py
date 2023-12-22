def colatz(n):
	steps = [n]
	if n > 0 and isinstance(n, int):
		while n != 1:
			if n % 2 == 0:
				n = int(n / 2)
				steps.append(n)
			else:
				n = int(3 * n + 1)
				steps.append(n)
		print(f"{n} => {steps}")
		print(f"Кол-во шагов - {len(steps) - 1}")
	else: 
		print("Гиппотеза Колатца распростроняется только на натуральные числа!")


n = int(input("\nn = "))
while n != 0:
	colatz(n)
	n = int(input("\nn = "))
