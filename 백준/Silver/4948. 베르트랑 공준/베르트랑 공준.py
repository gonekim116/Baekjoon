import math
primes=[]
for i in range(2,2*123456+1):
	isPrime=True
	for j in primes:
		if j > math.sqrt(2*123456): break
		if i%j==0:
			isPrime=False
			break
	if isPrime:
		primes.append(i)
n=int(input())
while n!=0:
	print(len([p for p in primes if n<p and p<=2*n]))
	n=int(input())