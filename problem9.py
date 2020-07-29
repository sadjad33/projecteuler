'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
for a in range(1, 300):
	for b in range(a, 500):
		c2 = a ** 2 + b ** 2
		c = c2 ** 0.5
		if not c % 1:
			if a + b + c == 1000:
				print(a * b * c)
