'''
What is the 10 001st prime number?
'''


def isprime(number):
	for i in range(2, int(number ** 0.5) + 1):
		if not number % i:
			return False
			break
	return True


def nth_prime(nth):	
	prime_counter = 0
	number = 1
	while prime_counter < nth:
		number += 1
		if isprime(number):
			prime_counter += 1
	return(number)


print(nth_prime(10001))