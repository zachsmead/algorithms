def recursive_powers(number, power):
	if power == 0:
		return 1
	elif power == 1:
		return number
	elif power > 1 and power % 2 == 0:
		y = recursive_powers(number, power/2)
		return y * y
	elif power > 1 and power % 2 != 0:
		return number * recursive_powers(number, power - 1)
	elif power < 0:
		return 1/recursive_powers(number, -power)

print recursive_powers(2, 4)
print recursive_powers(2, 3)
print recursive_powers(2, 0)
print recursive_powers(2, -2)
