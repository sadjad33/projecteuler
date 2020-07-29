'''
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

b = 0
for x in range(900, 999):
	for y in range(900, 999):
		n = x * y
		nstr = str(n)
		if nstr == nstr[::-1] and n > b:
			b = n
print(b)