import math
primes=[]
for i in range(2,10001):
	isPrime=True
	for j in primes:
		if j > math.sqrt(10000): break
		if i%j==0:
			isPrime=False
			break
	if isPrime:
		primes.append(i)
		
testcase=int(input())
for t in range(testcase):
	n=int(input())
	a = int(n/2)
	while True:
		if a in primes and n-a in primes:
			break
		a -= 1
	print(a,n-a)