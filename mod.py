
# Modular Exponentiation - Tanvi

def modexp(x, y, N):
	if y==0:
		return 1
	z = modexp(x, (y/2), N)
	if y%2==0:
		return (z*z)%N
	else:
		return x*(z*z)%N

x= int(raw_input("Enter the value of x:"))
y= int(raw_input("Enter the value of exponent y:"))
N= int(raw_input("Enter the value of N:"))

print "Calculating modular exponentiation..."
print modexp(x, y, N)
