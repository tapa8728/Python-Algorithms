
# Palindrome Recursive Function - Tanvi

print "Welcome to palindrome function"

def palindrome(k): 
	if len(k) == 0 or len(k) == 1: 
		return "Palindrome "
	elif k[0] != word[len(k)-1]:
		return 
	else: 
		return palindrome(k[1:len(k)-1])


word = "radaradar"
for x in range(0, len(word)):
	for y in range(x, len(word)):
		m = word[x:y]
		print m
		print palindrome(m)
	
   
#print "radar:", palindromeFunc("radaradar")

