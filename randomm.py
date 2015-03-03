# Application of Fermat's Theorem - Primality Check

from random import randint
def next_prime(n):
	prime_flag=0;
	for i in range(1, 1000):
		#print i
		a = randint(1, n-1)
		test = pow(a, n-1, n);
		if test==1:	#
			prime_flag=0;
		else:
			prime_flag=1;
			break;
		
	while(prime_flag==1):
		n=n+1;
		for i in range(1, 1000):
			#print i
			a = randint(1, n-1)
			test = pow(a, n-1, n);
			if test==1:	#
				prime_flag=0;
			else:
				prime_flag=1;
				break;		

	return n;

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

sum=0
for i in range(1, 1000):
	print i
	s = random_with_N_digits(100)
	n = next_prime(s)
	sum = sum + (n-s)

print "The average over 1000 samples is: ", (sum/1000)


