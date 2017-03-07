
def check_prime(y):

	for i in range(2,y):
		if (y % i) == 0:
			return False
	return True

def is_prime(y):
	prime_no_list =[]
	for i in range(2,y):
		
		if (y % i) == 0:
			prime_no_list.append(i)
		return prime_no_list

print is_prime(9)


			

