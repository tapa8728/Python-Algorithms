# Random prime number generator of n-digits - Tanvi

from random import randint

def next_prime(n):
	print n
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

	if prime_flag==0:
		print "number", n, "is prime";
	else:
		print "number", n, "not a prime";
	return n;

print "Welcome to Prime Checker!";
next_prime(2015**50);	


